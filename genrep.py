# Namn: Marcus
# Datum: 2023-10-11

print("Beräknar differansen av jämna/udda tal...")

even_sum = 0
odd_sum = 0
count = 0

for i in range(2,2001,2):
    even_sum += i

for i in range(1,2000,2):
    odd_sum += i

print(f"Differensen={odd_sum-even_sum}")