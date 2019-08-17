# Bio_Project
Blasting protein-protein sequences
Using for double blast
The current files stored in this repository were obtained during the test run of the script
------------------------------------
>bio_source.py            -- source script file

>test.fasta               -- first blasting protein sequence
>test2.fasta              -- second blasting protein sequence

>my_blast.xml             -- BLAST results after first blasting
>first_try_export.fasta   -- Genome Workbench BLAST results after second blasting

>db_file.fasta            -- MultiFasta database file
>db_file.fasta.psq        -- DataBase file for Genome Workbench

>result_file.fasta        -- Finish fasta file with second blasted proteins with their description and sequences


------------------------------------
#1) First protein blasting:
    first_blast("first_protein.fasta")

#2) Parse received xml and create fasta file for further making database:
    xml_parse("my_blast.xml")

#3) Linux terminal command:
    #$ makeblastdb -in db_file.fasta -title "my_database" -dbtype prot

#4) Use genome workbench with second protein to blast its against database received in previous step (Need a .psq file)

#5) Save received blast results from genome workbench as fasta sequnces file

#6) Parse final fasta file
    result_parse("first_try_export.fasta")
