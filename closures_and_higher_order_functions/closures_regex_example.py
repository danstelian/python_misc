import re


text = 'UPPER PYTHON, lower python, Mixed Python'

new_word = 'snake'

#1 match the case of the word to be replaced

pattern = re.compile('python', flags=re.IGNORECASE)

new_text = pattern.sub(new_word, text)
print('1', new_text)  # UPPER snake, lower snake, Mixed snake


#2 fixing the problem


def matchcase(new_word):
    w = new_word

    def replace(match_word):
        m = match_word.group()

        if m.isupper():
            return w.upper()
        elif m.islower():
            return w.lower()
        elif m[0].isupper():
            return w.title()
        else:
            return w

    return replace


new_text = pattern.sub(matchcase(new_word), text)
print('2', new_text)  # UPPER SNAKE, lower snake, Mixed Snake


#3 more descriptive
new_matchcase_func = matchcase('snake')

new_text = re.sub('python', new_matchcase_func, text, flags=re.IGNORECASE)
print('3', new_text)
# new_matchcase_func is called 3 times like this:
# new_matchcase_func('PYTHON')
# new_matchcase_func('python')
# new_matchcase_func('Python')


#4 without closures
def match_case(m, w):
    if m.isupper():
        return w.upper()
    elif m.islower():
        return w.lower()
    elif m[0].isupper():
        return w.title()
    else:
        return w


new_text = re.sub('python', lambda match: match_case(match.group(), 'snake'), text, flags=re.IGNORECASE)
print('4', new_text)
