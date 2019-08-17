import Bio
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio.Blast.NCBIWWW import _parse_qblast_ref_page


def first_blast(test):
    my_query = SeqIO.read(test, format="fasta")  # Read fasta file
    result_handle = NCBIWWW.qblast("blastp", "nr", my_query.seq, hitlist_size=30)# blast it in ncbi,
#                                                                                # hitsize need to put more,
#                                                                                # blastp -- program for proteins
#                                                                                # nr -- database for proteins
    blast_result = open("my_blast.xml", "w")  # Write result into xml
    blast_result.write(result_handle.read())
    blast_result.close()
    result_handle.close()

def xml_parse(my_blast):
    db_file = open("db_file.fasta", "w")
    E_VALUE_THRESH = 1e-20 # Changeable
    for record in NCBIXML.parse(open(my_blast)):
        if record.alignments:
            print("\n")
            for align in record.alignments:
                for hsp in align.hsps:
                    if hsp.expect < E_VALUE_THRESH:
                        db_file.write(">" + align.title + '\n' + hsp.sbjct + '\n')
    db_file.close()


def result_parse(db_exp):
    result_file = open("result_file.fasta", "w")
    for seq_record in SeqIO.parse(db_exp, "fasta"):
        result_file.write(">" + seq_record.description + '\n' + str(seq_record.seq) + '\n')
    result_file.close()

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
