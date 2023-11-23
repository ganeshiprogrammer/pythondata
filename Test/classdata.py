
class Test():



    def __init__(self):
        print("This is from constructor")

    def display(self,no1):
        print("This is from display function =",(no1))


class second(Test):

    def call(self):
        print("This is from call function")





s = second()
s.display(20)

#t = Test()
# t.display(20)