[![alt_text](https://zenodo.org/badge/DOI/10.5281/zenodo.14967827.svg)](https://doi.org/10.5281/zenodo.14967827)

# Taxonomy_Fasta_Headers

<p align="center">
<img src="https://github.com/raramayo/Taxonomy_Fasta_Headers_Python/blob/main/Images/Taxonomy_Fasta_Headers_Logo.png" width="400" height="400" style="display: block; margin: 0 auto">

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

## Motivation:

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
	Author:         Rodolfo Aramayo
    Work_Email:     raramayo@tamu.edu
    Personal_Email: rodolfo@aramayo.org
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

## Version:

	--------------------------------------------------------------------------------
	v1.0.2
	--------------------------------------------------------------------------------

## Code_Overview:

<pre>
--------------------------------------------------------------------------------
<a href="https://github.com/raramayo/Taxonomy_Fasta_Headers_Python/blob/main/Docs/Code_Overview.md" target="_blank">Code_Overview.md</a>
--------------------------------------------------------------------------------
</pre>

## Usage:

<pre>
--------------------------------------------------------------------------------
<a href="https://github.com/raramayo/Taxonomy_Fasta_Headers_Python/blob/main/Docs/Mini_Tutorial.md" target="_blank">Mini_Tutorial.md</a>
--------------------------------------------------------------------------------
</pre>

## Flags:

	--------------------------------------------------------------------------------
	FLAG:           "--fasta"
    REQUIRED:       "Yes"
    FORMAT:         "Alphanumeric String"
    DEFAULT:        "No default"
    HELP:           "Path to the FASTA file to process."
	--------------------------------------------------------------------------------
	FLAG:           "--database"
    REQUIRED:       "Yes"
    FORMAT:         "Alphanumeric String"
    CHOICES:        "NCBI", "UNIREF", "ENSEMBL", "GENCODE"
    DEFAULT:        "No default"
    HELP:           "The database from which the FASTA file originates."
	--------------------------------------------------------------------------------
    FLAG:           "--taxonomy"
    REQUIRED:       "Yes"
    FORMAT:         "Alphanumeric String"
    DEFAULT:        "No default"
    HELP:           "Genus_Species information (e.g., Homo_sapiens)."
	                "Required for ENSEMBL and Gencode files."
	                "Must not be provided for NCBI or UniRef files."
	--------------------------------------------------------------------------------
    FLAG:           "--output"
    REQUIRED:       "No"
    FORMAT:         "Alphanumeric"
    DEFAULT:        "Transcripts_Plots_dir_Run01"
    HELP:           "Output directory name."
	                "If provided and exists, a numeric suffix is added (e.g., Test01)"
	--------------------------------------------------------------------------------
    FLAG:           "-v", "--version"
    REQUIRED:       "No"
    ACTION:         "version"
    FORMAT:         "Alphanumeric"
    HELP:           "Show program version's number and exit"
	--------------------------------------------------------------------------------
    FLAG:           "-h", "--help"
    REQUIRED:       No
    ACTION:         help
    FORMAT:         Alphanumeric String
    HELP:           show this help message and exit
    --------------------------------------------------------------------------------

## Dependencies:

	--------------------------------------------------------------------------------
    Python3:        Required:
                        https://www.python.org/downloads/
	--------------------------------------------------------------------------------

## Development/Testing Environment:

    --------------------------------------------------------------------------------
    Distributor ID: Apple, Inc.
    Description:    Apple M1 Max
    Release:        15.3.1
    Codename:       Sequoia

    Script was tested with:
                    | Python Version | matplotlib | pandas | seaborn |
                    |----------------|------------|--------|---------|
                    | 3.8.20         | 3.7.5      | 2.0.3  | 0.13.2  |
                    | 3.9.21         | 3.9.4      | 2.2.3  | 0.13.2  |
                    | 3.10.16        | 3.10.1     | 2.2.3  | 0.13.2  |
                    | 3.11.11        | 3.10.1     | 2.2.3  | 0.13.2  |
                    | 3.12.9         | 3.10.1     | 2.2.3  | 0.13.2  |
                    | 3.13.2         | 3.10.1     | 2.2.3  | 0.13.2  |
    --------------------------------------------------------------------------------

## Repository:

<pre>
--------------------------------------------------------------------------------
<a href="https://github.com/raramayo/Taxonomy_Fasta_Headers_Python" target="_blank">Taxonomy_Fasta_Headers_Python</a>
--------------------------------------------------------------------------------
</pre>

## Issues:

<pre>
--------------------------------------------------------------------------------
<a href="https://github.com/raramayo/Taxonomy_Fasta_Headers_Python/issues" target="_blank">Taxonomy_Fasta_Headers_Python_Issues</a>
--------------------------------------------------------------------------------
</pre>
