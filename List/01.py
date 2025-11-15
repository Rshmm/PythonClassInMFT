# 1.
# یک لیست ایجاد کنید که شامل اعداد ۱ تا ۱۰ باشد. سپس:
# عنصر اول و آخر لیست را چاپ کنید.
# عناصر میانی لیست را چاپ کنید.


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[0])
print(numbers[-1])
# print(numbers[start:stop:step])
print(numbers[1:len(numbers) - 1:])  # [2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[1:-1:])  # [2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[1:])  # [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[:5])  # [1, 2, 3, 4, 5]
print(numbers[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

new_list = numbers[:]

print(numbers)
print(new_list)

numbers[0] = 12

print(new_list)
print(numbers)

print("*" * 50)

#
# 2.
# یک لیست خالی ایجاد کنید.
# عدد ۵ را به لیست اضافه کنید.
# عدد ۱۰ را به ابتدای لیست اضافه کنید.
# عنصر دوم را حذف کنید.
# لیست را چاپ کنید.

numbers = []

numbers.append(5)
numbers.insert(0, 10)
numbers.pop(1)  # index
print(numbers)

print("*" * 50)

# 3.
# یک لیست شامل اعداد تصادفی ایجاد کنید، مثلاً [4, 1, 8, 3, 7]. سپس:
#
# لیست را به ترتیب صعودی مرتب کنید.
# لیست را به ترتیب نزولی مرتب کنید.


numbers = [7, 3, 8, 1, 4]

numbers.sort()  # [1, 3, 4, 7, 8]
numbers.sort(reverse=True)  # [8, 7, 4, 3, 1]

print(numbers)

print("*" * 50)

# 4.
# یک لیست شامل اعداد [2, 5, 8, 11, 14, 17] ایجاد کنید.
# بررسی کنید که آیا عدد ۸ در لیست وجود دارد؟
# بررسی کنید که آیا عدد ۱۰ در لیست وجود دارد؟
# اندیس عدد ۱۱ را پیدا کنید


numbers = [2, 5, 8, 11, 14, 17, 11]

print(8 in numbers)

if 10 in numbers:
    print('10 found in this list of numbers')
else:
    print('10 not found in this list of numbers')

print(numbers.index(11))

# اگر چند تا 11 داشته باشیم و دنبال همه ایندکس ها با مقدار 11 باشیم
for i in range(len(numbers)):
    if numbers[i] == 11:
        print(i)

print("*" * 50)

# 5.
# یک لیست شامل اعداد [3, 6, 9, 12, 15] ایجاد کنید.
# مجموع کل اعداد را محاسبه کنید.
# میانگین اعداد را محاسبه کنید.
# بزرگ‌ترین و کوچک‌ترین عدد لیست را پیدا کنید.


numbers = [3, 6, 9, 12, 15]

sm = 0

for number in numbers:
    sm += number

avg = sm / len(numbers)

sorted_numbers = sorted(numbers)

min_num = sorted_numbers[0]
max_num = sorted_numbers[-1]

print("sum : ", sm)
print("average : ", avg)
print("min : ", min_num)
print("max : ", max_num)

print("*" * 50)
# 6.
# یک لیست شامل [1, 2, 3, 4, 5] ایجاد کنید.
# لیست را به صورت معکوس چاپ کنید (بدون استفاده از توابع آماده).


numbers = [1, 2, 3, 4, 5]

reversed_number = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_number.append(numbers[i])

print(reversed_number)

print(numbers[::-1])

print("*" * 50)

# 7.
# یک لیست شامل لیست‌های دیگر بسازید، مانند [[1, 2], [3, 4], [5, 6]].
# به عنصر ۴ دسترسی پیدا کنید.
# جمع اعداد داخل هر زیرلیست را محاسبه کرده و در یک لیست جدید ذخیره کنید.

numbers = [[1, 2], [3, 4], [5, 6]]

print(numbers[1][1])

sm_lst = []

for sublist in numbers:
    sm = 0
    for num in sublist:
        sm += num
    sm_lst.append(sm)

print(sm_lst)
print("*" * 50)

# 8.
# یک رشته مانند "hello world" تعریف کنید.
# کاراکترهای این رشته را به لیست تبدیل کنید.
# تعداد کاراکترهای l را در لیست بشمارید.

string_1 = "H,e,l,l,o, ,w,o,r,l,d"

string_list = string_1.split(",")

print(string_list)
print(len(string_list))

print("*" * 50)

# 9.
# یک لیست شامل اعداد [10, 21, 4, 45, 66, 93] ایجاد کنید.
# تنها اعداد زوج لیست را چاپ کنید.
# تنها اعداد فرد لیست را چاپ کنید.


numbers = [10, 21, 4, 45, 66, 93]

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even numbers : ")
for even_number in even_numbers:
    print(even_number, end=" ")

print("\nodd numbers : ")
for odd_number in odd_numbers:
    print(odd_number, end=" ")
print()


print("*" * 50)
# 10.
# دو لیست مانند [1, 2, 3] و [4, 5, 6] ایجاد کنید.
# این دو لیست را با هم ادغام کنید.
# از لیست ادغام شده، ۳ عنصر اول و ۳ عنصر آخر را استخراج کنید.


numbers_1 = [1, 2, 3]
numbers_2 = [4, 5, 6]


numbers_3 = numbers_1 + numbers_2

print(numbers_3)

mid = len(numbers_3) // 2

print(numbers_3[mid:])
print(numbers_3[:mid])