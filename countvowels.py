class Vowels:

    def __init__(self,name):
        self.name = name


    def countVowels(self):
        count = 0
        vowels = "aeiouAEIOU"
        for character in self.name:
            if character in vowels:
                count +=1
        return count

vowels = Vowels("Africa")
numberOfVowels = vowels.countVowels()
print(numberOfVowels)

