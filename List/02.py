# 1.
# برنامه‌ای بنویسید که عناصر تکراری لیست زیر را حذف کند و تنها مقادیر یکتا را نگه دارد:
# items = [1, 2, 2, 3, 4, 4, 5, 5, 6]

items = [1, 2, 2, 3, 4, 4, 5, 5, 6]

unique_items = []
for n in items:
    if n not in unique_items:
        unique_items.append(n)

print(unique_items)


print("*" * 50)
# 2.
# با استفاده از لیست زیر، مجموع اعدادی را که در موقعیت‌های فرد (ایندکس‌های 1، 3، ...) قرار دارند، محاسبه کنید:
# numbers = [10, 20, 30, 40, 50, 60, 70]
numbers = [10, 20, 30, 40, 50, 60, 70]

total = 0
for i in range(len(numbers)):
    if i % 2 == 1:     # ایندکس فرد
        total += numbers[i]

print(total)

print("*" * 50)
# 3.
# برنامه‌ای بنویسید که تمام اعداد اول بین 1 تا 50 را در یک لیست ذخیره کرده و لیست را چاپ کند.
primes = []

for num in range(2, 51):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)

print(primes)

print("*" * 50)
# 4.
#
# برنامه‌ای بنویسید که تمام مقادیر صفر را در لیست زیر با عدد 100 جایگزین کند:
# numbers = [0, 5, 0, 10, 15, 0, 20]

numbers = [0, 5, 0, 10, 15, 0, 20]

for i in range(len(numbers)):
    if numbers[i] == 0:
        numbers[i] = 100

print(numbers)

print("*" * 50)

# 5.
# برنامه‌ای بنویسید که سه عدد از لیست داده‌شده را پیدا کند که مجموع آن‌ها بیشترین مقدار ممکن باشد
# numbers = [10, 20, 5, 8, 70, 30]

numbers = [10, 20, 5, 8, 70, 30]

max1 = 0
for n in numbers:
    if n > max1:
        max1 = n

max2 = 0
for n in numbers:
    if n != max1 and n > max2:
        max2 = n

max3 = 0
for n in numbers:
    if n != max1 and n != max2 and n > max3:
        max3 = n

print(max1, max2, max3)
print("sum:", max1 + max2 + max3)


