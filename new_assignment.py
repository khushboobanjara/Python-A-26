# Sum of list elements

li = [2,7,9,6,3,1]
sum = 0
for i in li:
    sum+=i
print("sum of list elements is: ", sum)


# Find the largest element in a list

li = [55,78,9,5,3,55]

largest_number = 0
for i in li:
    if i>largest_number:
        largest_number = i
print("largest number in list " ,largest_number)

# Count even numbers in a list

li = [1,2,3,4,6,7,4,2,4]
even_counter = 0
for i in li:
    if i%2==0:
        even_counter+=1
print("total even number in list ",even_counter)

# Reverse a list using a loop

li = [0,192,43,94,5]
new_li = []
for i in range(len(li)-1,-1,-1):
    new_li.append(li[i])
print(new_li)

# Find the second largest element

li=[1,2,3,4,5,6,6,7]
first_largest=0
second_largest=0
for i in range(len(li)):
     if li[i]>first_largest: 
          second_largest = first_largest
          first_largest = li[i]
     elif li[i]>second_largest and li[i]!=first_largest:
          second_largest=li[i]
print("second largest", second_largest)
print("first largest", first_largest)


# Remove duplicates from a list

li = [1,1,4,4,7,6,3,2,2,5,4,6]
new_li = []
for i in li:
    if i not in new_li:
        new_li.append(i)
print(new_li)

# Find all elements greater than the average

# Rotate a list to the left by k positions


li = [10,20,30,40,50]
k=2
for j in range(k):
       
    first = li[0]

    for i in range(len(li)-1):
        li[i] =li[i+1]

    li[len(li)-1] = first

print("after rotation",li)


# Find the longest consecutive sequence in a list

li = [3,8,2,1,4,5,7]

li.sort()
print(li)
current_strike = 1
longest_strike = 1
for i in range(1,len(li)):
    if li[i]!=li[i-1]:       
           #smallest element
        if li[i]==li[i-1]+1:
            # ye strike ko continue kerta h
            current_strike+=1
        else:
            if current_strike > longest_strike:
                longest_strike = current_strike
            current_strike=1
if current_strike>longest_strike:
    longest_strike = current_strike
print(longest_strike)


# Flatten a 2D list into a 1D list

li = [[1,2,3,],[2,5,7,],[1,7,2,]]
new_li = []
for i in li:
    for j in i:
        new_li.append(j)
print(new_li)

# Find the frequency of each element

li = [1]
# Merge two sorted lists into one sorted list

li1 = [4,6,7,3,2,1,3]
li2 = [2,4,6,4,26,2,1]
new_li = li1 + li2
new_li.sort()
print(new_li)

# Check if a list is a palindrome

li = [1,2,3,2,1]
new_li = []
for i in range(len(li)-1,-1,-1):
    new_li.append(li[i])
if new_li==li:
    print("list is palindrom ")
else:
    print("list is not palindrome")


# Find all pairs that sum to a target value

li = [1,2,3,4,4,5,6]
target_value = 5
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]+li[j] == target_value:
            print(li[i],li[j])


# Find the missing number in a list from 1 to n

li = [1, 3, 5, 6]

missing = []

for i in range(1,len(li)+2):   
    if i not in li:
        missing.append(i)
print(missing)

# Move all zeroes to the end while preserving order

li = [0,1,0,3,12]

for i in range(len(li)):
    if li[i]==0:
        li.remove(li[i])
        li.append(0)
print(li) 

# Find the majority element (appears more than n/2 times)

li = [3,2,1,3,2,3]
count = 0
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i] == li[j]:
            count+=1
print(count)

# Find the sublist with the maximum sum (Kadane&#39;s algorithm with loops)

li =  [1,2,3]
current_sum = 0
best_sum = 0

for i in li:
    current_sum+=i
    if current_sum>best_sum:
        best_sum=current_sum
    if current_sum<=0:
        current_sum = 0
print(best_sum)

# Transpose a matrix (list of lists)

li = [[1,2,3],[4,5,6]]
new_matrix = []
for i in range(len(li[0])):
    new_row = []
    for j in range(len(li)):
        new_row.append(li[j][i])
    new_matrix.append(new_row)
print(new_matrix)


# Find the intersection of two lists (no repeats)

first_li = [1,2,3,4]
second_li = [3,4,5,6]

for i in first_li:
    if i in second_li:
        print(i)

li = [9,6,3,2,6,4,56,4]

start = 0
end = start+1

while start< len(li)-1:

    if end>=len(li):
        start+=1
        end = start+1
        continue

    if li[start]>li[end]:
        li[start],li[end] = li[end],li[start]
        
    end+=1
   
print(li)


n= 567
