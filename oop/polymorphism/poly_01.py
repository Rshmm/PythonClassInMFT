class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

    # def add(self, a, b,c):
    #     return a + b + c

calc = Calculator()
print(calc.add(2, 3))      # فقط دو عدد
print(calc.add(2, 3, 4))   # سه عدد
