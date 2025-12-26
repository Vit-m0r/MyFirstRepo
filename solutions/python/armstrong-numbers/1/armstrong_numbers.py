def is_armstrong_number(number):
    change_number = number
    sum = 0
    count = len(str(number)) 
    for i in range(count):
        right_digit = change_number % 10
        if change_number // 10 != 0 :
            change_number = change_number // 10
            sum += right_digit ** count
        else:
            right_digit = change_number % 10
            sum += right_digit ** count
    return sum == number
            