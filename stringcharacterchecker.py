class StringCharacterChecker:

    def __init__(self, string, character):
        self.string = string
        self.character = character

    def is_character_in_string(self):
        """Check if the character is present in the string."""
        return self.character in self.string

# Example usage
checker = StringCharacterChecker("Serangoong", "g")

result = checker.is_character_in_string()
print(result)  # Output: True
