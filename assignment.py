# def fact(num):
#     factorial = 1
#     i=1
#     while(i<=num):
#         factorial*=i
#         i+=1
#     print(factorial)
# fact(5)

# def is_prime(number):
#     factor = 0
#     i = 2
#     while(i<number):
#         if number%i==0:
#             factor+=1
#         i+=1
#     if factor==0:
#         print("it's prime number ")
#     else:
#         print("not a prime number ")

# is_prime(23)    



# def square(n):
#     print(n+5)

# square(6)
# def test(a,b):
#     print(a,b)



# test(10,square(5))


# def square(n):
#     return n*n

# def test(a,b):                         #a is 10
#     print("inside test: ",a,b)
#     print("square: ", a*square(a))     # 5*25

# test(5,square)                          #test (10,memory)  step 1

# def test():
#     print("hey user ")
#     return len
# out = test()
# print("Out value:: ",out)

# def key():
#     print("hay khushi ")
# dic = {1:'khushi'}
# dic = {1:'khushi',2:key}

# out = key()
# # print("out:: ",out)
# # print(dic)

# def test(n):
    
#     print("n::",id(n))
#     print("hey")

# num = 4
# test(num)
# print("num:: ",num)
# print("num reference:: ",id(num))
# # print("n reference:: ",id(n))
# print("reference of fuction ", id(test(num)))

# def test(num):
#     li.append(6)
#     print("inside function :" ,li)

# li = [1,2,3,5]
# test(li)
# print('outside function',li)
# print("reference of li:: ",id(li))
# print("reference of function:: ",id(test(li)))



# out = lambda x: x+5
# print("lambda return ",out(29))
# print('out ',out)

# dic = {1:lambda x:x+5}
# print(dic[1])
# y=dic[1]
# y(10)

# map function

# map (function_name,iterable)
map(len,[])


def function():
    print("line 1")
    yield 1


gen = function()
print("gen:: ",gen)
a = next(gen)              #to call it we do it next function
print(a)


def func():
    print("first time ")
    i=1
    while(True):
        print("inside loop ",i)
        yield i
        print('<- Restart generator-> increase value for i' )
        i+=1

generator_fuc = func()
print(next(generator_fuc))


print(next(generator_fuc))

# ----------------------------------------------------------------


def func():
    print("first time ")
    i=1
    while(True):
        print("inside loop ",i)
        yield i
        print('<- Restart generator-> increase value for i' )
        i+=1

generator_fuc = func()
print(next(generator_fuc))

for i in range(5):
    print(next(generator_fuc))

# -----------------------------------------------------------------

# fibonacci series 

# def fibonaccie():
#     a=0
#     b=1
#     while(True):
#         c = a+b
#         yield f'fibonaccie series {a}'
#         a=b
#         b=c

# gen = fibonaccie()

# for i in range(10):
#     print(next(gen))

# -----------------------------------------------------------------

def fibonaccie(n):
    a=0
    b=1
    while(n):
        c = a+b
        yield f'fibonaccie series {a} n:{n}'
        a=b
        b=c
        n-=1
gen = fibonaccie(10)

for i in gen:
    print(i)

# map function is used to itered each element of a sequence
 
# mylist = ['hey','khushi','mona','pinka']

# out = map(len,mylist)
# print('out: ',out)         #it will reference of out
# print(next(out))
# print(next(out))

# ----------------------------------------------

 
# mylist = ['hey','khushi','mona','pinka']

# out = list(map(len,mylist))
# print(out)

# ----------------------------------------------

# mylist = [6,8]

# def test(n):
#     return n*10

# out = (map(test,mylist) )
# print(next(out))


# --------------------------

# mylist = [6,8]
# out = map(lambda n: n*10,mylist)
# print(next(out))

# ---------------------------------------------------

li =[1,2,3,8,9,5,3]

def is_even(n):
    return n%2==0

even = filter(is_even,li)
print(next(even))

# ----------------------------------------------------

li =[1,2,3,8,9,5,3]

def is_even(n):
    return n%2==0

even = filter(is_even,li)
print(list(even))

# -----------------------------------------------------

s = ['k','h','u','s','h','i']

# s = s[::-1]

# print(s)

new_string = []
for i in range(len(s)-1,-1,-1):
    new_string.append(s[i])
print(new_string)


