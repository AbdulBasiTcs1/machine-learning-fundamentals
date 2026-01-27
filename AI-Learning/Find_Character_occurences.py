# In this we will define a function in which we will found the position of the character in the string
def find_character_occurences(String,char):
    return String.count(char)

output = find_character_occurences("Welcome",'c')
print("The character found at : ",output)