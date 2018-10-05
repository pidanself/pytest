#得到素数
def odd():
    n=1
    while True:
	    n=n+2
	    yield n
		
def not_divisible(n):
	return lambda x:x%n>0
	
def primes():
	yield 2
	it=odd()
	while True:
		n=next(it)
		yield n 
		it=filter(not_divisible,it)
		
for n in primes():
	if n <1000:
		print(n)
	else:
		break
		