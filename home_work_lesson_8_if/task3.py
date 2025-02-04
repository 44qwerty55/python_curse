from unittest.mock import patch
"""
task 3
Write a program that adds 'ing' to words (to each word) in the text:
"Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, 
dignissim vitae libero"
Then displays the resulting text. Punctuation marks should not end up inside the word. If a comma or period 
follows a word, this punctuation mark should go after the same word, but already transformed.
"""

import string
# Original text
text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero!"

# Split the text into words while preserving punctuation
words = text.split()
print(f"{words = }")
processed_words = []
print(string.punctuation)

# Process each word
for word in words:
    # Check if the word ends with punctuation
    if word[-1] in string.punctuation:
        # Separate punctuation from word
        pure_word = word[:-1]
        punctuation = word[-1]
        # Add 'ing' and restore punctuation
        processed_word = pure_word + 'ing' + punctuation
    else:
        # Just add 'ing' if no punctuation
        processed_word = word + 'ing'

    processed_words.append(processed_word)

# Join the words back together
result = ' '.join(processed_words)

# Print results
print("Original text:")
print(text)
print("\nProcessed text:")
print(result)
