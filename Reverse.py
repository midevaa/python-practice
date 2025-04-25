# Prompt the user to enter a string
string = input("Enter a text: ")
# an empty string to store the reversed word
reversed_string = ""
# Loop through each letter in the original string and writes it in reverse
for char in string:
    reversed_string = char + reversed_string
# display reversed string
print(f"Reversed string: {reversed_string}")

