

class demoException:
    def __init__(self):
        print("construct get called")
    def __del__(self):
        print("destructor get called,it will delete object which is created by constructor")
    def funAccept(self):

        name=input("enter name")
        self.name=name
        
        try:
            age=int(input("please enter age"))
            if(age<18):
                self.age=age
                raise ValueError
            else:
                self.age=age
        except ValueError:
            print("age is less that 18")
    def funDisplay(self):
        print("You have enter name:",self.name)
        print("You have enterd age is :",self.age)

    def funDivByZero(self):
        
        try:
            a=int(input("Enter first number"))
            b=int(input("Enter second number"))
            c=a/b;
        except Exception as e:
            print(e)
        else:
            print("Dividion is ",c)
        finally:
            print("division of 2 number handle through exception")
           


def main():
    obj=demoException()
    obj.funAccept()
    obj.funDisplay();
    obj.funDivByZero();

main()