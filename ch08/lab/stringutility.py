class StringUtility:
    def __init__(self,string = None):
        self.string = string
    
    def __str__(self):
        return self.string
    
    def vowels(self):
        count = 0 
        vowel = ["a","e","i","o","u"]
        for i in self.string:
            if i in vowel:
                count += 1
        if count >= 5:
            return str("many")
        if count <= 5:
            return str(count)
    
    def bothEnds(self):
        if len(self.string[:2] + self.string[-2:]) < 2:
            return ""
        else:
            return self.string[:2] + self.string[-2:]
    
    def fixStart(self):
        if len(self.string) <= 1:
            return self.string
        first = self.string[0]
        rest = self.string[1:]
        char = first

        for i in rest:
            if i == first:
                char += "*"
            else:
                char += i
        
        return char
    
    def asciiSum(self):
        sum = 0
        for i in self.string:
            sum += ord(i)
        return sum
    
    def cipher(self):
        result = ""
        for char in self.string:
            if char.isalpha():
            
                start = ord('A') if char.isupper() else ord('a')
            
                new_pos = (ord(char) - start + len(self.string)) % 26
            
                char = chr(start + new_pos)
            result += char
        return result
