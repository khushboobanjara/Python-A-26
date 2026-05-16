# 1. Write a Python program that takes an integer as input and checks whether the
# number is greater than zero, even, and divisible by 3. Print an appropriate
# message depending on whether all conditions are satisfied.

n = int(input("enter a number  "))

if n > 0 and n % 2 == 0 and n % 3 == 0:
    print("number is greater than zero, even, and divisible by 3")
else:
    print("conditions not satisfied")

#----------------------------------------------------------

# 2. Write a Python program that takes a number as input and checks whether it lies
# outside the range 10 to 50 (that is, less than 10 or greater than 50).

num = float(input("Enter a number: "))

if num < 10 or num > 50:
    print("number lies outside the range 10 to 50")
else:
    print("number lies inside the range 10 to 50")

#----------------------------------------------------------

# 3. Write a Python program that accepts a person’s age and checks whether the
# person is eligible to vote (age ≥ 18) and not a senior citizen (age < 60).

age = int(input("enter age  "))

if age >= 18 and age < 60:
    print("eligible to vote and not a senior citizen.")
else:
    print("not eligible under given conditions.")

#-----------------------------------------------------------

# 4. Write a Python program that accepts a year as input and checks whether it is a
# valid leap year using all leap year rules (divisible by 4, not divisible by 100 unless
# divisible by 400).

year = int(input("enter year "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")

#---------------------------------------------------------


# 5. Write a Python program that accepts a single character and checks whether it is an
# alphabet and also a vowel.

ch = input("enter a character ")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'
if ch in alphabet:
    if ch in vowels:
        print("its a alphabet and also vowel ")
else:
    print("its a alphabet but not a vowel")

#---------------------------------------------------------

# 6. Write a Python program that checks whether a number is divisible by 4 or divisible
# by 6, but not divisible by both at the same time.   

num = int(input("Enter a number: "))
if (num % 4 == 0 and num % 6 != 0):
    print("The number is divisible by 4 but not by 6.")
elif (num % 6 == 0 and num % 4 != 0):
    print("The number is divisible by 6 but not by 4.")
else:
    print(" does not satisfy the condition.")

#--------------------------------------------------------

# 7. Write a Python program that accepts marks of three subjects and checks whether
# the student has passed in all subjects, assuming the pass mark is 40 in each
# subject.

marks1 = int(input("enter marks1 "))
marks2 = int(input("enter marks2 "))
marks3 = int(input("enter marks3  "))

if marks1 >= 40 and marks2 >= 40 and marks3 >= 40:
    print("passed in all subjects")
else:
    print("failed") 

#---------------------------------------------------------

# 8. Write a Python program that checks whether a number lies between 100 and 999
# (inclusive) and is also an even number.

num = int(input("enter number "))

if 100 <= num <= 999 and num % 2 == 0:
    print("3-digit even number")
else:
    print("Not a 3-digit even number")

#--------------------------------------------------------

# 9. Write a Python program that checks whether a given temperature lies within a
# comfortable range, where both lower and upper limits are predefined.

temp = float(input("Enter temperature: "))

low = 18
high = 28

if low <= temp <= high:
    print("Comfortable temperature")
else:
    print("Not comfortable")

#---------------------------------------------------------

# 10. Write a Python program that checks whether a given character is neither a digit
# nor a special character, meaning it must be an alphabet.

ch = input("enter any charector ")
charector = 'abcdefghijklmnopqrstuvwxyz'

if ch in charector:
    print("its a charector ")
elif ch>0 and ch<9:
    print("its a digit ")
else:
    print("speacial charector ")

#---------------------------------------------------------

# 11. Write a Python program that checks whether a given temperature lies within a
# comfortable range, where both lower and upper limits are predefined.

temp = int(input("enter temprature "))

if temp> 18 and temp<25:
    print("comfortable range ")

else:
    print("temprature is not comfortable ")

#---------------------------------------------------------

# 12. Write a Python program that checks whether a number is divisible by 2, 3, or 5,
# and prints exactly which condition(s) the number satisfies.

n = int(input("enter number"))
if(n%2==0 and n%3==0 and n%5==0):
    print("satisfies")
else:
    print("not satisfied") 

#---------------------------------------------------------

# 13. Write a Python program that checks whether a person is eligible for a loan, based
# on conditions such as minimum age and minimum monthly income.

age = int(input("enter your age "))
income = int(input("enter your mounthly income "))

if age>20:
    if income>30000:
        print("you are eligible for loan ")
    else:
        print("you are not able to take loan ")
else:
    print("you are not eligible for loan ")

#------------------------------------------------------------


# 14. Write a Python program that checks whether a string is not empty and also has a
# length greater than 8 characters.

st = input("enter a string ")
if st and len(st)>8:
    print("valide string ")
else:
    print("not a valide string ")

#-----------------------------------------------------------

# 15 .Write a Python program that accepts three sides of a triangle and checks whether
# the triangle is a right-angled triangle.

side1 = int(input("enter side1 = "))
side2 = int(input("enter side2 = "))
side3 = int(input("enter side3 = "))
if(side1*side1+side2*side2==side3*side3):
    print("right angle triangle")
elif(side2*side2+side3*side3==side1*side1):
    print("right angle traingle ") 
elif(side3*side3+side2*side2==side1*side1):
    print("right angle traingle")
else:
    print("not a right angle traingle")  

#-----------------------------------------------------------

#  16. Write a Python program that accepts a student’s percentage and classifies the
# performance as excellent, very good, good, average, or poor.

percentage = int(input("enter percentage = "))
if(percentage<0 or percentage>100):
    print("invalid percentage")
elif(percentage>=90):
    print("excellent")
elif(percentage>=75):
    print("very good")
elif(percentage>=65):
    print("good") 
elif(percentage>=50):
    print("average")
else:
    print("poor")      

#----------------------------------------------------------

# 17. Write a Python program that takes a number and determines whether it is positive
# even, positive odd, negative even, negative odd, or zero.

n = int(input("enter number"))
if(n>=0):
    if(n>0):
        if(n%2==0):
            print("possitive even")
        else:
            print("possitive odd")
    else:
        print("zero")
else:
    if(n<=0):
        if(n%2==0):
            print("negative even")
        else:
            print("negative odd")
    else:
        print("zero")   

#-----------------------------------------------------------

# 18. Write a Python program that calculates an electricity bill using slab-wise unit
# charges and prints the total bill amount.

unit = float(input("enter the electricity unit "))

if unit>0 and unit<100:
    print(f"total electricity bill is {unit*1.5}")
elif unit>100 and unit<200:
    print(f"total electricity bill is {unit*2.5}")
else:
    print(f"total electricity bill is {unit*4}")

#------------------------------------------------------------

# 19. Write a Python program that determines the tax slab of a person based on their
# annual income.

income = int(input("enter your income "))

if income<=250000:
    print("no tax slad ")
elif income <=500000:
    print("5% tax slad")
elif income<=1000000:
    print("20% tax slad")
else:
    print("30% tax slade")

#-------------------------------------------------------------

# 20.Write a Python program that accepts a day number (1–7) and determines whether it
# is a weekday or weekend.

day = int(input("enter a day"))
if day>=1 and day<=5:
    print("weekday")
elif day==6 or day ==7:
    print("weekend")

#-------------------------------------------------------------

# 21. Write a Python program that checks a user’s internet data usage and categorizes it
# as low usage, medium usage, or high usage.

GB = int(input("enter data useges "))

if GB>0 and GB<5:
    print("low useges ")
elif GB >5 and GB<15:
    print("medium useges ")
else:
    print("high useges ")

#------------------------------------------------------------

# 22.Write a Python program that calculates the final payable amount after applying
# different discount slabs based on the purchase amount.

ammount = float(input("enter your purchase amount "))

if ammount>0 and ammount<1000:
    print("do not apply any dicount")
elif ammount>1000 and ammount<5000:
   discount = ammount*0.05
elif ammount>5000 and ammount<10000:
    discount = ammount*0.10
else:
    discount = ammount*0.15

total_ammount = ammount-discount
print(total_ammount)

#--------------------------------------------------------------


# 23.Write a Python program that accepts a month number and prints the
# corresponding season (summer, rainy, or winter).

month = int(input("enter month  "))

if month == 12 or month == 11 or month == 1 or month==2:
    print("winter")
elif month == 3 or month == 4 or month == 5 or month==6:
    print("summer")
elif month == 7 or month == 8 or month == 9 or month==10:
    print("rainy")
else:
    print("wronge input ")

#---------------------------------------------------------------

# 24. Write a Python program that determines a student’s exam result category,
# considering pass marks and a small grace-marks rule.

marks = int(input("enter a number "))

if marks>=45 and marks>=100:
    print("pass")
elif marks>=35 and marks<45:
    print("pass with grace")
else:
    print("fail!")

#---------------------------------------------------------


# 25.Write a Python program that simulates a login system, first checking whether the
# username exists and then checking whether the password is correct.

username = 'khushi'
password = 'khushi123'

name = input("enter username ")
passw = input("enter password ")

if name==username:
    if passw==password:
        print("succesfully login ")
    else:
        print("incorrect password")
else:
    print("username not available")

#-------------------------------------------------

# 26. Write a Python program that simulates an ATM withdrawal system, where the
# program checks account balance, minimum balance requirement, and withdrawal
# amount.


marks = float(input("enter academic marks "))
test_score = float(input("enter entrance test score "))


if marks >= 60 and test_score >= 50:
    print("Eligible for admission")
else:
    print("Not eligible for admission")

#----------------------------------------------------------

# 27.Write a Python program that checks whether a student qualifies for a scholarship,
# considering marks, family income, and category.

marks = int(input("enter your marks "))
income = int(input("enter your family income "))

if marks>=75:
    if income<=300000:
        print("eligible for scholarship ")
    else:
        print("you are not eligible")
else:
    print("you are not eligible ")

#---------------------------------------------------------

# 28. Write a Python program that determines whether an employee is eligible for a
# bonus, based on performance rating and years of service.

performence_rating = int(input("enter a number "))
experiance = int(input("enter experiace of year "))

if performence_rating>=4 and experiance>=3:
    print("eligible for bonus")
else:
    print("not eligible for bonus")

#----------------------------------------------------------

# 29.Write a Python program that validates a mobile number, checking its length and
# starting digit.

mobile_num = input("enter mobile number ")

if len(mobile_num)==10 and mobile_num[0] in ['6','7','8','9']:
    print("valide phone number ")
else:
    print("not a valide phone number  ")

#----------------------------------------------------

# 30. Write a Python program that determines whether a vehicle is allowed on the road,
# based on fuel type and government rules.

# Input details
fuel_type = input("Enter fuel type  ").lower()
vehicle_age = int(input("Enter vehicle age (year) "))


if fuel_type == "petrol":
    if vehicle_age <= 15:
        print("vehicle is allowed on the road")
    else:
        print("vehicle is not allowed on the road")

elif fuel_type == "diesel":
    if vehicle_age <= 10:
        print("vehicle is allowed on the road")
    else:
        print("vehicle is not allowed on the road")

elif fuel_type == "electric":
    print("vehicle is allowed on the road")

else:
    print("invalid fuel type")
