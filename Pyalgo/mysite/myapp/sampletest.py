'''App Accademy Coding Challenge'''
#PYTHON 2.7


# 1. crazy_sum
'''Write a method named crazy_sum(numbers) that takes an array of numbers.
 crazy_sum should multiply each number in the array by its position in the array, and return the sum.'''


def crazy_sum(numbers):
	return sum([x*numbers[x] for x in xrange(len(numbers))])


#print crazy_sum([2]) 
#print crazy_sum([2, 3])
#print crazy_sum([2, 3, 5]) 
#print crazy_sum([2, 3, 5, 2]) 

#square_nums
'''Write a method square_nums that takes a number max and returns
 the number of perfect squares less than max.'''

def square_nums(max):
	squares = 0
	for x in xrange(1, max):
		if (x ** (0.5)) % 1 == 0:
			squares +=1
	return squares
#print square_nums(5) 
#print square_nums(10)
#print square_nums(25)

#crazy_nums
'''Write a method crazy_nums that takes a number, max, and returns an array of the integers that

are less than max
are divisible by either three or five
are not divisible by both three and five
You may wish to use the modulo operation: 5 % 2 returns the remainder when dividing 5 by 2: 1. If num is divisible by i, then num % i == 0.
'''

def crazy_nums(max):

	lista = filter(lambda x: x%3 == 0 or x%5 ==0, [x for x in xrange(1, max)])
	listb = filter(lambda x: x%3 ==0 and x%5 == 0, lista)
	listc = [x for x in lista if x not in listb]
	return listc


#print crazy_nums(3) 
#print crazy_nums(10)
#print crazy_nums(20)