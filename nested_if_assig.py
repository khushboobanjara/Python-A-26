v# 1. Write a program using nested if to check whether a number is positive,
# negative, or zero, and if positive, also check whether it is even or odd.

num = int(input("enter a number "))
if num>0:
    if num %2 == 0:
        print(" its a even number ")
    else:
        print("its a odd number ")

elif num <0:
    print("its a negative number ")

else:
    print("its a zero")

# -----------------------------------------------------------------------------------


# 2. Write a program using nested if to find the greatest among three numbers.

a = int(input("enter first number "))
b = int(input("enter  second number "))
c = int(input("enter third number "))

if a>b:
    if a>c:
        print("a is max ")
    else:
        print("c is max ")
else:
    if b>c:
        print("b is max ")
    else:
        print("c is max ")

#--------------------------------------------------------------------------------

# 3. Write a program using nested if to check whether a student has passed or
# failed, and if passed, assign a grade based on marks.

marks = int(input("enter  a number "))

if marks > 45:
    if marks >70:
        print("A grade ")
    else:
        print("B grade ")
else:
    print("you are fail !")


# 4. Write a program using nested if to check whether a person is eligible to
# vote, and if eligible, check whether they are a first-time voter.

age = int(input("enter your age "))
first = True
if age>18:
    if first == True:
        print("you are first time voter ")
    else:
        print("you are not a first time voter ")
else:
    print("you are not eligible for vote ")

#-------------------------------------------------------------------------------------

# 5. Write a program using nested if to check whether a number is divisible by
#  5, and if yes, check whether it is also divisible by 10.

num = int(input("enter a number "))

if num%5==0:
    if marks%10==0:
        print("the number is divisible by both numbers ")
    else:
        print("the numer is divisible by 5 ")
else:
    print("the number is divisible by 10")

#---------------------------------------------------------------------------------------

# 6. Write a program using nested if to check whether a character is an
# alphabet, and if it is an alphabet, check whether it is a vowel or consonant.

ch = input("enter a number ")
charector = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'
if ch in charector:
    if ch in vowels:
        print("its a vowels ")
    else:
        print("its a conconents ")
else:
    print("its not a charector")

#--------------------------------------------------------------------------------------------

# 7. Write a program using nested if to check whether a person is eligible for a
# job based on age, and if eligible, check whether they have the required
# qualification.

age = int(input("enter your age"))
qualification = True
if age > 20:
    if qualification== True:
        print("you are eligible for job ")
    else:
        print("you have not qualified ")
else:
    print("you are not eligible for job ")


#-----------------------------------------------------------------------------------------------

# 8. Write a program using nested if to check whether a number is greater than
# 50, and if yes, check whether it is also greater than 100.

num = int(input("enter a number "))
if num>50:
    if num>100:
        print("the number is greater than 100")
    else:
        print("the number is grater than 50 but less than 100")
else:
    print("the number is less than 50 ")

#----------------------------------------------------------------------------------------------------

# 9. Write a program using if-elif-else to check whether a number is positive,
# negative, or zero.

num = int(input("enter a number "))
if num>0:
    print("the number is positive ")
elif num<0:
    print("the number is negative ")
else:
    print("the number is zero ")

#------------------------------------------------------------------------------------------------------

# 10. Write a program using elif to assign grades based on marks:
# A (90–100), B (80–89), C (70–79), D (60–69), F (below 60).

marks = int(input("enter your marks "))
if marks>90 and marks<100:
    print("A grade")
elif marks>90 and marks<80:
    print("B grade ")
elif marks>80 and marks<70:
    print("c grade ")
elif marks>70 and marks<60:
    print("D grade ")
else:
    print("fail!")

#------------------------------------------------------------------------------------------------------

# 11. Write a program using elif to check whether a given day number (1–7)
# corresponds to Monday–Sunday.

day = int(input("enter a day "))

if day == 1:
    print("monday")
elif day==2:
    print("tuesday")
elif day==3:
    print("wednesday")
elif day==4:
    print("thursday ")
elif day==5:
    print("friday")
elif day==6:
    print("saturday")
elif day == 7:
    print("sunday")
else:
    print("wrong input !")

#----------------------------------------------------------------------------------------------------

# 12. Write a program using elif to find the largest among three numbers.

a = int(input("enter a number "))
b = int(input("enter a number "))
c = int(input("enter a number "))

if a>b and a>c:
    print("a is greatest number ")
elif b>a and b>c:
    print("b is greatest number ")
else:
    print("c is greatest number ")

#-------------------------------------------------------------------------------------------------------

# 13. Write a program using elif to check whether a year is a leap year or not.

year = int(input("enter a number "))
if (year%400==0) or (year%4==0 and year%100!=0):
    print("leap year ")
else:
    print("not a leap year ")

#-------------------------------------------------------------------------------------------------------

# 14. Write a program using elif to classify a person’s age group: Child, Teen, Adult, or
# Senior.

age = int(input("enter your age "))

if age<=12:
    print("child")
elif age>12 and age< 19:
    print("teenager ")
elif age>19 and age<60:
    print("adult")
else:
    print("senior citizen")

#----------------------------------------------------------------------------------------------------------

# 15. Write a program using elif to check whether a character is a vowel, consonant,
# digit, or special character.

ch = input("enter a any charector or num ")
charector = 'abcdefghigklmnopqrstuvwxyz'
vowels = 'aeiou'
digits = '0123456789'
if ch in charector:    
    if ch in vowels:
        print("its a vowels")
    else:
        print("its a consonant ")
elif ch in digits:
    print("its a number ")
else:
    print("its a speacial charector ")

#-------------------------------------------------------------------------------------------------

# 16. Write a program using elif to build a simple calculator for +, -, *, and /.

a = float(input("enter  a number "))
b = float(input("enter  second number "))
operator =(input("enter  operator  "))

if operator == '+':
    print("addision =  ", a+b)
elif operator == '-':
    print("subtraction =  ", a-b)
elif operator == '*':
    print("multiplication =  ", a*b)
elif operator == '/':
    print("division =  ",a/b)
else:
    print("wrong operator ")

#----------------------------------------------------------------------------------------------------

# 17. Write a program using elif to check whether a number is divisible by 2, 3, 5, or
# none of them.

num = int(input("enter a number "))

if num %2==0:
    print("the number is divisible by 2 ")
elif num%3==0:
    print("the number is divisible by 3 ")
elif num%5 == 0:
    print("the number  is divisible by 5 ")
else:
    print("the number is not divisible by non of them")

#-------------------------------------------------------------------------------------------------------

# 18. Write a program using elif to convert a numeric month value (1–12) into the month
# name.

month = int(input("enter  a month "))

if month==1:
    print("january ")
elif month==1:
    print("fabruary")
elif month==3:
    print("march")
elif month==4:
    print("april")
elif month==5:
    print("may")
elif month==6:
    print("june")
elif month==7:
    print("july")
elif month==8:
    print("august")
elif month==9:
    print("september")
elif month==10:
    print("october")
elif month==11:
    print("november")
elif month==12:
    print("december ")
else:
    print("wrong input! ")

#---------------------------------------------------------------------------------------------

# 19. Write a program using elif to check the type of triangle: Equilateral, Isosceles, or
# Scalene

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

#--------------------------------------------------------------------------------------------------

# 20. Write a program using elif to determine the season based on month number.

month = int(input("enter month  "))

if month == 12 or month == 1 or month == 2:
    print("winter")
elif month == 3 or month == 4 or month == 5:
    print("spring")
elif month == 6 or month == 7 or month == 8:
    print("summer")
elif month == 9 or month == 10 or month == 11:
    print("autumn")
else:
    print("wronge input ")

#--------------------------------------------------------------------------------------------

# 21. Write a program using elif to calculate electricity bill based on unit ranges.

unit = int(input("enter  unit "))

if unit<=100:
    print("bill = ",unit*1.5)
elif unit<=200:
    print("bill= ",unit*2.5)
elif unit<=300:
    print("bill= ", unit*4)
else:
    print("bill= ", unit*6)

#-----------------------------------------------------------------------------------------------

# 22. Write a program using elif to check whether a number is one-digit, two-digit,
# three-digit, or more.

num = int(input("enter a number  "))

if num>0 and num<=9:
    print("one digit number ")
elif num>9 and num<=99:
    print("two digit number ")
elif num>99 and num<=999:
    print("three digit number ")
else:
    print("more than three digit number ")

#-------------------------------------------------------------------------------------------------

# 23. Write a program using elif to check the result of a student: Distinction, First
# Class, Second Class, Pass, or Fail.

marks = int(input("enter marks "))
if marks >=75:
    print("distinction ")
elif marks >=60:
    print("first class ")
elif marks >=50:
    print("second class ")
else:
    print("fail ")

#-------------------------------------------------------------------------------------------------

# 24. Write a program using elif to convert percentage into grade category.
 
per = int(input("enter percentage "))

if per>=90:
    print("A+")
elif per>=80:
    print("A")
elif per>=70:
    print("B+")
elif per>=60:
    print("B")
elif per>=50:
    print("C")
elif per>=40:
    print("D")
else:
    print("fail! ")

#-------------------------------------------------------------------------------------------------


# 25. Write a program using elif to check traffic light action based on color input.

color = input("enter light color ")

if color =='red':
    print("stop")
elif color =='yellow':
    print("slow down ")
elif color =='green':
    print("go") 
else:
    print("invalide color")

#-----------------------------------------------------------------------------------------------------

# 26. Write a program using elif to classify temperature as Cold, Moderate, or Hot.

temp = int(input("enter tempreture "))
if temp<=15:
    print("cold ")
elif temp>=15 and temp<=30:
    print("moderate")
else:
    print("hot")

#-----------------------------------------------------------------------------------------------------

# 27. Write a program using elif to check the type of input number: zero, positive even,
# positive odd, or negative.

num= int(input("enter a number "))
if num==0:
    print("its zero")
elif num>0 and num%2==0:
    print("positive even ")
elif num>0 and num%2!=0:
    print("positive odd")
else:
    print("negative ")


