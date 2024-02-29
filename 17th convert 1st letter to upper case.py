def convert_and_join(sentence):
    words = sentence.split()  
    capitalized_words = [word.capitalize() for word in words]  
    result = '.'.join(capitalized_words)  
    return result

sentence = "this is  a cat"
converted_sentence = convert_and_join(sentence)
print(converted_sentence)
