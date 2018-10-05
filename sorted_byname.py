#按名字进行排序
def by_name(t):
	return t[0]
	
#按成绩进行排序
def by_grades(t):
	return t[1]
	
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
print(L2)
L3=sorted(L,key=by_grades,reverse=True)
print(L3)