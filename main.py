# controller в кот соединяются все модули
import view
import logic
import Util

def main():
    while True:
        size = int(input("Input size of list: "))
        if size > 0:
            break
        else:
            view.write("Error. User data was invalid.")

    ls = Util.create_list(size)

    # random_ init_list(ls) # элементы списка создаются рандомно
    Util.user_init_list(ls) # юзер вручную заполняет элеменеты списка

    second = logic.find_second_max_value(ls)
    view.write(ls)
    msg = f"Second max value is {second}"

    view.write(msg)

if __name__ == "__main__":
    main()