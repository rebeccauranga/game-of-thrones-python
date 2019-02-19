
letters = 'abcdefghijklmnopqrstuvwxyz'

secret = [1, 0, 3] # "bad"

def translate(index, master):
    return master[index]

def map_over(collection, master, how):
    result = ''
    for item in collection:
        result += how(item, master)

    return result

# give your functions "verb" names
def decode(number_list, master_list):
    return map_over(number_list, master_list, translate)
    # configuration came in as arguments
    # result = ''
    # count = 0 

    # do the translation 
    # for each item in number_list...
    # for item in number_list:
    #     # find that index in master_list...
    #     letter = master_list[item]

    #     # put that character in result 
    #     # result = result + letter
    #     result += letter

    # # return the result 
    # return result
   
    # the end result after defining the decode function
    # decoded_message = decode(secret, letters)
    # print(decoded_message)
#print(decode(secret, letters))

def decode_while(number_list, master_list):
    # configuration came in as arguments
    result = ''
    count = 0
    max_length = len(number_list)

    # do the translation
    # for each item in number_list...
    # for item in number_list:
    while count < max_length:
        # find that index in master_list...
        # item = number_list[count]
        # letter = master_list[item]

        # put that character in result
        # result = result + letter
        # result += letter
        
        # result += master_list[item]
        result += master_list[number_list[count]]
        count += 1

    # return the result
    return result

# print(decode_while(secret, letters))
# print(map_over(secret, letters, translate))




letters = 'abcdefghijklmnopqrstuvwxyz'
secret = 'bad'


def convert_letter_to_numbers(a_letter, master):
    # find a_letter in master
    return master.index(a_letter)
    # save the index
    # then return it

print(convert_letter_to_numbers('b', letters))
# 1

print(convert_letter_to_numbers('a', letters))
# 0

print(convert_letter_to_numbers('d', letters))
# 3

def map_over(collection, master, do_translation):
    result = []
    for letter in collection:
        result.append(do_translation(letter, master))
    return result

# for each item in a string sequence, translate to numbers
def encode(message, master):
    return map_over(message, master, convert_letter_to_numbers)
    # result = []
    # for letter in message:
    #     result.append(convert_letter_to_numbers(letter, master))
    # return result

print(encode(secret, letters))
# [1, 0, 3]




















