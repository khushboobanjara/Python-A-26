# 1. Create a list of numbers from 1 to 10 using list comprehension.

li = [x for x in range(1,11)]
print(li)

# 2. Create a list containing squares of numbers from 1 to 10.

li = [x*x for x in range(1,11)]
print(li)

# 3.Create a list containing cubes of numbers from 1 to 10.

li = [x*x*x for x in range(1,11)]
print(li)

# 4.Generate a list of even numbers from 1 to 20.

li = [x for x in range(1,21) if x%2==0]
print(li)

# 5.Generate a list of odd numbers from 1 to 20.

li = [x for x in range(1,21) if x%2!=0]
print(li)

# 6. Create a list of numbers divisible by 3 from 1 to 30.

li = [x for x in range(1,31) if x%3==0]
print(li)

# 7. Create a list of numbers greater than 10 from a given list.

li = [1,90,34,63,10,2]

num = [x for x in li if x>10]
print(num)

# 8.  From a list of numbers, create a new list containing only positive numbers.

li = [1,-4,2,7,-2,-8]
num = [x for x in li if x>0]
print(num)

# 9. From a list, create a list containing only negative numbers.

li = [1,-4,2,7,-2,-8]
num = [x for x in li if x<0]
print(num)

# 10. Create a list of numbers whose square is greater than 50.

li = [1,2,3,4,5,6,7,8,9,8]
num = [x for x in li if x*x>=50]
print(num)

# 11. Convert all words of a list into uppercase using list comprehension.

li = ['khushi','hello']
words = [word.upper() for word in li ]
print(words)

# 12. Convert all words into lowercase.

li = ['KHUSHI','HELLO']
words = [word.lower() for word in li ]
print(words)

# 13. Create a list containing length of each word from a list of strings.

li = ['khushi','hello','mono','varsha']
words = [len(words) for words in li]
print(words)

# 14. Extract only words having more than 4 characters.

li = ['khushi','hello','mono','varsha']
words = [words for words in li if len(words)>4]
print(words)

