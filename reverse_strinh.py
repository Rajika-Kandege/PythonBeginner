class ReverseString:

    def __init__(self, name):
        self.name = name


    def reverse_name(self):
        return self.name[::-1]


reverseName = ReverseString("Gondola")
text = reverseName.reverse_name()
print(text)
