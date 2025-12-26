def convert(number):
    str_our = ""
    if number % 3 == 0:
        str_our += "Pling"
    if number % 5 == 0:
        str_our += "Plang"
    if number % 7 == 0:
        str_our += "Plong"
    if str_our == "":
        return str(number)
    return str_our
