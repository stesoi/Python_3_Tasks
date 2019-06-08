import os

Saved = True
params = ""

def operations(filename):
    global Saved
    f = open(filename, 'r')
    lines = sorted(f.readlines())
    f.close()

    while(True):
        flags = "aq"
        if(len(lines)>0):
            flags += "d"
        print_menu(flags)
        while(True):
            choice = (input())
            if len(choice) == 0:
                print("Empty string!")
            else:
                choice = choice[0]
                if(choice.lower() not in params):
                    print("Enter one of", params)
                else:
                    break

        if(choice.lower() == 'a'): # добавление нового
            new_item = input("Add item: ")
            lines.append(new_item)
            lines = sorted(lines)
            Saved = False
            print_list(lines, "List Keeper")

        if (choice.lower() == 'd'):  # удаление
            while(True):
                try:
                    number = int(input('Delete item number (or 0 to cancel): '))
                except ValueError:
                    print("Invalid input!")
                else:
                    if(number == 0):
                        break
                    else:
                        if(number > len(lines) or number <= 0):
                            print("Out of range!")
                        else:
                            break
            if(number != 0):
                lines.pop(number-1)

        if (choice.lower() == 'q'):
            if(Saved):
                return

            while(True):
                ch = input("Save unsaved changes (y/n): ")
                if(len(ch) == 0 or len(ch) > 1 or ch.lower() not in 'yn'):
                    print("Invalid input!")
                else:
                    break

            if(ch.lower() == 'y'):
                choice = 's'
            else:
                return

        if (choice.lower() == 's'):
            counter = 0
            f = open(filename, "w")
            for line in lines:
                f.write(line)
                counter += 1
            f.close()
            print("Saved {0} items in {1}".format(counter, filename))
            Saved = True


def print_menu(flags):
    global params
    params = ""
    if 'a' in flags.lower():
        print("[A]dd ", end="")
        params += 'a'
    if 'd' in flags.lower():
        print("[D]elete ", end="")
        params += 'd'
    if not Saved:
        print("[S]ave ", end="")
        params += 's'
    if 'q' in flags.lower():
        print("[Q]uit ", end="")
        params += 'q'
    print(": ", end="")

def create_new_file():
    file_created = False
    while (not file_created):
        name = input("Enter name of the file: ")
        try:
            name = name + ".lst" if name.rfind(".lst") != (len(name)-len(".lst")) else name
            file = open(name, "tw")
            file.close()
        except Exception as err:
            print(err)
            print("Invalid name of file!")
        else:
            file_created = True

    return name

def print_list(list, message):
    print(message)
    for i in range(len(list)):
        print("\t{0}: {1}".format(i + 1, list[i]))


def choose_file(files_list):
    file_select = False
    while(not file_select):
        try:
            number = int(input("Enter number of file (or 0 to create new file):"))
        except ValueError:
            print("Invalid input!")
        else:
            try:
                a = files_list[number-1]
            except IndexError:
                if(number==0):
                    return 0
                print("Out of range!")
            else:
                file_select = True

    return number

def open_file(filename):
    try:
        f = open(filename, 'r')
    except Exception as err:
        print(err)

    file_list = []
    for line in f:
        file_list.append(line)

    if(len(file_list) == 0):
        print("--no items are in the list--")
        operations(filename)

    else:
        file_list = sorted(file_list)
        print_list(file_list, "List Keeper")
        operations(filename)

def main():
    files_list = [] # список файлов
    # сканирование файлов в текущей директории и запись нужных в список
    for file in os.listdir("."):
        if(file.find(".lst") != -1):
            files_list.append(file)

    # если файлы отсутствуют, запрашиваем у пользователя название
    if(len(files_list) == 0):
        files_list.append(create_new_file())
        files_list = sorted(files_list)

    # если были найдены файлы
    else:
        # выводим список
        files_list = sorted(files_list)
        print_list(files_list, "List of files:")
        # запрашиваем номер из списка
        c = choose_file(files_list)
        # если 0, запрашиваем новое название файла
        if (c == 0):
            files_list.append(create_new_file())
            print("No items are in the list")
        # иначе, читаем содержимое файла
        else:
            open_file(files_list[c-1])


if __name__ == "__main__":
    main()