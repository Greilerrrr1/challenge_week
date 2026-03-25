def reverse_string(sentence):
   reversed_sentence = sentence[::-1]
   return reversed_sentence
if __name__ == "__main__":
    print(reverse_string("I want to test this to see if it's working."))

# using a loop

# def reverse_string2(sentence: str):
#     result_string = ""
#     for x in sentence:
#         result_string = x + result_string
#     return(result_string)




# print(reverse_string2("Random"))