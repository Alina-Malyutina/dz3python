numbers = [1, 3, 5, 7, 9]
sum = 0
for i in range(1, len(numbers), 2):
        sum += numbers[i]       
print(f"{numbers} -> сумма элементов на нечётных позициях: {sum}")