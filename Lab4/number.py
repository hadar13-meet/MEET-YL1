class Integer(object):
	def __init__(self, n, pos_or_neg):
		self.number = n
		self.pon = pos_or_neg
	def display(self):
		print self.pon + str(self.number)

class NegativeInteger(Integer):
	def __init__(self, n):
		super(NegativeInteger, self).__init__(n, "-")
		
	def display(self):
		print "-" + str(self.number)

			
if __name__=="__main__":
	test = NegativeInteger(76)
	test.display()
	
	
	
