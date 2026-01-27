# In this code we are definig a  function to find all occurrences of a substring in a given string
def find_occurrences(string, substring):
    occurrences = []
    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        occurrences.append(start)
        start += len(substring)  # Move past the last found substring
    return occurrences
# Example usage
string = "This is a test string. This test is only a test."
substring = "test"
print(find_occurrences(string, substring))  # Output: [10, 26, 43]  
# The output indicates the starting indices of each occurrence of "test" in the string.
# The function returns a list of starting indices where the substring is found in the string.