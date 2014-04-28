import random

def swap(first, second):
	return second, first

def main():
	'''Main class for the problem generator'''

	num_line = ''
	for i in xrange(31):
		num_line += str(i-10)+'  '

	# print num_line
	# print 
	# print 
	for i in xrange(25):
		first_num = random.randint(1, 10)
		second_num = random.randint(1, 10)
		third_num = random.randint(1, 10)
		fourth_num = random.randint(1, 10)
		sign = random.choice(['+', '-'])
		second_sign = random.choice(['+', '-'])		
		if third_num - fourth_num < 0:
			# print third_num, fourth_num
			third_num, fourth_num = swap(third_num, fourth_num)
			# print third_num, fourth_num

		if first_num - second_num < 0:
			first_num, second_num = swap(first_num, second_num)

		print 'Problem %2i: \t%2i %s %2i =\t\t\t\t Problem %2i: \t%2i %s %2i = ' % \
			(i+1, first_num, sign, second_num, (i+26), third_num, second_sign, fourth_num)
		


if __name__ == '__main__':
	main()