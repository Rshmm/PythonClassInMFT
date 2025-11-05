# path = "C:\\Users\\intel\\Desktop\\text.txt"

# names = ["Arsham\n","Ali\n","Reza\n","Mohammad\n"]

# f = open(path,"w")
# # f.write("Hello")
# for name in names:
#     f.writelines(name)
# f.close()

f = open("text.txt", "w", encoding="utf-8")
f.write("سلام آرشام ")
f.close()
