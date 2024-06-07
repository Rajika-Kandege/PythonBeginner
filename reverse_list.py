class Reverse:

    def __init__(self, list):
        self.list = list

    def reverse(self):
        return self.list[::-1]
    # can use [::] too

reverselist = Reverse((3,4,5,6,2,3,4,5))
numbers = reverselist.reverse()
print(numbers)
