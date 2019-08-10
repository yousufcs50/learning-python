def sayhi (name):
    #indent is important
    name1= input ("Enter your name:")
    print("hello "+name1+"!")
    print("you are "+ name)

print("Before")
sayhi("Mohammad")
print("After")
sayhi("Yousuf")
"""calling a function
def sayhi (name, age):
multiple strings
"""
def add_num(num1 ,num2):
    num1= input("Enter num1: ")
    num2 =input ("Enter num2: ")
    total =0
    total = int(num1) +int (num2)
    print(total)

add_num(2,3)
