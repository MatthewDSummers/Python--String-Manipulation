from collections import Counter

def reverse_the_characters(text):
    return text[::-1]
    # Steps backwards through the entire string starting at last character
print(reverse_the_characters("i am happy"))
# output: "yppah ma i"

def reverse_the_words(text):
    reversed = text.split(" ")
    reversed.reverse()
    return " ".join(reversed)
    # Returns a string with order of its words reversed
print(reverse_the_words("i am happy"))
# output: "happy am i"

def alphabetize_text(text):
    sort = sorted(text)
    return "".join(sort).replace(" ", "")
    # Returns text alphabetized
print(alphabetize_text("gf ed c ba"))
# output: abcdefg

def is_anagram(string1, string2):
    return Counter(string1.replace(" ", "")) == Counter(string2.replace(" ", ""))
    # Returns True if string1 is an anagram of string2; False otherwise 

### Alternative solution (not as efficient; more of an exercise in string manipulation)

    # string1 = ''.join(sorted(string1.lower().replace(" ", "")))
    # string2 = ''.join(sorted(string2.lower().replace(" ", "")))

    # return string1 == string2
print(is_anagram("i listen", "isilent")) # True
print(is_anagram("Not", "An anagram")) # False