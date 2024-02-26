from itertools import permutations

def get_possible_words(letters):
    """
    Generate possible words from given letters
    """
    perms = permutations(letters)
    possible_words = [''.join(word) for word in perms]
    return possible_words

while True:
    user_input = input("Enter a word (type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        break
    
    possible_words = get_possible_words(user_input)
    
    print("Possible words:")
    for word in possible_words:
        print(word)
