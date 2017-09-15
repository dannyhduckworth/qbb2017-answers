
1) Run BLAST on query sequences.

./blastn -db nr -remote -query week1_query.fa -evalue 1e-4 -num_alignments 1000 -outfmt "6 sseqid sseq" -out 1000_homologs

2) Convert BLAST tsv --> fa
Remove gaps in sequence

awk '{gsub ("-","")} {print ">"$1"\n"$2}' blast_alignment.tsv > 1000_homologues.fa


3) Convert DNA sequence to protein sequence

transeq 1000_homologues.fa 1000_h_prot.fa


4) Align protein sequence, introducing gaps. 

mafft 1000_h_prot.fa alignment_prot.fa


5) Realign the protein sequence with DNA to introduce gaps. See the other attached .py files. 