dic = {0:0, 1:1}

def main():
	n = int(input("Input a number"))
	## PSSST! If you use 45 for 'n' you get a real phone number!
	counter = Counter()
	x = fib(n,counter)
	print("Fibonacci'd with memoization I'd get",x)
	print("I had to count",counter,"times!")
	y = recursivefib(n, counter)
	print("And with recusion I still get",y)
	print("But the count changes to",counter)
	
def fib(n,counter):
	if n in dic:
		return dic[n]
	else:
		counter.increment()
		if n < 2:
			dic[n] = n
		else:
			dic[n] = fib(n-2,counter) + fib(n-1,counter)
			return dic[n]

def recursivefib(n, counter):
	if n < 2:
		return n
	else:
		counter.increment()
		return (recursivefib(n-2,counter) + recursivefib(n-1,counter))



class Counter(object):
	def __init__(self):
		self._number = 0
	def increment(self):
		self._number += 1
	def __str__(self):
		return str(self._number)
	
main()		
