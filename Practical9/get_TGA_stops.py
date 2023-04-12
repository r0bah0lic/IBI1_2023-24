#Identify those genes containing a ‘TGA’ stop codon
import os
os.chdir("/Users/misaki/IBI1_2022-23/Practical9")
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

