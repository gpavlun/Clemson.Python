"""
name:       Gregory Pavlunenko
user:       gpavlun
course:     ECE2220
semester:   fall
project:    Alarm
purpose:    This code is designed to detect if 
	    an intruder is likely based off of 
            date from various packets
assumpt:    We are assuming that the inputs are	
            being accurately read and that a
            the conditons for a false alarm are
            correct and not coincidental.
bugs:  
"""

# You CANNOT import other modules
import sys

# Do NOT change the variable below.
redirectIOtoFile = True

"""
MAXSAMPLES and MINTHREASH are global variables.
In this project, both variables should be treated as a constant. 
This means you should NOT try to change them.
"""
MAXSAMPLES = 500
MINTHRESH = 3


def if_int(l):
	"""Returns True if l can be converted to an integer and False otherwise.
	Args:
		l (str): The return value of input()
	"""
	try: 
		l=int(l)
		return True
	except:
		return False

def process_one_sample_set(dict_threat_count, min_threat_level, false_alarm_count):
	""" Processes one sample set and prints the result.
	
	Args:
		dict_threat_count: Each key of dictionary dict_threat_count is a valid threat value, with the associated value 
							being the count of that threat in one sample set.
		min_threat_level: The user-defined min_threat_value.
		false_alarm_count: The user-defined false_alarm_count.
	"""
	key=[]
	value=[]
	for x in dict_threat_count:
		if int(x)>=min_threat_level and dict_threat_count[x]<=false_alarm_count:
			key.append(x)
			value.append(dict_threat_count[x])
	if key==[]:
		print('No threat detected')
	else:
		count=value.index(max(value))
		print('Threat detected with level',key[count],' and appears ',max(value),' times')
	






def process_sample_sets():
	"""First reads in the min_threat_level and false_alarm_count and then
	continuously processes sample sets one-by-one until a negative value other than -1 is read.

	Args: None
	"""
	min_threat_level = -12345	# This value is expected to change according to user's input
	false_alarm_count = -137153163	# This value is expected to change according to user's input
	
	# Each key of dictionary dict_threat_count is a valid threat value, with the associated value 
	# being the count of that threat in one sample set
	dict_threat_count = dict()	 

	# The following while-loop reads in the min_threat_level. 
	while True:
		min_threat_level=input()
		if if_int(min_threat_level)==True and int(min_threat_level)>=MINTHRESH:
			min_threat_level=int(min_threat_level)
			print('The minimun threat level is %d.' % min_threat_level)
			break
		elif min_threat_level=='-1':
			sys.exit()
		else:
			print('The minimum level is invalid. What is the minimum threat level?')

	# The following while-loop reads in the false_alarm_count. 
	while True:	
		false_alarm_count=input()
		if if_int(false_alarm_count)==True and int(false_alarm_count)>=0:
			false_alarm_count=int(false_alarm_count)
			print('A false alarm if the count is < %d.'%false_alarm_count)
			break
		elif false_alarm_count=='-1':
			sys.exit()
		else:
			print('The false alarm threshold is invalid. What is the false alarm threshold?')

	# The following while-loop continuously processes sample sets one-by-one until a negative value other than -1 is read.  		
	while True:	
		l = input()
		if not if_int(l):
			print('The threat is invalid. What is the threat?')
		elif int(l) == -1:
			process_one_sample_set(dict_threat_count, min_threat_level, false_alarm_count)
			dict_threat_count=dict()
		elif int(l) < -1:
			print('Goodbye')
			dict_threat_count=dict()
			sys.exit()
		else:
			con=0
			for x in dict_threat_count:
				if l==x:
					con=1
			if con==1:
				dict_threat_count[l]=dict_threat_count[l]+1
			else:
				dict_threat_count[l]=1


				
					
				
if __name__ == '__main__':
	""" Reads input from input file
	"""
	if(redirectIOtoFile):
		sys.stdin = open('input', 'r')
	process_sample_sets()
