def reverse_alphabetical(word):
    # Sort the letters of the word alphabetically in reverse order
    sorted_word = sorted(word, reverse=True)
    # Join the sorted letters to form the reversed alphabetical word
    reversed_alphabetical_word = ''.join(sorted_word)
    return reversed_alphabetical_word

# Main function
def main():
    # Input the word
    word = input("Enter a word: ")
    
    # Arrange the letters of the word alphabetically in reverse order
    reversed_alphabetical_word = reverse_alphabetical(word)
    
    # Output the result
    print("Word with letters arranged alphabetically in reverse order:", reversed_alphabetical_word)

# Run the program
if __name__ == "__main__":
    main()
