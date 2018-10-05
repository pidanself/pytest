def createCounter():
    n=0
    def counter():
	    nonlocal n
	    n=n+1
	    return n
    return counter

counterB=createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')