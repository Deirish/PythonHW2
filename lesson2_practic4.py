# Ввести число, вывести его разряды и их множители ( не могу понять, как вывести вместе с разрядами!((()
n = int(input())
i = 2
list_of_numbers = []
while i * i <= n:
    while n % i == 0:
        list_of_numbers.append(i)
        n = n / i
    i = i + 1
if n > 1:
    list_of_numbers.append(n)
    print(list_of_numbers)