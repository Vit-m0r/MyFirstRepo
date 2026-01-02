digit_colors = {
        "black": "0",
        "brown": "1",
        "red": "2",
        "orange": "3",
        "yellow": "4",
        "green": "5",
        "blue": "6",
        "violet": "7",
        "grey": "8",
        "white": "9"
    }

def value(colors):
    digit = ""
    for i in range(2):
        if colors[i] in digit_colors:
            digit += digit_colors[colors[i]]   
        else:
            raise KeyError("Такого цвета нет")
    return int(digit)
