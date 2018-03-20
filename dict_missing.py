# The curious case of the missing dictionary
import re


class passthroughdict(dict):
    def __missing__(self, key):
        return key


censor = passthroughdict({
    'hell': 'h**l',
    'damn': 'd**n',
    'Damn': 'D**n'  # this needs to be dealt with in a more elegant way
})


text = 'What the hell?! Where is my phone? Damn, somebody must have taken it.'

censored_text = ''.join(censor[word] for word in re.split(r'([^a-zA-Z]+)', text))

print(censored_text)
