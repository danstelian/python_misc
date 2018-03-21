# Searching and replacing case-insensitive text
import re


text = 'UPPER PYTHON, lower python, Mixed Python'
matches = re.findall(r'python', text, flags=re.IGNORECASE)

print(matches)


# this is a problem
new_text = re.sub(r'python', r'snake', text, flags=re.IGNORECASE)
print(new_text)


# this is a solution
def matchcase(word, new_word):
    if word.isupper():
        return new_word.upper()
    elif word.islower():
        return new_word.lower()
    elif word[0].isupper():
        return new_word.capitalize()
    else:
        return new_word


new_text = re.sub('python', lambda word: matchcase(word.group(), 'snake'), text, flags=re.IGNORECASE)
print(new_text)

# instead of lambda try using closures
