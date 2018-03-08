str = "123456789"
def getSolutions(s1, i):
    if i == 9:
        if eval(s1) == 100:
            print(s1)
        return
    if i > 0:
        getSolutions(s1 + '+' + str[i], i + 1)
    getSolutions(s1 + '-' + str[i], i + 1)
    getSolutions(s1 + str[i], i + 1)
getSolutions('', 0)
