a=int(input('Enter range of series: '))
b=0
c=1
r=" "
print('FIBONACCI SERIES: ')
for i in range(a+1):
    print(b, r)
    d=b+c
    b=c
    c=d
