def square(number):
    if number < 1 or number > 64:    
        raise ValueError("square must be between 1 and 64")
    count = 1
    for i in range(1, number):
        count *= 2
    return count
    


def total():
    return 2 ** 64 - 1