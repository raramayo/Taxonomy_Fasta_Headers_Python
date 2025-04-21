#!/usr/bin/env python3
"""
--------------------------------------------------------------------------------
Taxonomy_Fasta_Headers Script
--------------------------------------------------------------------------------
Author:                            Rodolfo Aramayo
Work_Email:                        raramayo@tamu.edu
Personal_Email:                    rodolfo@aramayo.org
--------------------------------------------------------------------------------
Overview:
The Taxonomy_Fasta_Headers script is designed to reformat FASTA file headers
according to the source database and taxonomy information. FASTA files can
originate from various databases such as NCBI, UniRef, ENSEMBL, and Gencode,
each with its own header format. This script automates the process of
standardizing these headers by:

+ NCBI: Extracting the organism’s taxonomy from the last square-bracketed
segment (e.g., [Homo sapiens]), converting spaces to underscores (resulting in
Homo_sapiens), and prefixing it to the header.

+ UniRef: Locating the TaxID value within the header and prefixing the header
with TaxID_<number>: where <number> is the extracted TaxID.

+ ENSEMBL and Gencode: Requiring the user to provide taxonomy information via a
flag. The provided taxonomy is then prepended to the header.

The script carefully processes only the header lines (lines starting with >),
leaving the sequence data completely untouched. Additionally, it performs
essential validations such as ensuring the input file exists, confirming the
file is in FASTA format, and enforcing proper flag usage based on the selected
database.
--------------------------------------------------------------------------------
Copyright:
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <https://www.gnu.org/licenses/>.
--------------------------------------------------------------------------------
Version Number:
Version: 1.0.2
--------------------------------------------------------------------------------
"""

#-------------------------------------------------------------------------------
# Import dependencies
import argparse
import os
import re
import sys
#-------------------------------------------------------------------------------
# Defining Script Name
script_name = os.path.basename(sys.argv[0])

# Defining Script Current Version
script_version = "1.0.2"

# Defining_Script_Current_Version (date '+DATE:%Y/%m/%d%tTIME:%R')
current_version_date = "DATE:2025/04/21"
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Helper Functions
#-------------------------------------------------------------------------------

def validate_fasta(file_path):
    """
    Check that the FASTA file exists and its first line starts with '>'.
    """
    if not os.path.isfile(file_path):
        sys.exit("Error: FASTA file not found. Please provide a valid FASTA file.")
    with open(file_path, "r") as f:
        first_line = f.readline()
        if not first_line.startswith(">"):
            sys.exit("Error: The provided file does not appear to be in FASTA format.")

def process_ncbi_header(header):
    """
    Process an NCBI header.
    Expected input example:
      >NP_000005.3 alpha-2-macroglobulin isoform a precursor [Homo sapiens]
    Output example:
      >Homo_sapiens:NP_000005.3 alpha-2-macroglobulin isoform a precursor
    """
    header = header.lstrip(">").strip()
    # Identify the last square-bracketed group as the taxonomy
    match = re.search(r'\[([^\[\]]+)\]\s*$', header)
    if match:
        taxonomy = match.group(1).replace(" ", "_")
        # Remove the trailing taxonomy block from the header
        header_without_tax = re.sub(r'\s*\[[^\[\]]+\]\s*$', '', header).strip()
        new_header = f">{taxonomy}:{header_without_tax}"
        return new_header
    else:
        # If no taxonomy found, leave header unchanged
        return ">" + header

def process_uniref_header(header):
    """
    Process a UniRef header.
    Expected input example:
      >UniRef50_A0A2N2KJH1 Uncharacterized protein n=1 Tax=Deltaproteobacteria bacterium HGW-Deltaproteobacteria-12 TaxID=2013739 RepID=A0A2N2KJH1_9DELT
    Output example:
      >TaxID_2013739:UniRef50_A0A2N2KJH1 Uncharacterized protein n=1 Tax=Deltaproteobacteria bacterium HGW-Deltaproteobacteria-12 TaxID=2013739 RepID=A0A2N2KJH1_9DELT
    """
    header = header.lstrip(">").strip()
    match = re.search(r'TaxID=(\d+)', header)
    if match:
        taxid = match.group(1)
        new_header = f">TaxID_{taxid}:{header}"
        return new_header
    else:
        return ">" + header

def process_ensembl_header(header, taxonomy):
    """
    Process an ENSEMBL header by prefixing with the provided taxonomy.
    Expected input example:
      >ENSP00000354665.2 pep chromosome:GRCh38:MT:14149:14673:-1 gene:ENSG00000198695.2 ...
    Output example:
      >Homo_sapiens:ENSP00000354665.2 pep chromosome:GRCh38:MT:14149:14673:-1 gene:ENSG00000198695.2 ...
    """
    header = header.lstrip(">").strip()
    new_header = f">{taxonomy}:{header}"
    return new_header

def process_gencode_header(header, taxonomy):
    """
    Process a Gencode header by prefixing with the provided taxonomy.
    Expected input example:
      >ENST00000832831.1|ENSG00000290825.2|-|-|DDX11L16-267|DDX11L16|1300|lncRNA|
    Output example:
      >Homo_sapiens:ENST00000832831.1|ENSG00000290825.2|-|-|DDX11L16-267|DDX11L16|1300|lncRNA|
    """
    header = header.lstrip(">").strip()
    new_header = f">{taxonomy}:{header}"
    return new_header

def process_file(input_file, database, taxonomy, output_path):
    """
    Process each record in the FASTA file and write the modified headers to the output.
    """
    with open(input_file, "r") as fin, open(output_path, "w") as fout:
        current_header = None
        sequence_lines = []
        for line in fin:
            if line.startswith(">"):
                # Write the previous record (if any)
                if current_header is not None:
                    fout.write(current_header + "\n")
                    fout.write("".join(sequence_lines))
                original_header = line.rstrip("\n")
                # Choose the proper header processing based on the database flag
                if database.upper() == "NCBI":
                    new_header = process_ncbi_header(original_header)
                elif database.upper() == "UNIREF":
                    new_header = process_uniref_header(original_header)
                elif database.upper() == "ENSEMBL":
                    new_header = process_ensembl_header(original_header, taxonomy)
                elif database.upper() == "GENCODE":
                    new_header = process_gencode_header(original_header, taxonomy)
                else:
                    sys.exit("Error: Unsupported database type.")
                current_header = new_header
                sequence_lines = []
            else:
                # Preserve the sequence lines unaltered
                sequence_lines.append(line)
        # Write the final record
        if current_header is not None:
            fout.write(current_header + "\n")
            fout.write("".join(sequence_lines))

def main():
    parser = argparse.ArgumentParser(
      description="Taxonomy_Fasta_Headers: Reformat FASTA file headers based on the database origin.",
      formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
      "--fasta",
      required=True,
      help="Path to the FASTA file to process."
    )
    parser.add_argument(
      "--database",
      required=True,
      type=lambda s: s.upper(),
      choices=["NCBI", "UNIREF", "ENSEMBL", "GENCODE"],
      help="The database from which the FASTA file originates."
    )
    parser.add_argument(
      "--taxonomy",
      help="""Genus_Species information (e.g., Homo_sapiens).
Required for ENSEMBL and Gencode files.
Must not be provided for NCBI or UniRef files."""
    )
    parser.add_argument(
      "--output",
      help="""Output file path or directory.
If a directory is provided, the output file will be named
based on the input file with '_Tax_Headers.fa' appended."""
    )
    parser.add_argument(
      "-v",
      "--version",
      action="version",
      version=f"Taxonomy_Fasta_Headers.py Version: {script_version}",
      help="Show program version and exit"
    )
    args = parser.parse_args()

    # Validate the provided FASTA file
    validate_fasta(args.fasta)

    # Check taxonomy flag requirements
    if args.database.upper() in ["ENSEMBL", "GENCODE"]:
        if not args.taxonomy:
            sys.exit("Error: For ENSEMBL and Gencode FASTA files, the --taxonomy flag is required.")
        # Normalize taxonomy string (e.g., replace spaces with underscores)
        taxonomy = args.taxonomy.strip().replace(" ", "_")
    else:
        if args.taxonomy:
            sys.exit("Error: The --taxonomy flag should not be provided for NCBI or UniRef FASTA files.")
        taxonomy = None

    valid_extensions = (".fa", ".fasta", ".fsa", ".fna", ".ffn", ".faa")
    base_name = os.path.basename(args.fasta)

    if args.output:
        # Determine if output is intended as a directory.
        if args.output.endswith(os.sep) or os.path.basename(args.output) == "":
            # Output is a directory
            outdir = args.output
            if not os.path.exists(outdir):
                os.makedirs(outdir)
            output_file = os.path.join(outdir, os.path.splitext(base_name)[0] + "_Tax_Headers.fa")
        else:
            # Output is provided as a filename.
            output_dir = os.path.dirname(args.output)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
            if not args.output.lower().endswith(valid_extensions):
                output_file = args.output + ".fa"
            else:
                output_file = args.output
    else:
        output_file = os.path.join(os.path.dirname(args.fasta), os.path.splitext(base_name)[0] + "_Tax_Headers.fa")

    process_file(args.fasta, args.database, taxonomy, output_file)
    print(f"Processing complete. Output written to {output_file}")

if __name__ == "__main__":
    main()
