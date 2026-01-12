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



def label(colors):
    answer = ""
    for i in range(2):
        answer += digit_colors[colors[i]]
    n = digit_colors[colors[2]]
    for i in range(int(n)):
        answer += "0"
    if answer[-1:-10:-1] == "000000000":
        return answer.replace("000000000", "") + " gigaohms"
    elif answer[-1:-7:-1] == "000000":
        return answer.replace("000000", "") + " megaohms"
    elif answer[-1:-4:-1] == "000":
        return answer.replace("000", "") + " kiloohms"
    elif answer[0] == "0" and len(answer) >= 2:
        return answer.replace("0", "", 1) + " ohms"
    else:
        return answer + " ohms"
        