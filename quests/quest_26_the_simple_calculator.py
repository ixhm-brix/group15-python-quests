def add (a,b) :
    return a+b
def sub (a,b):
    return a-b
def mult (a , b):
    return a*b
def div (a,b) :
    if b == 0 :
        return ("mathematical error")
    return a/b
num1 = int(input("Enter the first number:  "))
num2 = int(input("Enter the second number: "))
po  = input("Enter the operator like +,-,/ : ")
if po == "+" :
    result= add(num1,num2)
elif po == "-" :
    result= sub(num1,num2)
elif po == "/" :
    result= div(num1,num2)
else :
    result= "wrong operator" 
print(result)
