# Q1

print("------------------------++++++---------------------------")
array = 'Python is a case sensitive language'
print(len(array))
reversed = array[::-1]
print(reversed)
a = array.replace("a case sensitive", "")
print(a)
b = array.replace("a case sensitive", "object oriented")
print(b)
c = array.find('a')
print(c)
d = array.replace(" ", "")
print(d)
print("\n")
print("------------------------++++++---------------------------")


# Q2


name = input("Your name\n")
SID = int(input("Your SID\n"))
name2 = input("Your department\n")
CGPA = float(input("Your CGPA \n"))
print("\nHey,%s Here!" % (name))
print("My SID is %d " % (SID))
print("I am from %s department and my CGPA is %f \n\n" % (name2, CGPA))
print("------------------------++++++---------------------------")

# Q3


a = 56
b = 10
c = a & b
print(c)
d = a | b
print(d)
e = a ^ b
print(e)
f = a << 2
g = b << 2
print(f, g)
h = a >> 2
i = b >> 4
print(h, i)
print("\n")
print("------------------------++++++---------------------------")

# Q4


num01 = int(input("Enter first  your number\n"))
num02 = int(input("Enter second your number\n"))
num03 = int(input("Enter third  your number\n"))
print("Highest number is : %d\n\n" % (max(num01, num02, num03)))
print("\n")
print("------------------------++++++---------------------------")
# Q5

arr = ['kanish', 'name', 'ishita', 'loveneet', 'anish', 'tanish']
if 'name' in arr:
    print("Yes")
else:
    print("No")
print("\n")
print("------------------------++++++---------------------------")
# Q6
print("We using this formula (a + b >=c)  so please enter in this order\n")
num1 = float(input("Enter Value of a : \n"))
num2 = float(input("Enter Value of b : \n"))
num3 = float(input("Enter Value of c : \n"))
if ((num1 + num2) >= num3):
    print("Yes,This form triangle")
else:
    print("No,This not form triangle")
print("\n")
print("------------------------++++++---------------------------")
