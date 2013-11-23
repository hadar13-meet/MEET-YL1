import random

def flip():
	n = raw_input("Next flip? press n")
	list = []
	while n == "n":
		num = random.randint(0,2)
		if num == 1:
			list.append("H")
			print"H"
		else:
			list.append("T")
			print "T"
		
		n = raw_input("Next flip? press n")
	return list


def flip2():
	pro = float(raw_input("Please put probibility of coin flip as a float(shever) smaller than 1"))
	n = raw_input("Next flip? press n")
	list = []
	while n == "n":
		num = random.random()
		if num < pro:
			list.append("H")
			print"H"
		else:
			list.append("T")
			print "T"
		
		n = raw_input("Next flip? press n")
	return list


def flip3():
	n = int(raw_input("How many times to flip the coin?"))
	list = []
	for p in xrange(n):
		num = random.randint(0,2)
		if num == 1:
			list.append("H")
			
		else:
			list.append("T")
			
		
	return list

def flip4(n, pro):
	list = []
	for p in xrange(n):
		num = random.random()
		if num < pro:
			list.append("H")
			
		else:
			list.append("T")
			
	return list
	
	




if __name__ == "__main__":
	n = int(raw_input("How many times to flip the coin?"))
	pro = float(raw_input("Please put probibility of coin flip as a float(shever) smaller than 1"))
	k = flip4(n, pro)
	print k	