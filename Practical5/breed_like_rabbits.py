#let i be the generation,and asumme it is from 1-8
for i in range(1,8):
#n is the number of the total rabbits
  n=2**i
#we want it to stop when total number of rabbits is larger than 100
  if n <= 100:
    print(i, "st generation", "are", n, "rabbits" )  
  if n >= 100:
    print("the number of generations required to exceed 100 rabbits is", 
i)  
