# Ввести число, вывести все его делители.
n = int(input())
i = 2
while i <= n:
    if(n % i == 0):
      print(i)
    i+=1