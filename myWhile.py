a=int(input('Enter A: '))
b=int(input('Enter B: '))
c=int(input('C: '))
def myWhile(a,b,c):
    while a > b:
        b+=c
        if a > b:
            print('Value A is not yet',a)
        else:
            a<b
            print('Finally: ',a)
myWhile(a,b,c)
