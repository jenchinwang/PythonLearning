## As titled. All vowel will be removed by running this program.

def anti_vowel(text):
    new_string = ""
    for x in range(len(text)):
        if text[x] in "aeiouAEIOU":
            continue
        else:
            new_string = new_string + text[x]
    return new_string        
inp = raw_input('Please enter a string: ')
inp = str(inp)
print anti_vowel(inp)