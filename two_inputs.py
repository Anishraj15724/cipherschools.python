# name = input("enter your name: ")
# age = input("enter your age: ")
#name, age= input("enter your name and age ").split(",")
#print(name)
#print(age)
# ask user to input 3 number and you have to print average of three number 
#  using string formatting.
                                        # >>>>>>>>>>>>>>>average<<<<<<<<<<


num1,num2,num3 = input("enter the three number commas seprated ").split(",")
print(f"average of three number: {(int(num1)+ int(num2) + int(num3)) / 3}" )