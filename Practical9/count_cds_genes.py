#open the given file
#input the 'TGA', 'TAA' or 'TAG'
#use re.compile to select the name of the gene and the sequence of the gene that ends with particular promoter
#create empty str "gene_name" and "gene"
#choose the name line and pick out the name, stored as new_gene_name
#choose the sequence lines and combine all the lines into one line, and pick out the ones that end with particular promoter, stored as new_gene
#combine new_gene_name and new_gene together and output it as a new file 'particular promoter_genes.fa'
#use len and re.findall to count the number of particular promoter

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

in_file.close()
out_file.close()
