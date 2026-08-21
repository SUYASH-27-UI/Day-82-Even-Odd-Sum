numbers = [10, 15, 22, 33, 40, 57, 68, 71]

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum = even_sum + num
    else:
        odd_sum = odd_sum + num

print("Sum of Even Numbers:", even_sum)
print("Sum of Odd Numbers:", odd_sum)
