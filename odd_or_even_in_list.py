print("enter the limit")
lim=int(input())
print("enter the number")  
num=[]
for i in range (10):
    num2=int(input())
    num.append (num2)

eve=[]
odd=[]
for i in range (10):
    if i%2 ==0:
        eve.append(i)
    else:
        odd.append(i)

print ("even number is")
print (eve)
print ("odd number is")
print (odd)
