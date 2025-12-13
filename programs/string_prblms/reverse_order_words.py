# Write a program to Reverse the order of the words in a sentence.
def reverse_words(str):
    words = str.strip()
    reversed_sentence = " "
    
    for i in range(len(words) -1, -1, -1):
        reversed_sentence =+ words[i] + ""
        
    
    return reversed_sentence.strip()



str = input("Enter a sentence : ")
result = reverse_words(str)
print("Reversed sentence:",result)



    