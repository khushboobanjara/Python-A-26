# 1 Create a list of 5 integers and print it.

li = [1,7,8,9,5]
print(li)

# 2 Create a list of 3 different data types and print each element.

li = ['khushi',75.89,5]
print(li)

# 3 How do you check the length of a list? Write a small example.
li=[15,3,9,45,78,1]
print(len(li))

# 4 Create an empty list and add three elements to it.
li=[]
li.extend([2,8,56,0])
print(li)

# 5. Create a list of 6 numbers and print the first element.
li=['mona',45,6,3,78,79,3]
print(li[0])

# 6 Print the last element of a list using negative indexing.
li=[45,9,62,7,47]
print(li[-1])

# 7. Given a list, print the third element.
li = [4,6,8,9,0]
print(li[2])

# 8 Extract the first three elements using slicing.
li = [55,6,8,96,5,3]
print(li[3:])

# 9 Reverse a list using slicing.
li=[55,6,8,96,5,3]
print(li[-1:0:-1])

# 10 Create a list and change the second element to a new value.
li=[55,6,8,96,5,3]
li[1]=4
print(li)

# 11 Replace the last element of a list with 100.
li=[5,24,13,10,26]
li[-1]=100
print(li)

# 12 Modify multiple elements in a list using slicing.
li=[5,24,13,10,26]
li[3]=100
li[0]=25
li[1]=50
print(li)

# 13 Create a list and use append() to add one element.
li=[5,24,13,10,26]
li.append(100)
print(li)

# 14. Use extend() to add multiple elements to a list.
li=[5,24,13,10,26]
li.extend([100,6,9])
print(li)

# 15 Use insert() to add an element at index position 2
li=[6,5,7,9,0]
li.insert(1,911)
print(li)

# 16 What is the difference between append() and extend()?

# append() fuction is used to add only one new element at the end of the list
# extend() functions is used to add multiple elements at the end of the list

# 17 Remove an element using remove().
li=[6,5,7,9,0]
li.remove(6)
print(li)

# 18 Remove an element using pop() and print the removed value.
li = [6,5,7,9,0]
print(li[1])
li.pop(1)
print(li)

# 19 Clear all elements from a list.
li = [6,5,7,9,0]
li.clear()
print(li)

# 20 Print all elements of a list using a for loop.
li = [6,5,7,9,0]
for i in range(len(li)):
    print(li[i])

# 21 Print only even numbers from a list using a loop.
li = [6,5,7,9,0]
even=[]
for i in range(len(li)):
    if li[i]%2==0:
        even.append(li[i])
print(even)

# 22 Count how many numbers are greater than 10 using a loop.
li=[20,56,0,5,3]
count=0
for i in range(len(li)):
    if li[i]>10:
        count+=1
print(count)

# 23 Find the sum of all elements in a list using a loop.
li=[20,56,0,5,3]
sum=0
for i in range(len(li)):
    sum+=li[i]
print(sum) 

# 24 Find the maximum element in a list without using max().
li=[20,56,0,5,3]
max=0
for i in range(len(li)):
    if li[i]>max:
        max=li[i]
print(max)
