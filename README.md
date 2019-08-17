# Bio_Project
Blasting protein-protein sequences
Using for double blast
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
    result_parse("exported_from_genome_workbench.fasta")
