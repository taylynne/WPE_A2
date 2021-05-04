# Week one exercise:
# acrobot -- make acronyms

def acrobot(string, min_word_length=0):
    acro = ""

    for word in string.split():
        if len(word) >= min_word_length:
            acro = acro + word[0].upper()
        else:
            pass

    return acro
