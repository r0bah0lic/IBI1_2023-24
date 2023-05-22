#automatically count the total number of possible coding sequences formed by this sequence
#first input the seq
#find the begins ATG
#count the number of TGA, let it be a
#count the number of TAA, let it be b
#add a and b


seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
l = seq.find('ATG')
a = seq.count('TGA',l)
b = seq.count('TAA',l)
print(a+b)
