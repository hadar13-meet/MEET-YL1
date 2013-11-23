def pali(jessica):
	if jessica == jessica[::-1]:
		return True
	else:
		return False

if __name__=="__main__":
	text= raw_input("Please write something ")
	print pali(text)

#Tal changed the names here to explain something.

	
