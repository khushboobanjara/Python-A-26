n = int(input('enter a number '))

temp=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print(temp, end=" ")
            temp+=2
        else:
            print(' ',end=" ")
    print()

#---------------------------------

temp=n*n+n-1
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print(temp, end=" ")
            temp-=2
        else:
            print(' ',end=" ")
    print()

#---------------------------------

temp=2
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print(temp, end=" ")
            temp+=2
        else:
            print(' ',end=" ")
    print()

#---------------------------------

temp=n*n+n
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print(temp, end="   ")
            temp-=2
        else:
            print(' ',end=" ")
    print()

#---------------------------------

temp=1
for i in range(n,0,-1):
    for j in range(1,n+1):
        if j<=i:
            print(temp, end="  ")
            temp+=2
        else:
            print(' ',end="  ")
    print()

#---------------------------------

temp=n*n+n-1
for i in range(n,0,-1):
    for j in range(1,n+1):
        if j<=i:
            print(temp, end="  ")
            temp-=2
        else:
            print(' ',end="  ")
    print()

#---------------------------------

temp=2
for i in range(n,0,-1):
    for j in range(1,n+1):
        if j<=i:
            print(temp, end="  ")
            temp+=2
        else:
            print(' ',end="  ")
    print()

#---------------------------------

temp=n*n+n
for i in range(n,0,-1):
    for j in range(1,n+1):
        if j<=i:
            print(temp, end="  ")
            temp-=2
        else:
            print(' ',end="  ")
    print()

#--------------------------------

temp=1
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j<=i:
            print(temp, end=" ")
            temp+=2
        else:
            print('  ',end=" ")
    print()

#-------------------------------

temp=n*n+n-1
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j<=i:
            print(temp, end=" ")
            temp-=2
        else:
            print(' ',end=" ")
    print()

#-------------------------------

temp=2
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j<=i:
            print(temp, end=" ")
            temp+=2
        else:
            print('  ',end=" ")
    print()

#-------------------------------

temp=n*n+n
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j<=i:
            print(temp, end=" ")
            temp-=2
        else:
            print('  ',end=" ")
    print()

#-------------------------------

temp=1
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if j<=i:
            print(temp, end=" ")
            temp+=2
        else:
            print('  ',end=" ")
    print()

#------------------------------

temp=n*n+n-1
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if j<=i:
            print(temp, end=" ")
            temp-=2
        else:
            print('  ',end=" ")
    print()

#-------------------------------

temp=2
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if j<=i:
            print(temp, end=" ")
            temp+=2
        else:
            print('  ',end=" ")
    print()

#-------------------------------

temp=n*n+n
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if j<=i:
            print(temp, end=" ")
            temp-=2
        else:
            print('  ',end=" ")
    print()

