#Identify those genes containing a ‘TGA’ stop codon
#open the file first
#use re.compile to select the name of the gene and the sequence of the gene that ends with TGA
#create empty str "gene_name" and "gene"
#choose the name line and pick out the name, stored as new_gene_name
#choose the sequence lines and combine all the lines into one line, and pick out the ones that end with TGA, stored as new_gene
#combine new_gene_name and new_gene together and output it as a new file 'TGA_genes.fa' 

in_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
out_file =open('TGA_genes.fa','w')

import re
gene_name = re.compile(r'>(\S+)')
gene = re.compile(r'TGA$')


new_gene_name= ''
new_gene=''

with in_file as ip,out_file as op:
    for line in ip:
        if line.startswith('>'):
            new_gene_name = gene_name.match(line).group()
            new_gene=''
        else:
            new_gene+=line.strip()
            if gene.search(new_gene):
                op.write('{}\n{}\n\n'.format(new_gene_name,new_gene))

in_file.close()
out_file.close()
