class Screen(object):
    @property
    def width(self):
        return self.__birth

    @width.setter
    def width(self,value):
        self.__width=value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,value):
        self.__height=value

    @property
    def resolution(self):
        self.__resolusion=self.__width*self.__height
        return self.__resolusion

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
