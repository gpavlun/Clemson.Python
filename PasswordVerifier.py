''' 
name:       Gregory Pavlunenko
user:       gpavlun
course:     ECE 2210
semester:   Fall 2024
project:    Password Verifier
purpose:    This code is designed to check if a
            persons password is going strong or
	    weak, based off presupposed rules.
assumpt:    
bugs:  
'''

# You CANNOT import other modules
import sys

redirectIOtoFile = True

if(redirectIOtoFile):
	# redirect stdin to a file
	sys.stdin = open('input', 'r')
	

############ Your input starts here. Do NOT change the above code!!! #################
def verify_password(pwd):
	for x in pwd:
		x=ord(x)
		if ((x<33 and x>=0) or x==127 or len(pwd)<12):	
			return(False)
	State=False
	for x in pwd:
		x=ord(x)
		if x<123 and x>96:	
			State=True
	if State==False:
		return(False)
	State=False
	for x in pwd:
		x=ord(x)
		if x<91 and x>64:	
			State=True
	if State==False:
		return(False)
	State=False
	for x in pwd:
		x=ord(x)
		if x<58 and x>47:
			State=True
	if State==False:
		return(False)
	State=False
	for x in pwd:
		x=ord(x)
		if (x<48 and x>32) or (x<65 and x>57) or (x<127 and x>122):
			State=True
	return(State)
################# Your input ends here. Do NOT change the following code!!! ######################
if __name__ == '__main__':
	while True:
		line = input()
		if line == 'End':
			break
		else:
			print(verify_password(line))

