class one:
    one = 1
    two = 2
    oneA = 0
    oneB = 0

    def __init__(self,x,y):
        self.oneA = x
        self.oneB = y

    def second(self):
        print self.one + self.two + self.oneA + self.oneB


class two:
    one = 2
    two = 3

    def __init__(self,x,y):
        self.oneA = x
        self.oneB = y

    def second(self):
        print self.one + self.two + self.oneA + self.oneB

class three:
    one = 4
    two = 5

    def __init__(self,x,y):
        self.oneA = x
        self.oneB = y

    def second(self):
        print self.one + self.two + self.oneA + self.oneB
