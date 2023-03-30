# model
def find_second_max_value(ls):
    max_value = ls[0]
    second_max_value = ls[0]

    for element in ls:  #перебирать элементы просто
        if max_value < element:
            second_max_value = max_value
            max_value = element
        elif second_max_value < element:
            second_max_value = element

    return second_max_value

if __name__ == "__main__":
    main()