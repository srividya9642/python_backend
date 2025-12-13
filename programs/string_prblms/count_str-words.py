# write a program to count the no of words in a string

def count_words(sentence):
    count = 0
    in_word = False

    for ch in sentence:
        if ch != ' ' and not in_word:
            count += 1       # starting of a new word
            in_word = True
        elif ch == ' ':
            in_word = False  # end of a word

    return count


# calling the function
text = input("Enter a sentence: ")
print("Number of words:", count_words(text))


def count_words(str):
    
    count = 0
    in_word = False
    for ch in str:
        if ch != ' ' and not in_word:
            count = count + 1
            in_word =  True
        elif ch == " ":
            in_word =  False
    return count

text  = input("Enter a string")
print("Number of words:",count_words(text))


def count_words(sentence):
    count = 0
    in_word = False
    i = 0

    while i < len(sentence):
        ch = sentence[i]

        if ch != ' ' and not in_word:
            count += 1         # start of a new word
            in_word = True
        elif ch == ' ':
            in_word = False    # end of a word

        i += 1  # move to next character

    return count


# Example usage
text = input("Enter a sentence: ")
print("Number of words:", count_words(text))

def count_words(str):
    count = 0
    in_word = False
    i = 0
    while i <len(str):
        ch = str[i]
        if ch != '' and not in_word:
            count = count + 1
            in_word = True
            i = i+1
        elif ch == '':
            in_word = False
            i = i+1
    return count

text = input("Enter a string")
print("Number of words:",count_words(text))










