#What is the number of the generation?
#The first generation has 2 rabbits
#if the number of rabbits(n) is smaller than 100
#the generation(i) will add one
#if the number of rabbits(n) is larger than 100
#print the generation number that has more than 100 rabbits
i=1
n=2
while n<=100:
  n=2**i
  i+=1

print("the number of generations required to exceed 100 rabbits is",
i-1)
