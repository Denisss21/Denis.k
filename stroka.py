a=input('Enter the text: ')
def stroka(a):
    for i in a:
        s=input('Select the letter: ')
        b=a.count(s)
        print('Quanity letters in the text: ',b)
stroka(a)