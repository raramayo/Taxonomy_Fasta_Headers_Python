# Taxonomy_Fasta_Headers
![alt text](https://github.com/raramayo/Taxonomy_Fasta_Headers_Python/blob/main/Images/Taxonomy_Fasta_Headers_Logo.png)

## Overview:

    --------------------------------------------------------------------------------
    The Taxonomy_Fasta_Headers script is designed to reformat FASTA file headers
    according to the source database and taxonomy information. FASTA files can
    originate from various databases such as NCBI, UniRef, ENSEMBL, and Gencode,
    each with its own header format. This script automates the process of
    standardizing these headers by:

    + NCBI:
	  Extracting the organism’s taxonomy from the last square-bracketed segment
	  (e.g., [Homo sapiens]), converting spaces to underscores (resulting in Homo_sapiens),
	  and prefixing it to the header.

    + UniRef:
	  Locating the TaxID value within the header and prefixing the header with
	  TaxID_<number>: where <number> is the extracted TaxID.

    + ENSEMBL and Gencode: Requiring the user to provide taxonomy information
	  via a flag. The provided taxonomy is then prepended to the header.

    The script carefully processes only the header lines (lines starting with >),
    leaving the sequence data completely untouched. Additionally, it performs
    essential validations such as ensuring the input file exists, confirming the
    file is in FASTA format, and enforcing proper flag usage based on the selected
    database.
    --------------------------------------------------------------------------------

## Motivation

	--------------------------------------------------------------------------------
    Computational genomics encompasses the searching, clustering,
    comparison, and evaluation of vast numbers of sequences from a diverse
    array of organisms.

    Although individual transcriptome and proteome sequences are typically
    assigned unique identifiers, prepending each identifier with its
    corresponding taxonomy information significantly enhances the clarity
    and interpretability of computational outputs. By incorporating
    taxonomy data directly into sequence headers, researchers can more
    easily trace the organismal origin of each sequence, thereby
    streamlining downstream analyses and improving overall data
    integration.
	--------------------------------------------------------------------------------

## Authorship:

    --------------------------------------------------------------------------------
	Author:                          Rodolfo Aramayo
    Work_Email:                      raramayo@tamu.edu
    Personal_Email:                  rodolfo@aramayo.org
    --------------------------------------------------------------------------------

## Copyright:

    --------------------------------------------------------------------------------
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or (at
    your option) any later version.

    This program is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
    General Public License for more details.

	You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/>.
    --------------------------------------------------------------------------------

## Script_Version:

	--------------------------------------------------------------------------------
	v1.0.0
	--------------------------------------------------------------------------------

## Script_Usage:
## Summary of How to Use the Script
+ ### Input File:
  + Use the ```-f``` or ```--fasta``` flag to specify the path to your FASTA file.
  + Example:
    ```
    --fasta path/to/your_file.fa
    ```
+ ### Database Selection:
  + Use the ```-d``` or ```--database``` flag to indicate the origin of the FASTA file. Acceptable values are:
    + NCBI
    + UniRef
    + ENSEMBL
    + Gencode
  + Example:
    ```
    --database NCBI
    ```
+ ### Taxonomy Information:
  + For ENSEMBL and Gencode files, the ```-t``` or ```--taxonomy``` flag is required.
  + This flag should provide the organism’s taxonomy (e.g., Homo_sapiens or "Homo sapiens").
  + Examples:
    ```
    --taxonomy "Homo sapiens"
	--taxonomy 'Homo sapiens'
	--taxonomy Homo_sapiens
    ```
  + For NCBI and UniRef files, this flag must not be provided.
+ ### Output Specification:
  + Optionally, use the ```-o``` or ```--output``` flag to designate either a full output file path or just a directory.
    + If a directory is given, the script will create an output file in
    that directory named based on the input file (with _Tax_Headers.fa
    appended).
    + If the full path (directory + filename) is provided, the script will write the output accordingly.
  + Example (directory):
    ```
    --output /path/to/output_directory/
    ```
  + Example (full path):
    ```
    --output /path/to/output_directory/custom_output.fa
    ```
## Example Commands:
+ ### For a NCBI FASTA File:
  ```
  python3 Taxonomy_Fasta_Headers.py \
  --fasta input_ncbi.fa \
  --database NCBI
  ```
  + This command processes an NCBI FASTA file by extracting taxonomy
  from the header and writes the output as input_ncbi_Tax_Headers.fa
  in the same directory as the input file.
+ ### For an ENSEMBL FASTA File:
  ```
  python3 Taxonomy_Fasta_Headers.py \
  --fasta input_ensembl.fa \
  --database ENSEMBL \
  --taxonomy "Homo sapiens" \
  --output /path/to/output_directory/
  ```
  + This command processes an ENSEMBL FASTA file by prepending
  Homo_sapiens: (converted from the provided taxonomy) to each header,
  with the output written to the specified directory.
+ ### Show Version:
  ```
  python3 Transcripts_Plots.py \
  --version
  ```
## Script_Flags:

	--------------------------------------------------------------------------------
	FLAG:                            "-f", "--fasta"
    REQUIRED:                        "Yes"
    FORMAT:                          "Alphanumeric String"
    DEFAULT:                         "No default"
    HELP:                            "Path to the FASTA file to process."
	--------------------------------------------------------------------------------
	FLAG:                            "-d", "--database"
    REQUIRED:                        "Yes"
    FORMAT:                          "Alphanumeric String"
    CHOICES:                         "NCBI", "UNIREF", "ENSEMBL", "GENCODE"
    DEFAULT:                         "No default"
    HELP:                            "The database from which the FASTA file originates."
	--------------------------------------------------------------------------------
    FLAG:                            "-t", "--taxonomy"
    REQUIRED:                        "Yes"
    FORMAT:                          "Alphanumeric String"
    DEFAULT:                         "No default"
    HELP:                            "Genus_Species information (e.g., Homo_sapiens)."
	                                 "Required for ENSEMBL and Gencode files."
	                                 "Must not be provided for NCBI or UniRef files."
	--------------------------------------------------------------------------------
    FLAG:                            "-o", "--output"
    REQUIRED:                        "No"
    FORMAT:                          "Alphanumeric"
    DEFAULT:                         "Transcripts_Plots_dir_Run01"
    HELP:                            "Output directory name."
	                                 "If provided and exists, a numeric suffix is added (e.g., Test01)"
	--------------------------------------------------------------------------------
    FLAG:                            "-v", "--version"
    REQUIRED:                        "No"
    ACTION:                          "version"
    FORMAT:                          "Alphanumeric"
    HELP:                            "Show program version's number and exit"
	--------------------------------------------------------------------------------

## Dependencies:

	--------------------------------------------------------------------------------
    None
	--------------------------------------------------------------------------------

## Development/Testing Environment:

	--------------------------------------------------------------------------------
    Distributor ID:                  Apple, Inc.
    Description:                     Apple M1 Max
    Release:                         15.3.1
    Codename:                        Sequoia
	--------------------------------------------------------------------------------

## Repository:

	--------------------------------------------------------------------------------
    https://github.com/raramayo/Taxonomy_Fasta_Headers_Python
	--------------------------------------------------------------------------------

## Issues:

	--------------------------------------------------------------------------------
    https://github.com/raramayo/Taxonomy_Fasta_Headers_Python/issues
	--------------------------------------------------------------------------------
