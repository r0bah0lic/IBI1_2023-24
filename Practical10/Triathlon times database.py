class triathlon(object):
	def __init__(self, first_name, last_name, location,swim, cycle, run ):
		self.first = first_name
		self.last = last_name
		self.l = location
		self.s = swim
		self.c = cycle
		self.r = run
	def add(self):
		total = self.s + self.c + self.r
		return total
athlete = triathlon('MYan','Misaki','Japan',3,4,5)
print('first name:',athlete.first,' ','last name:',athlete.last,' ','location:',athlete.l,' ','swim time:',athlete.s,' ','cycle time:',athlete.c,' ','run time:',athlete.r,' ','total time:',athlete.add())
