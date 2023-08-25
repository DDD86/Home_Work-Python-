import csv

def show_menu():
    print("\nТелефонный справочник. Введите нужную цифру в соответствии с опцией.")
    print("\n1. Распечатать справочник\n"
          "2. Найти телефон по фамилии\n"
          "3. Изменить номер телефона\n"
          "4. Удалить запись\n"
          "5. Найти абонента по номеру телефона\n"
          "6. Добавить абонента в справочник\n"
          "7. Закончить работу")
    choice = int(input())
    return choice


def print_phonebook(phonebook):
    file = open(phonebook, mode="r", encoding="utf-8")
    print("-" * 45)
    print("Список всех абонентов: \n")
    print(file.read())
    print("-" * 45)
    file.close()
    

def find_numbers_by_lastname():
    last_name = input("Введите фамилию: ")
    found = False
    found_numbers = []

    with open("phonebook.csv", mode="r", encoding="utf-8") as file:
        found_numbers = {}
        reader = csv.reader(file)
        for row in reader:
            if last_name == row[0]:
                found_numbers[row[1]] = row[2]
                found = True

    if found:
        print(f"Найдены номера телефона для абонента {last_name}: {found_numbers}")
    else:
        print(f"Абонент с фамилией {last_name} не найден!")


def change_number():
    with open("phonebook.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        data = list(reader)

    the_same_last_names = []
    last_name = input("Введите фамилию абонента, чей номер нужно изменить: ")
    for row in data:
        if last_name == row[0]:
            the_same_last_names.append(row[1])
    
    if len(the_same_last_names) > 1:
        print(f"В базе есть {len(the_same_last_names)} абонента(ов) с данной фамилией: {the_same_last_names}")
        first_name = input("Введите имя абонента: ")

        found = False

        for row in data:
            if last_name == row[0] and first_name.strip() == row[1].strip():
                print("Найдено:", row[0], row[1])
                new_number = input("Введите новый номер: ")
                row[2] = new_number
                found = True

        if found:
            with open("phonebook.csv", "w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(data)
            print("Данные успешно обновлены.")
        else:
            print("Абонент не найден.")
    elif len(the_same_last_names) == 1:
        first_name = the_same_last_names[0]
        new_number = input("Введите новый номер: ")
        found = False

        for row in data:
            if last_name == row[0] and first_name.strip() == row[1].strip():
                print("Найдено:", row[0], row[1])
                row[2] = new_number
                found = True

        if found:
            with open("phonebook.csv", "w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(data)
            print("Данные успешно обновлены.")
        else:
            print("Абонент не найден.")
    else:
        print("Абонент не найден.")

                  
def delete_entry_by_lastname_and_firstname():
    last_name_to_delete = input("Введите фамилию: ")
    first_name = input("Введите имя абонента: ")

    with open("phonebook.csv", mode="r", encoding="utf-8") as file:
        lines = file.readlines()

    new_lines = []
    deleted = False
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) >= 2:
            saved_last_name, saved_first_name = parts[0].strip(), parts[1].strip()
            if last_name_to_delete == saved_last_name and first_name == saved_first_name:
                deleted = True
            else:
                new_lines.append(line)

    if not deleted:
        print(f"Абонент с фамилией {last_name_to_delete} и именем {first_name} не найден.")
    else:
        with open("phonebook.csv", mode="w", encoding="utf-8") as file:
            file.writelines(new_lines)
            print(f"Абонент с фамилией {last_name_to_delete} и именем {first_name} удален.")
     

def find_user_by_number():
    phone_number = input("Введите номер телефона абонента: ")
    found = False  
    with open("phonebook.csv", mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if phone_number == row[2].lstrip():
                print(row)
                found = True
                break  
    if not found:
        print("Такого номера нет!")          


def add_entry_to_phonebook():

    with open("phonebook.csv", mode="r", encoding="utf-8") as file:
        lines = file.readlines()

    last_name = input("Введите фамилию: ")
    name = input("Введите имя: ")  
    phone_number = input("Введите номер телефона: ")  
    extra = input("Введите описание: ")    

    for line in lines:
        if last_name in lines:
            print(f"Абонент с фамилией {last_name} уже существует.")
            return

    new_entry = f"{last_name}, {name}, {phone_number}, {extra}\n"

    with open("phonebook.csv", mode="a", encoding="utf-8") as file:
        file.write(new_entry)

    print(f"Абонент {last_name} {name} добавлен в справочник с номером {phone_number}.")


def operation_with_phonebook():
    choice = show_menu()

    while choice != 7:
        if choice == 1:
            print_phonebook("phonebook.csv")
        elif choice == 2:
            find_numbers_by_lastname()
        elif choice == 3:
            change_number()
        elif choice == 4:
            delete_entry_by_lastname_and_firstname()
        elif choice == 5:
            find_user_by_number()
        elif choice == 6:
            add_entry_to_phonebook()
        else:
            print("Некорректный выбор")

        choice = show_menu()


with open("phonebook.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    data = list(reader)

data.sort(key=lambda x: x[0])

with open("phonebook.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

operation_with_phonebook()