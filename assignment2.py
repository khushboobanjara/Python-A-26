# 2. Rotate a List Left by One Position

li = [10,20,30,40,50]
k=2
for j in range(k):
       
    first = li[0]

    for i in range(len(li)-1):
        li[i] =li[i+1]

    li[len(li)-1] = first

print(li)


# find the index of all occurences of a given element

li = [5,2,7,2,9,2]
target=2
for i in range(len(li)):
        if li[i]==target:
                print(i)

# remove all negetive numbers from list

li = [2,-5,8,-6,3]
new_li= []
for i in range(len(li)):
        if li[i] >0:
                new_li.append(li[i])

print(new_li)

# check whether a list is palindrome or not:

li = [1,2,3,2,1]
new_li=[]
for i in range(len(li)-1,-1,-1):
       new_li.append(li[i])

if li==new_li:
        print("list is palindrome ")
else:
       print("list is not palindrome ") 

# merge two lists and remove duplicates

li1 =[1,2,3]
li2 =[3,4,5]
new_li =[]
new_li = li1 + li2 
new_li2 = []

for i in range(len(new_li)):
        if new_li[i] not in new_li2:
                new_li2.append(new_li[i])

print(new_li2)

# find pairs whose sum equals target value
li=[2,7,11,15]
target =9
for i in range(len(li)):
        for j in range(i+1,len(li)):
                if li[i]+li[j]==target:
                        print(i,j)

# find mising number from 1 to n

li = [1, 2, 3, 5, 6]

missing = []

for i in range(1,len(li)+2):   
    if i not in li:
        missing.append(i)
print(missing)


s = 'abcde'
new_s = 'cdeab'

rotated = s[1:]+s[0]
print(rotated)
for i in s:
    if i in new_s:
        if (rotated==new_s):
                print(True)
        else:
                print(False)