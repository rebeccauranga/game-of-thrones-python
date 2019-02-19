
letters = 'abcdefghijklmnopqrstuvwxyz'

secret = [1, 0, 3] 

def translate(index, master):
    return master[index]

def map_over(collection, master, how):
    result = ''
    for item in collection:
        result += how(item, master)
    return result

def decode(number_list, master_list):
    return map_over(number_list, master_list, translate)
print(decode(secret, letters))

def decode_while(number_list, master_list):
    result = ''
    count = 0
    max_length = len(number_list)
    while count < max_length:
        result += master_list[number_list[count]]
        count += 1
    return result

print(decode_while(secret, letters))

print(map_over(secret, letters, translate))

