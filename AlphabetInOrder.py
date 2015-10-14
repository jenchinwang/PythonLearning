## This program will find the longest alphabetic letters 
## in order inside an user input string. For Example
## "abcdabefiklmasdfuqwh"
## will return "abefiklm". Try it to test it out!

def AlphabetInOrder(s):
    str = s[0]
    lrg_str = ""
    print "The first letter is", s[0]
    for i in range(1,len(s)):        
        if s[i] >= s[i-1]:
            str += s[i]
            print "The new letter appended is", s[i]
            if len(str) > len(lrg_str):
                lrg_str = str            
        else:
            str = s[i]
            print "Starting a new string with", s[i]
    return lrg_str
s = raw_input("Please enter a string: ")
print AlphabetInOrder(s)