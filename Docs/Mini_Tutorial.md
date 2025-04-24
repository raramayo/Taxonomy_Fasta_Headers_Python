[![alt_text](https://zenodo.org/badge/DOI/10.5281/zenodo.14967827.svg)](https://doi.org/10.5281/zenodo.14967827)

# Taxonomy_Fasta_Headers Mini Tutorial

## Summary of How to Use the Script:

### Input File:

+ Use the `--fasta` flag to specify the path to your FASTA file.
+ Example:

```
--fasta path/to/your_file.fa
```

### Database Selection:

+ Use the `--database` flag to indicate the origin of the FASTA file. Acceptable values are:
  + NCBI
  + UniRef
  + ENSEMBL
  + Gencode
+ Example:

```
--database NCBI
```

### Taxonomy Information:

+ For ENSEMBL and Gencode files, the `--taxonomy` flag is required.
+ This flag should provide the organism’s taxonomy (e.g., Homo_sapiens or "Homo sapiens").
+ Examples:

```
--taxonomy "Homo sapiens"
--taxonomy 'Homo sapiens'
--taxonomy Homo_sapiens
```

+ For NCBI and UniRef files, this flag must not be provided.

### Output Specification:

+ Optionally, use the `--output` flag to designate either a full output file path or just a directory.
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

### For a NCBI FASTA File:

```
python3 Taxonomy_Fasta_Headers.py \
--fasta input_ncbi.fa \
--database NCBI
```

+ This command processes an NCBI FASTA file by extracting taxonomy
  from the header and writes the output as input_ncbi_Tax_Headers.fa
  in the same directory as the input file.

### For an ENSEMBL FASTA File:

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

### Version:

```
python3 Taxonomy_Fasta_Headers.py -v
```

or

```
python3 Taxonomy_Fasta_Headers.py --version
```

### Help:

```
python3 Taxonomy_Fasta_Headers.py -h
```

or

```
python3 Taxonomy_Fasta_Headers.py --help
```

## Repository:

<pre>
<a href="https://github.com/raramayo/Taxonomy_Fasta_Headers_Python" target="_blank">Taxonomy_Fasta_Headers_Python</a>
</pre>

## Issues:

<pre>
<a href="https://github.com/raramayo/Taxonomy_Fasta_Headers_Python/issues" target="_blank">Taxonomy_Fasta_Headers_Python_Issues</a>
</pre>
