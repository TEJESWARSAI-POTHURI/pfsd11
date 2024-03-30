

class BankAccount:
     accountNumber=int()
     name=str()
     balance=0
     def __init__(self,accountnumber,name,balance):
          self.accountNumber=accountnumber
          self.name=name
          self.balance=balance
     def deposits(self,a):
          self.balance+=a
     def withdrawal(self,a):
          if(a<=self.balance):
               self.balance -= a
          else:
               print("In-Sufficient Balance")
     def bankfees(self):
          self.balance=self.balance-(self.balance*0.05)
     def display(self):
          print("Account Number: ",self.accountNumber)
          print("Account Name: ",self.name)
          print("Balance: ",self.balance)

account1=BankAccount(1,'A Sai Sankar',100000)
account2=BankAccount(2,'A Eswar',10000)
account3=BankAccount(3,'P Tej Eswar',1000)
account1.display()
account2.display()
account3.display()
account1.deposits(5000)
account2.withdrawal(200)
account3.withdrawal(230)
account1.display()
account2.display()
account3.display()



'''2Q) 
class Student:
     student_id=int()
     student_name=str()
     student_class=int()
     def __init__(self,student_id,student_name):
          self.student_id=student_id
          self.student_name=student_name

     def display(self):
          print("Name: ",self.student_name)
          print("Id: ",self.student_id)

     
     def add(self,a):
          self.student_class=a

     def display(self):
          print("Name: ",self.student_name)
          print("Id: ",self.student_id)
          print("Class: ",self.student_class)


Student1=Student(1,"KLU")
Student1.add(10)
Student1.display()
del Student1.student_name
Student1.display()
'''

'''
1Q)
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

'''


