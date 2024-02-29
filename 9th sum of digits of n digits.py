def count_words(sentence):
    words = sentence.split()  
    return len(words)  


sentence = "Python is a high level interpreted programming language"
num_words = count_words(sentence)
print("Number of words in the sentence:", num_words)
