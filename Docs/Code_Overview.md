# Taxonomy_Fasta_Headers_Pseudocode

## Pseudo-Code Outline:

```
BEGIN
    // Parse Command-Line Arguments
    CREATE argument parser with:
        - Required flag: --fasta (input FASTA file)
        - Required flag: --database (choices: NCBI, UNIREF, ENSEMBL, Gencode)
        - Optional flag: --taxonomy (required for ENSEMBL and Gencode; forbidden for NCBI or UNIREF)
        - Optional flag: --output (specifies output file/directory)
        - Optional flag: --version

    // Validate the Provided FASTA File
    IF FASTA file does not exist THEN
        PRINT "Error: FASTA file not found. Please provide a valid FASTA file."
        EXIT
    ELSE
        OPEN file and READ first line
        IF first line does not start with ">" THEN
            PRINT "Error: The provided file does not appear to be in FASTA format."
            EXIT

    // Check Taxonomy Flag Requirements
    IF database is ENSEMBL or Gencode THEN
        IF taxonomy flag is not provided THEN
            PRINT error message and EXIT
        ELSE
            Normalize taxonomy (replace spaces with underscores)
    ELSE IF taxonomy flag is provided for NCBI or UNIREF THEN
        PRINT error message and EXIT

    // Determine Output File Name
    IF --output argument is provided THEN
        IF output ends with a path separator OR basename is empty THEN
            TREAT output as a directory:
                CREATE directory if it does not exist
                SET output_file = (directory) + (input basename + "_Tax_Headers.fa")
        ELSE
            TREAT output as a filename:
                CREATE parent directory if necessary
                IF filename does not end with a valid FASTA extension THEN
                    APPEND ".fa" to filename
                SET output_file accordingly
    ELSE
        SET output_file = (input file directory) + (input basename + "_Tax_Headers.fa")

    // Process Each Record in the FASTA File
    OPEN input FASTA file for reading
    OPEN output_file for writing
    INITIALIZE current_header and sequence_lines
    FOR each line in the input file:
        IF line starts with ">" THEN
            IF current_header exists THEN
                WRITE current_header and sequence_lines to output
            END IF
            BASED on database type:
                CALL the corresponding header processing function
                    - For NCBI: process_ncbi_header
                    - For UNIREF: process_uniref_header
                    - For ENSEMBL: process_ensembl_header (using taxonomy)
                    - For Gencode: process_gencode_header (using taxonomy)
            SET current_header to the processed header
            RESET sequence_lines
        ELSE
            APPEND line to sequence_lines (preserve sequence data)
    END FOR
    WRITE final record (current_header and sequence_lines) to output
    CLOSE input and output files

    PRINT "Processing complete. Output written to" output_file
END
```

## Function-Specific Pseudo-code Outline:

```
FUNCTION process_ncbi_header(header_line):
    REMOVE ">" from header_line
    EXTRACT taxonomy from the trailing square brackets (e.g., [Homo sapiens])
    REPLACE spaces in taxonomy with underscores (e.g., Homo_sapiens)
    REMOVE the taxonomy part from header_line
    RETURN ">" + taxonomy + ":" + modified header_line

FUNCTION process_uniref_header(header_line):
    REMOVE ">" from header_line
    EXTRACT TaxID using regex (e.g., TaxID=123456)
    RETURN ">" + "TaxID_" + TaxID + ":" + header_line

FUNCTION process_ensembl_header(header_line, taxonomy):
    REMOVE ">" from header_line
    RETURN ">" + taxonomy + ":" + header_line

FUNCTION process_gencode_header(header_line, taxonomy):
    REMOVE ">" from header_line
    RETURN ">" + taxonomy + ":" + header_line
```
