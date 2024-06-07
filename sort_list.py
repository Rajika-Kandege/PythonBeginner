class SortList:

    def __init__(self,list):
        self.list = list

    def sorting(self):
        return sorted(self.list)

sortlist = SortList((2,4,56,2,3,4,523,45,24,23,45,65,45))

numbers = sortlist.sorting()
print(numbers)
