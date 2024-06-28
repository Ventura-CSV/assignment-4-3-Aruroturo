def main():
    number = int(input('Enter your input: '))
    result = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    while number > 0:
        Camerino = number % 2
        result.append(Camerino)
        number = number // 2
    result.reverse()
    print(*result)
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
