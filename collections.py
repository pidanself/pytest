#学习collections这个模块

#namedtuple
from collections import namedtuple
#建立一个tuple来表达坐标系中的一个圆
circle=namedtuple('circle',['x','y','r'])
cir=circle(3,4,5)
print(cir.x,cir.y)
print('this circle (x,y) is (%s,%s)\nthis circle r is %s'%(cir.x,cir.y,cir.r))

#deque
from collections import deque
p=deque(['a','b','c','e'])
p.appendleft('y')
q=['a','b','c','e']
#q.appendleft('z') list没有这种操作
print(p)
print(q)

#defaultdict
from collections import defaultdict
dd=defaultdict(lambda:'0')
dd['a']=1
print(dd['a'])
print(dd['b'])

#OrderedDict
from collections import OrderedDict
d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
#会按照先后顺序展示，并且可以实现先进先出

#Counter记录一个字母出现的次数，
from collections import Counter
c=Counter()
print(c['w'])
for i in 'programming':
	c[i]=c[i]+1
print(c['m'])