"""#6. 
sec=float(input("Enter total seconds:- "))
min=int(sec//60)
sec=(sec%60)
print(min,"Minutes and",sec,"seconds")


#7. 
print("average speed of a car",(120/3),"Km/hour")

#8.
num1=int(input("Enter 1st number:- "))
num2=int(input("Enter 2nd number:- "))
if num1%num2==0:
    print(num1,"is a multiple of",num2)
else:
    print(num1,"is not a multiple of",num2)

#9.
pri=float(input("principle amount"))
int=float(input("rate of interest"))
time=float(input("time period in years"))
print("$",(pri*int*time)/100)


num1=float(input("1st one"))
num2=float(input("2nd one"))
if num1==num2:
    print("both are equals")
elif num1>num2:
    print(num1, "is greater")
else:
    print(num2, "is greater")

a=10
b=8
c=11
if a>b and a>c:
    print(a, "is gratest")
elif b>a and b>c:
    print(b,"is gratest")
else:
    print(c, "is gratest")

marks=float(input("Enter marks:- "))
if marks>=40:
    print("Pass")
else:
    print("fail")



age=int(input("Enter age:- "))
if age>=18:
    print("Eligible")
else:
    print("Not Eligible")


    
num1=int(input("Enter number:- "))
if num1%2==0:
    print("Even")
else:
    print("odd")

    

word1=(input("Enter 1st word:- "))
word2=(input("Enter 2nd word:- "))
if word1==word2:
    print("same")
else:
    print("not same ")


  
num1=int(input("Enter 1st person salery:- "))
num2=int(input("Enter 2nd person salery:- "))
if num1>num2:
    print("Employee A Earns more")
else:
    print("Employee B Earns more")



num=float(input("Enter your number:- "))
if 10<num>50:
    print("LIES BTW 10 AND 50")
else:
    print("Not lies btw 10 and 50")


year=int(input("Enter YOUR YEAR:- "))
if ((year%400==0) or (year%4 and year%100!=0)):
    print("Its a Leap year") 
else:
    print("not a leap Year")5

    """
    
