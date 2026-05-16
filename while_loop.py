# 1. Write a program using a while loop to print all digits of a number one by one.

num = int(input("enter a  number "))
while(num!=0):
    n = num%10
    print(n)
    num//=10 

#----------------------------------------------------------------------------

# 2. Write a program to find the sum of digits of a number using a while loop.

num = int(input("enter  a number "))
sum = 0
while(num!=0):
    n = num%10
    sum+=n
    num//=10
print(sum)

#-----------------------------------------------------------------------------

# 3. Write a program to count how many digits are in a given number using a while loop.

num = int(input("enter a number "))
count=0
while(num!=0):
    num//=10
    count+=1
print(count)

#------------------------------------------------------------------------------

# 4. Write a program to reverse a number using a while loop.

num = int(input("enter a number "))
rev = 0
while(num>0):
    n = num%10
    rev = rev*10+n
    num//=10
print(rev)

#------------------------------------------------------------------------------

# 5. Write a program to check whether a number is a palindrome using a while loop.

num = int(input("enter a number "))
new = num
rev = 0
while(num>0):
    n = num%10
    rev = rev*10+n
    num//=10
if rev == new:
    print("palindrome ")
else:
    print("not palindrome ")

# 6. Write a program to find the product of digits of a number using a while loop.


num = int(input("enter  a number "))
product = 1
while(num!=0):
    n = num%10
    product*=n
    num//=10
print(product)

#------------------------------------------------------------------------------

# 7. Write a program to find the largest digit in a number using a while loop.

num = int(input("enter a number "))
largest =0
while(num!=0):
    n = num%10
    if n> largest:
        largest = n
    num//=10
print(largest)

#-----------------------------------------------------------------------------

# 8. Write a program to find the smallest digit in a number using a while loop.

num = int(input("enter  a number "))
smallest = 9
while(num>0):
    n = num%10
    if n < smallest:
        smallest = n
    num//=10
print(smallest)

#-----------------------------------------------------------

# 9. Write a program to check whether a number is an Armstrong number using a while loop.

num = int(input("enter  a number "))
new = num
count=0
while(num>0):
    count+=1
    num//=10
sum = 0
num=new
while(num>0):
    n = num%10
    sum=sum+n**count
    num//=10
if new == sum:
    print("armsrong number ")
else:
    print("not a armsrong number ")



#-----------------------------------------------------------

# 10. Write a program to remove all zeros from a number using a while loop.

num = int(input("enter a number "))
new = 0
place = 1
while(num!=0):
    n = num%10
    if n!=0:
        new = new+n*place
        place*=10
    num//=10    
print(new)
    

#-----------------------------------------------------------------------

# 11. Write a program to count how many even and odd digits are present in a number using a
# while loop.

num = int(input("enter a number "))
while(num>0):
    n = num%10
    if n%2==0:
        print(f"even number = {n}")
    else:
        print(f"odd number = {n}")
    num//=10

#------------------------------------------------------------------------

# 12. Write a program to check whether a number contains a specific digit (for example, 5)
# using a while loop.

num = int(input("enter a number "))
num1 = int(input("enter a specific number  "))
found = False
while(num>0):
    n = num%10
    if n == num1:
       found = True
    num//=10
if found:
    print("found")
else:
    print("not found")

#------------------------------------------------------------------------

# 13. Write a program to calculate the sum of even digits and sum of odd digits separately
# using a while loop.


num = int(input("enter a number "))
sum = 0
add = 0
while(num>0):
    n = num%10
    if n%2==0:
        sum+=n
    else:
        add+=n
    num//=10
print(f"sum of even number is {sum},sum of odd number is {add}")

#----------------------------------------------------------------------

# 14. Write a program to create a new number by squaring each digit of a given number using
# a while loop.

num = int(input("enter a number "))
while(num>0):
    n = num%10
    s = n*n
    print(s) 
    num//=10

# 15. Write a program to check whether a number is a perfect number using a while loop.

num = int(input("enter a number "))
new = num
i = 1
sum =0
while(i<num):
    if num%i==0:
        sum = sum+i
        # print(i)
    i+=1
# print(sum)

if sum == new:
    print("its a perfect number ")
else:
    print("not a perfect number ")

# 16. Write a program to print the Fibonacci series up to N terms using a while loop.

num = int(input("enter a number "))
a = 0
b = 1
print(a)
print(b)
i = 1
while(i<=num):
    next = a+b
    a = b
    b = next
    print(next)
    i+=1

#--------------------------------------------------------------------------

# 17. Write a program to find the factorial of a number using a while loop.

num = int(input("enter a number "))
i = 1
fact = 1
while(i<=num):
    fact*=i
    i+=1
print(fact)

#--------------------------------------------------------------------------

# 18. Write a program to calculate the power of a number (a^b) using a while loop.

num = int(input("enter a number "))
power = int(input("enter a power "))
result = 1
while(power>0):
    result*=num
    power-=1
print(result)

#--------------------------------------------------------------------------

# 19. Write a program to find the GCD of two numbers using a while loop.

# num = int(input("enter a number "))
# num2 = int(input("enter a number "))


i = 2
count=1
while(num>=i and num2>=i):
    if num%i==0 and num2%i==0:
        count*=i
        num=num//i
        num2=num2//i
    else: 
        i+=1
print(count)

# 20. Write a program to check whether a number is prime using a while loop.

num = int(input("enter a number "))
i = 1
factor = 0
while(i<=num):
    if num%i==0:
        factor+=1
    i+=1
if factor==2:
    print("prime number ")
else:
    print("not a prime number ")

    