class LargestNumber:

    def __init__(self,list):
        self.list = list

    def largest_number_of_list(self):

        return max(self.list)

largestValue = LargestNumber((2,4,5,6,3,4,5,634,23,35,24))

number = largestValue.largest_number_of_list()
print(number)
