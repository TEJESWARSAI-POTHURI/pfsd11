class Parent:
    def function1(self):
        print("This is function One")

class Child(Parent):
    def function2(self,a):
        print("This is function Two")
        print(a)

b=20

y=Child()
y.function1()
y.function2(10)
print(y,b)
