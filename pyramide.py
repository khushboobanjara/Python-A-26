# *
# * *       
# * * *     
# * * * *   
# * * * * * 

for i in range(5):
    for j in range(5):
        if i>=j:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#--------------------------------------

#           * 
#         * * 
#       * * *
#     * * * *
#   * * * * *

for i in range(5):
    for j in range(5,-1,-1):
        if i>=j:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#------------------------------------

# * * * * * 
#   * * * *
#     * * *
#       * *
#         *

for i in range(5,0,-1):
    for j in range(5,0,-1):
        if i>=j:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#-----------------------------------

# * * * * * 
# * * * *   
# * * *
# * *
# *

n=4
for i in range(n,-1,-1):
    for j in range(5):
        if j<=i:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#----------------------------------

# 1       
# 2 2     
# 3 3 3
# 4 4 4 4

n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print(i,end=' ')
        else:
            print(" ",end=' ')
    print()

#---------------------------------

# 1       
# 2 3     
# 4 5 6
# 7 8 9 10

n=4
temp=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print(temp,end=' ')
            temp+=1
        else:
            print(" ",end=' ' )
    print()

#--------------------------------------

#       1
#     2 1
#   3 2 1
# 4 3 2 1

n=4
for i in range(1,n+1):
   
    for j in range(n,0,-1):
        if j<=i:
            print(j,end=' ')
        else:
            print(" ",end=" ")
    print()

#---------------------------------------

# A
# B B
# C C C
# D D D D

ch='A'
temp=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print(chr(65+temp),end=' ')
            
        else:
            print(" ",end=' ' )
    temp+=1
    print()

#-------------------------------------------

# A
# B C
# D E F
# G H I J

ch='A'
temp=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print(chr(65+temp),end=' ')
            temp+=1
        else:
            print(" ",end=' ' )
    print()

#-------------------------------------------

#       1 
#     1 2 3 
#   1 2 3 4 5
# 1 2 3 4 5 6 7

n=4
for i in range(1,n+1):
    for sp in range(n-i):
        print(" ",end=' ')
    for j in range(1,2*i):
        print(j,end=' ')
    print()

#-------------------------------------------

#         *   
#       *   *   
#     *   *   *
#   *   *   *   *
# *   *   *   *   *

n=5
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j<=i:
            print("*",end="   ")
        else:
            print(" ",end=" ")
    print()

#-----------------------------------------       

# *   *   *   *   *   
#   *   *   *   *   
#     *   *   *
#       *   *
#         *

n=5
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if j<=i:
            print("*",end="   ")
        else:
            print(" ",end=" ")
    print()

#-----------------------------------------

#                 1   
#               2   2   
#             3   3   3
#           4   4   4   4
#         5   5   5   5   5
#       6   6   6   6   6   6
#     7   7   7   7   7   7   7
#   8   8   8   8   8   8   8   8
# 9   9   9   9   9   9   9   9   9

n=9
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j<=i:
            print(i,end="   ")
        else:
            print(" ",end=" ")
    print()

#----------------------------------------

#                 1
#               1   2
#             1   2   3
#           1   2   3   4
#         1   2   3   4   5
#       1   2   3   4   5   6
#     1   2   3   4   5   6   7
#   1   2   3   4   5   6   7   8
# 1   2   3   4   5   6   7   8   9


n=9
for i in range(1,n+1):
    temp=1
    for j in range(n,0,-1):
        if j<=i:
            print(temp,end="   ")
            temp+=1
        else:
            print(" ",end=" ")
    print()

#------------------------------------

#                 *
#               *   *   
#             *   *   *
#           *   *   *   *
#         *   *   *   *   *
#       *   *   *   *   *   *
#     *   *   *   *   *   *   *
#   *   *   *   *   *   *   *   *
# *   *   *   *   *   *   *   *   *


n=9
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j<=i:
            print("*",end="   ")
        else:
            print(" ",end=" ")
    print()

#------------------------------------------

# *   *   *   *   *   *   *   *   *   
#   *   *   *   *   *   *   *   *   
#     *   *   *   *   *   *   *
#       *   *   *   *   *   *
#         *   *   *   *   *
#           *   *   *   *
#             *   *   *
#               *   *
#                 *

n=9
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if j<=i:
            print("*",end="   ")
        else:
            print(" ",end=" ")
    print()
#-----------------------------------------

# 9   9   9   9   9   9   9   9   9   
#   8   8   8   8   8   8   8   8   
#     7   7   7   7   7   7   7
#       6   6   6   6   6   6
#         5   5   5   5   5
#           4   4   4   4
#             3   3   3
#               2   2
#                 1

n=9
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if j<=i:
            print(i,end="   ")
        else:
            print(" ",end=" ")
    print()

#------------------------------------------

#                 1 
#               1 2 1 
#             1 2 3 2 1
#           1 2 3 4 3 2 1
#         1 2 3 4 5 4 3 2 1
#       1 2 3 4 5 6 5 4 3 2 1
#     1 2 3 4 5 6 7 6 5 4 3 2 1
#   1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1

n=9
for i in range(1,n+1):
    temp=1
    for j in range(n,0,-1):
        if j<=i:
            print(temp,end=" ")
            temp+=1
        else:
            print(" ",end=" ")
    temp=i-1
    for j in range(2,n+1):
        if j<=i:
            print(temp,end=" ")
            temp-=1     
    print()

#----------------------------------------

#       1 
#     2 3 
#   3 4 5
# 4 5 6 7

n=4
for i in range(1,n+1):
    temp=i
    for j in range(n,0,-1):
        if j<=i:
            print(temp,end=' ')
            temp+=1
        else:
            print(" ",end=' ')
    print()

#---------------------------------------

#       1       
#     2 3 2     
#   3 4 5 4 3
# 4 5 6 7 6 5 4


n=4
for i in range(1,n+1):
    temp=i
    for j in range(n,0,-1):
        if j<=i:
            print(temp,end=' ')
            temp+=1
        else:
            print(" ",end=' ')
    temp-=2
    for j in range(2,n+1):
        if j<=i:
            print(temp,end=' ')
            temp-=1
        else:
            print(" ",end=" ")
    print()  

n =4

for i in range(1,n+1):
    temp=1
    for j in range(n,-1,-1):
        if i>=j:
            print(temp,end = " ")
            temp+=1
        else:
            print(' ',end = " ")
    
    # temp+=1
    for j in range(2,n+1):
        if i>=j:
            print(temp,end = " ")
            temp+=1
        else:
            print(' ',end = " ")
    print()