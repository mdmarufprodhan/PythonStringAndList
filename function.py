
#Create function

def sayHello():
  print('Hello world')

sayHello()

#Return value

def getSum(num1, num2):
    total = num1+num2
    return total
numSum = getSum(5,6)
print(numSum)

def addOneToNum(num):
    num += 1
    return num
num = 4
new_num = addOneToNum(num)
print(new_num)

#Lamda function
getSum = lambda num1, num2 : num1 + num2
print(getSum(9,2))

addOneToNum = lambda num: num + 1
print(addOneToNum(5))
