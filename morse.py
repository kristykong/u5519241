def morse_translator(text):
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    morse_parts = []
    
    # Split the text
    words = text.upper().split()
    
    for word in words:
        # Initialize an empty list
        morse_word = []
        for char in word:
            if char in morse_code_dict:
                # Translate character
                morse_word.append(morse_code_dict[char])
        # Join the Morse code of the current word
        morse_parts.append(" ".join(morse_word))
    
    # Join all Morse code parts
    return " / ".join(morse_parts)

print(morse_translator("HELLO WORLD"))