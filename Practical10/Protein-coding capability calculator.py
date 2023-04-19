#Here is an example
seq = 'AAAAATGCCCTAG'

str = seq.upper()
class calculator(object):
    def __init__(self,total_DNA, target_DNA):
        self.total = total_DNA
        self.target = target_DNA
    def count(self):
        if self.target > 0.5*self.total:
            print('protein-coding')
        elif self.target < 0.1*self.total:
            print('non-coding')
        else:
            print('unclear')
DNA = calculator(len(str),str.index('TAG') - str.index('ATG') + 3)
DNA.count()


#here you can input whatever you like
print("\nhere you can try a new DNA sequence")
seq = input('DNA sequence:')

str = seq.upper()
class calculator(object):
    def __init__(self,total_DNA, target_DNA):
        self.total = total_DNA
        self.target = target_DNA
    def count(self):
        if self.target > 0.5*self.total:
            print('protein-coding')
        elif self.target < 0.1*self.total:
            print('non-coding')
        else:
            print('unclear')
DNA = calculator(len(str),str.index('TAG') - str.index('ATG') + 3)
DNA.count()
