class Calculation:

    def __init__(self, numberOne, numberTwo):
        self.numberOne = numberOne
        self.numberTwo = numberTwo

    def addition(self):
        print(f"{self.numberOne + self.numberTwo}")


    def multiplication(self):
        print(f"{self.numberOne * self.numberTwo}")

    def division(self):
        print(f"{self.numberOne / self.numberTwo}")

    def substraction(self):
        print(f"{self.numberOne - self.numberTwo}")

calculation = Calculation(15,5)
calculation.addition()
calculation.multiplication()
calculation.division()
calculation.substraction()
