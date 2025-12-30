def rotate(text, key):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    big_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_str = ""
    for i in range(len(text)):
        index = alphabet.find(text[i])
        if index == -1:
            index = big_alphabet.find(text[i])
            if index == -1:
                new_str += text[i]
            elif index + key >= 26:
                step = index + key - 26
                new_str += big_alphabet[step]
            else:
                new_str += big_alphabet[index + key]
        elif index + key >= 26:
            step = index + key - 26
            new_str += alphabet[step]
        else:
            new_str += alphabet[index + key]
    return new_str