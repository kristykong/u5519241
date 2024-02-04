def case_counter(text):
    uppercase_count = 0
    lowercase_count = 0
    
    # Iterate through each character in the string
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            uppercase_count += 1
        # Check if the character is a lowercase letter
        elif char.islower():
            lowercase_count += 1
    
    # Print the counts
    print(f"Uppercase letters: {uppercase_count}, Lowercase letters: {lowercase_count}")

case_counter("Kong") 