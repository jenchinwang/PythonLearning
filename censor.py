## This program will censor all the words that are not welcome.
## You will make the decision on what phrases are not welcome.

def censor(text, word):   
    list = text.split()
    new_list = []
    for i in list:
        if i == word:
            new_list.append("*"*len(word))
        else:
            new_list.append(i)
    new_text = " ".join(new_list)
    return new_text

inp1 = raw_input('Please enter a sentence: ')
inp2 = raw_input('Please enter a word that you wish to censor: ')
print censor(inp1, inp2)