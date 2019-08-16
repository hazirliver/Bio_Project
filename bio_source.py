import Bio
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio.Blast.NCBIWWW import _parse_qblast_ref_page

#help(NCBIWWW.qblast)
base_dir = 'C:\\Users\\Арсений\\PycharmProjects\\Bio_Project'


## First protein blasting
my_query = SeqIO.read("test.fasta", format="fasta") # Read fasta file
result_handle = NCBIWWW.qblast("blastp", "nr", my_query.seq, hitlist_size = 10000) # blast it in ncbi,
                                                                                         # hitsize need to put more,
                                                                                         # blastp -- program for proteins
                                                                                         # nr -- database for proteins
blast_result = open("my_blast.xml", "w") # Write result into xml
blast_result.write(result_handle.read())
blast_result.close()
result_handle.close()

## Parse received xml and create fasta file for further making database

#accession_list = [] # accession numbers list
db_file = open("db_file.fasta", "w")

E_VALUE_THRESH = 1e-20
for record in NCBIXML.parse(open("my_blast.xml")):
    if record.alignments:
       print("\n")
       #print(record.query)
      # print("query: %s" % record.query[:100])
       for align in record.alignments:
          for hsp in align.hsps:
             if hsp.expect < E_VALUE_THRESH:

                db_file.write(">" + align.title + '\n' + hsp.sbjct + '\n')
                #print("match: %s " % align.title[:100])
                #accession_list.append(align.accession)
db_file.close()

