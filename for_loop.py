# 1. Print numbers from 1 to 10 using for and range.

for i in range(1,11):
    print(i)

#-----------------------------------------------------------------------

# 2. Print numbers from 10 to 1 using for and range.

for i in range(10,0,-1):
    print(i)

#-------------------------------------------------------------------------

# 3. Print all even numbers from 1 to 50 using for and range.

for i in range(1,51):
    if i%2==0:
        print(i)

#-------------------------------------------------------------------------

# 4. Print all odd numbers from 1 to 50 using for and range.

for i in range(1,51):
    if i%2!=0:
        print(i)

#-------------------------------------------------------------------------

# 5. Print numbers from 0 to 100 with a step of 10.

for i in range(0,101,10):
    print(i)

#--------------------------------------------------------------------------

# 6. Print numbers from 5 to 50 with a step of 5.

for i in range(5,51,5):
    print(i)

#--------------------------------------------------------------------------

# 7. Print numbers from 100 to 0 with a step of -5.

for i in range(100,0,-5):
    print(i)

#----------------------------------------------------------------------------

# 8. Print the square of numbers from 1 to 10 using for and range.

for i in range(1,11):
    print(i*i)

#----------------------------------------------------------------------------

# 9. Print the cube of numbers from 1 to 5 using for and range.

for i in range(1,6):
    print(i*i*i)

#-----------------------------------------------------------------------------

# 10. Find the sum of numbers from 1 to 100 using for and range.
sum=0
for i in range(1,101):
    sum = sum+i
print(sum)

#-----------------------------------------------------------------------------

# 11. Find the sum of even numbers from 1 to 50 using for and range.

sum=0
for i in range(1,51):
    if i%2==0:
        sum+=i
print(sum)

#-------------------------------------------------------------------------------

# 12. Print the table of 7 using for and range.

for i in range(1,11):
    print(i*7)

#-------------------------------------------------------------------------------

# 13. Print numbers between 1 and 100 that are divisible by 4.

for i in range(1,101):
    if i%4==0:
        print(i)

#-------------------------------------------------------------------------------

# 14. Print numbers from 1 to 30 but skip multiples of 3.

for i in range(1,31):
    if i%3!=0:
        print(i)

#--------------------------------------------------------------------------------

# 15. Print numbers from 1 to 50 and stop when the number becomes 25.

for i in range(1,51):
    if i==25:
        break
    print(i)

#--------------------------------------------------------------------------------

# 16. Print numbers from 20 to 1 using for and range.

for i in range(20,0,-1):
    print(i)

#--------------------------------------------------------------------------------

# 17. Print all multiples of 6 between 1 and 100.

for i in range(1,101):
    if i%6==0:
        print(i)

#--------------------------------------------------------------------------------

# 18. Print numbers from 2 to 20 with a step of 2.

for i in range(2,21,2):
    print(i)

#--------------------------------------------------------------------------------

# 19. Print numbers from 1 to 100 in reverse order using range.

for i in range(100,0,-1):
    print(i)

#--------------------------------------------------------------------------------

# 20. Count how many numbers are there from 1 to 100 using for and range.

count=0
for i in range(1,101):
    count+=1
print(count)



