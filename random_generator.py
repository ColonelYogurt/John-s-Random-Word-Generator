import random

def random_word(list, n):

    words = [random.choice(list) for _ in range(n)]
    
    return words


import random

def generate_random_word(length):

    characters = 'abcdefghijklmnopqrstuvwxyz'
    
  
    word = ''.join(random.choice(characters) for _ in range(length))
    
    return word


#too lazy to write main its 5am here
wordlist = []

Pwordlist[i] = [generate_random_word(5) for _ in range(43)]

ret = random_word(list, 8)
