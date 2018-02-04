import sys
import string
"""
Create a data structure that can be globaly used and holds each vowel of every tone
"""
# Now you understand what is a promgramming 'chores'
vowels = {'a': ['a', 'ā', 'á', 'ǎ', 'à'], 
          'e': ['e', 'ē', 'é', 'ě', 'è'],
          'i': ['i', 'ī', 'í', 'ǐ', 'ì'],
          'o': ['o', 'ō', 'ó', 'ǒ', 'ò'],
          'u': ['u', 'ū', 'ú', 'ǔ', 'ù'],
          'ü': ['ü', 'ǖ', 'ǘ', 'ǚ', 'ǜ']}

def pinyin(word, punc):
    """
    Parameters:
    str: a string of word with number of tone at the end 

    Return:
    str: a string of pinyin without the number at the end

    Usage Examples:
    >>> pinyin('hao3')
    'hǎo'
    """
    word = word.replace('v', 'ü') 
    punctuation = ''
    while word[-1] in string.punctuation:
        punctuation += word[-1] 
        word = word[:-1]

    if word[-1].isdigit():
        tone = int(word[-1])
        word = word[:-1]
    else:
        return word + punctuation

    vowel_to_change = ''
    if 'a' in word:
        vowel_to_change = 'a'
    elif 'e' in word:
        vowel_to_change = 'e'
    elif 'i' in word:
        vowel_to_change = 'i'
    elif 'o' in word:
        vowel_to_change = 'o'
    elif 'u' in word:
        vowel_to_change = 'u'
    elif 'ü' in word:
        vowel_to_change = 'ü'
    else: 
        vowel_to_change = ''

    if vowel_to_change:
        new_word = word.replace(vowel_to_change, vowels[vowel_to_change][tone])

    return new_word + punctuation

def convert(sentence):
    """
    Takes in an input of sentence with words with tone number at each end.
    Calls convert function to convert each word.
    Then return the complete sentence of pinyin.

    Parameters:
    str: a string of sentence with multiple words 

    Return:
    str: a string of sentence with multiple pinyin

    Usage Examples:
    >>> convert('ni3 hao3 ma1')
    'nǐ hǎo mā'
    """
    result = []
    for word in sentence.split():
        result.append(pinyin(word, ''))

    return ' '.join(result)

def main():
    if len(sys.argv) == 1:
        """
        If runs with no argument, it asks for user input and print answer back
        """
        sentence = input('Input: ')
        result = convert(sentence)
        print(result)

    elif len(sys.argv) == 2:
        """
        If runs with one argument, it expects a txt file to convert it and
        output into another txt file named 'output.txt'
        """
        print('1 arg')
    else:
        """
        If runs with more than one argument, that is an error
        Or we can implement multiple file features but still
        output into one file 'output.txt' separate by new line
        """
        print('many args')

if __name__ == '__main__':
    main()

