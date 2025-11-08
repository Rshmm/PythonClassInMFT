# 1 - Start
# 2 - Read integer n
# 3 - If n <= 1 then
#       3.1 - Print "The number is NOT a Perfect number"
# 4 - Else
#       4.1 - Initialize sum <-- 1
#       4.2 - For each integer i from 2 to n**0.5 do
#               4.2.1 - If n mod i = 0 then
#                       4.2.1.1 - sum <-- sum + i
#                       4.2.1.2 - If n != n / i then
#                               4.2.1.2.1 - sum <-- sum + (n / 1)
#                                 END IF
#                       END IF
#             END FOR
#     END IF
# 5 - If num = n then
#       5.1 - Print "The number is a Perfect number"
# 6 - Else:
#       6.1 - Print "The number is NOT a Perfect number"
#     END IF
# 7 - End


n = int(input("Enter a number : "))

if n <= 1:
    print("This number is not a perfect number")
else:
    total = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i

    if total == n:
        print("This number is a perfect number")
    else:
        print("This number is not a perfect number")
