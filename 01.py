import re

pattern = "^[a-zA-Z\s]{2,30}$"

print(re.match(pattern, "Apple"))     # ✅ True
print(re.match(pattern, "Apple123"))   # ✅ True (اشتباه! چون فقط اول "Apple" می‌خونه)

print(re.fullmatch(pattern, "Apple"))   # ✅ True
print(re.fullmatch(pattern, "Apple123"))# ❌ False (درسته!)
