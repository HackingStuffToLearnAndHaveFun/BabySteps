a = int(input("give me a number"))
b = int(input("and another one"))
while a > b :
    b = int(input("give another number bigger this time"))
sum = 0
z = a
while z <= b :
    sum = sum + z
    z = z +1
print (sum)

