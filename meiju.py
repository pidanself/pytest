from enum import Enum,unique

# Month=Enum('Month',('Jan','Feb','Mar'))
# for name,member in Month.__members__.items():
	# print(name,'=>','member',',',member.value)
	
# @unique
# class Weekday(Enum):
	# Sun=0
	# Mon=1
	# Tue=2
	# Wed=3
	# Thu=4
	# Fri=5
	# Sat=6

# print(Weekday(1))
# print(Weekday.Tue.value)

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name,gender):
        self.name = name
        self.gender = gender
		
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')