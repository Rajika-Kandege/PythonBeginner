class EvenOdd:

    def __init__(self,number):
        self.number = number

    def even_or_odd(self):
        if(self.number % 2 == 0):
            print(f"{self.number} is even")

        else:
            print(f"{self.number} is odd")


given_number = EvenOdd(28)
given_number.even_or_odd()

