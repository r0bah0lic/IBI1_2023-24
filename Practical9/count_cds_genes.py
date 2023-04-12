import os
os.chdir("/Users/misaki/IBI1_2022-23/Practical9")

in_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')

fname = input('input TAA, TAG or TGA: ')

out_file =open('{}_genes.fa'.format(fname),'w')

import re
gene_name = re.compile(r'>(\S+)')
gene = re.compile(r'{}$'.format(fname))


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
                count = len(re.findall(fname,new_gene))
                op.write('{}:__{}\n{}\n\n'.format(new_gene_name,count,new_gene))


