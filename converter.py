roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def Converter(numeral):
    sum = 0
    for i in range(len(numeral) - 1):
        left = numeral[i]
        right = numeral[i + 1]
        if roman[left] < roman[right]:
            sum -= roman[left]
        else:
            sum += roman[left]
    sum += roman[numeral[-1]]
    return sum


print(Converter("XX"))