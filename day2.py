"""
#1.
num=int(input("Enter a number"))
if num<0:
    print("Negative")
elif num==0:
    print("Zero")
else:
    print("positive")

#2. 
num=int(input("Enter a number"))
if 76<num>=90:
    print("A")
elif 51<num>=75:
    print("B")
elif 49.9<num>=50:
    print("C")
else:
    print("Fail")
    
   

#3.
num=(input("Enter a number"))
len=len(num)
if len==1:
    print("Singke Digit")
elif(len==2:):
    print("Double Digit")
else:
    print("More than 2 digits")


#4
num=int(input("Enter a number btw 1-7"))
if num==1:
    print("Monday")
elif num==2:
    print("Tuesday")
elif num==3:
    print("Wednesday")
elif num==4:
    print("Thrusday")
elif num==5:
    print("Friday")
elif num==6:
    print("Saturday")
elif num==7:
    print("Sunday")
else:
    print("number is not btw 1-7")

     

#5 
tem=float(input("Enter temperature in celcius"))
if tem<0:
    print("Freezing")
elif 0<=tem<21:
    print("Cold")
elif 21<=tem<=35:
    print("Warm")
else:
    print("Hot")



#6.
num=int(input("Enter a number"))
if num>0 and num%2==0:
    print("Positive annd Even")
if num>0 and num%2!=0:
    print("Positive annd Odd")
else:
    print("Negative")

   
    
pswrd=input("Enter a Your Passward")
paswrd="KOE"
if pswrd==paswrd:
    print("Access Granted")
else:
    print("Access Denied")


     

    i=0
for i in range(1,11):
    print(i)

    
 

i=0
sum=0
while i<=10:
    sum+=i
    i+=1 
print("Sum of First 10 nautral",sum) 

num=int(input("Enter a number"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)

    
       


num=int(input("Enter a number"))
i=num
fact=1
while(i!=1):
    fact*=i
    i-=1
print("Factprial = ", fact)



# reverse of a number

num=int(input("Enter a number"))
n1=0
while num>0:
    rem=num%10
    n1=n1*10+rem
    num=num//10
print(n1)



"""
