a= int(input('Enter your number: '))
# FOR EVEN ODD
if(a%2==0):
    print( a,' is EVEN')
else:
    print(a,' is ODD')

# FPR PRIME
b=0
for i in range(2, a-1):
    if(a%2==0):
     b=b+1
if b>0:
    print(a, ' is not PRIME')
else:
    print(a, 'is PRIME')

# FOR PALLINDROME

rev=0
b=a
while(b !=0):
    r=b%10
    rev=rev*10+r
    b=b//10
if (rev==a):
    print(a,'is PALINDROME')
else:
    print(a,'is not PALINDROME')

# FOR ARMSTRONG

c=a
e=a
sum=0
d=0
while(c!=0):
    rem=c%10
    d=d+1
    c=c//10
while(e!=0):
    rem=e%10
    sum = sum + (rem**d)
    e=e//10
if(sum==a):
    print(a,'is ARMSTRONG')
else:
    print(a,'is not ARMSTRONG')
