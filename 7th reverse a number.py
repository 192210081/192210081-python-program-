def reverse_word(word):
    reversed_word = ''
    
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    return reversed_word


word = input("Enter a word: ")
reversed_word = reverse_word(word)
print("Reversed word:", reversed_word)
