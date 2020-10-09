from random import randint
L = [randint(0, 20) for i in range(5)]
print(L)
s=int(input("Введите число из списка: "))
pos=-1
k=1
for elem in L:
      if s==elem:
          pos=k
          break
      k=k+1
print("Число в списке под номером: ",pos)



