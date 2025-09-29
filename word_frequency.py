#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

# This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        print("this is not a string")
        return False
    if not text[0].isupper():
        print("start with a capital letter")
        return False
    if not re.search(r'[.!?]$', text):
        print("end with punctuation")
        return False
    if not re.search(r'\w+', text):
        print("have atleast one word")
        return False
    return True

# Step 1: Prompt the user
user_sentence = input("Enter a sentence: ")
while not is_sentence(user_sentence):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")  # ✅ Fixed variable name from 'user_input' to 'user_sentence'

# Step 2: Split the sentence into words (remove punctuation and lowercase)
words = re.findall(r'\b\w+\b', user_sentence.lower())

# Step 3: Create lists to store unique words and their frequencies
unique_words = []
frequencies = []

# Step 4: Iterate through words and update frequencies
for word in words:
    if word in unique_words:
        index = unique_words.index(word)
        frequencies[index] += 1
    else:
        unique_words.append(word)
        frequencies.append(1)

# Display the results
print("\nWord Frequencies:")
for i in range(len(unique_words)):
    print(f"{unique_words[i]}: {frequencies[i]}")
