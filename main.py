def arithmetic_formatter(operations, optional=""):
    temp = ""
    for i in operations:
        operation = i.split()
        term1 = operation[0]
        term2 = operation[2]
        operator = operation[1]
        operation_length = max(len(term1), len(term2)) + 2
        bigger_number = str(max(int(term1), int(term2)))
        smaller_number = str(min(int(term1), int(term2)))
        separator = ""
        for j in range(operation_length):
            separator += "-"
        small_length = operation_length - len(smaller_number)
        spaces = ""
        for h in range(small_length - 1):
            spaces += " "

        temp += "\n  " + bigger_number + "\n" + operator + spaces + smaller_number + "\n" + separator + "\n"

        if optional == "true":
            answer = str(eval(i))
            spaces = ""
            for o in range(operation_length - len(answer)):
                spaces += " "
            temp += spaces + answer + "\n"

    return temp


if __name__ == '__main__':
    print(arithmetic_formatter(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], "true"))
