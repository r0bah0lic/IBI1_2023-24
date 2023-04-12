seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
l = seq.find('ATG')
a = seq.count('TGA',l)
b = seq.count('TAA',l)
print(a+b)
