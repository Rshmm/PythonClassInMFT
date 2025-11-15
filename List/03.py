# 1
# برنامه‌ای بنویسید که یک لیست شامل اعداد صحیح از کاربر بگیرد و دو لیست جداگانه شامل اعداد زوج و اعداد فرد بسازد و چاپ کند.
numbers = input("Enter list of numbers(use space to separate them) : ").split()

list_numbers = [int(num) for num in numbers]

evens = []
odds = []

for n in list_numbers:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

print("evens", evens)
print("odds", odds)

print("*" * 50)
# 2
# برنامه‌ای بنویسید که یک لیست از اعداد را بگیرد و دومین عدد بزرگ‌تر موجود در لیست را پیدا کند.
# شرط: بدون استفاده از توابع آماده مثل sorted.

numbers = input("Enter list of numbers(use space to separate them) : ").split()

list_numbers = [int(num) for num in numbers]

max1 = list_numbers[0]
for n in list_numbers:
    if n > max1:
        max1 = n

max2 = 0
for n in list_numbers:
    if n != max1 and n > max2:
        max2 = n

print("دومین بزرگ‌ترین عدد:", max2)

print("*" * 50)

# 3
# برنامه‌ای بنویسید که یک لیست از اعداد بگیرد و عناصر را به این ترتیب مرتب کند:
# اول اعداد زوج به‌ترتیب صعودی
# سپس اعداد فرد به‌ترتیب نزولی
numbers = input("Enter list of numbers(use space to separate them) : ").split()

list_numbers = [int(num) for num in numbers]

evens = []
odds = []

# جدا کردن
for n in list_numbers:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

# مرتب‌سازی صعودی evens
for i in range(len(evens)):
    for j in range(i + 1, len(evens)):
        if evens[j] < evens[i]:
            evens[i], evens[j] = evens[j], evens[i]

# مرتب‌سازی نزولی odds
for i in range(len(odds)):
    for j in range(i + 1, len(odds)):
        if odds[j] > odds[i]:
            odds[i], odds[j] = odds[j], odds[i]

# ترکیب
result = evens + odds

print("نتیجه:", result)




print("*" * 50)
# 4
# برنامه‌ای بنویسید که یک لیست از اعداد را بگیرد و عناصر تکراری و موقعیت (ایندکس) آن‌ها در لیست را نمایش دهد.

numbers = input("Enter list of numbers(use space to separate them) : ").split()

list_numbers = [int(num) for num in numbers]

for i in range(len(list_numbers)):
    for j in range(i + 1, len(list_numbers)):
        if list_numbers[i] == list_numbers[j]:
            print(list_numbers[i], "تکراری است → ایندکس‌ها:", i, "و", j)
