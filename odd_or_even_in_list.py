print("enter the lim")
limit=int(input())
print("enter the num")  
num=[]
for i in range (limit):
    num2=int(input())
    num.append (num2)

even=[]
odd=[]
for i in range (10):
    if i%2 ==0:
        even.append(i)
    else:
        odd.append(i)

print ("even number is")
print (even)
print ("odd number is")
print (odd)
