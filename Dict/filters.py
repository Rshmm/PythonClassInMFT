# data = {"ali" : 25, "sara" : 30, "reza" : 20, "maryam" : 35}
#
#
# filter = {k:v for k,v in data.items() if v > 20}
#
# print(filter)


original = {"a" : 1, "b" : 2, "c" : 3}

# doubled = {k: v * 2 for k,v in original.items()}
# print(doubled)

swapped = {v : k for k,v in original.items()}
print(swapped)

