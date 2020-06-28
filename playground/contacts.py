#  Contact program
import string

name = []
phone_num = []


def collect_info():
    name_input, phone_num_input = input("Enter your name: "), input("Enter your phone number: ")
    if name_input == "" or phone_num_input == "":
        print("You have entered invalid data!")
        collect_info()
    for i in phone_num_input:
        if i in string.ascii_letters:
            print("You have entered an invalid phone number!\n"
                  "Please start over!")
            return collect_info()

    name.append(name_input)
    phone_num.append(phone_num_input)

    ask = input("Do you want to add another number? yes|no: ")

    if ask == "yes":
        collect_info()
    else:
        pass


collect_info()


def search(name_of_contact):
    if name_of_contact in name:
        print(f"Found!")
        print(f"Here's the phone number: {phone_num[name.index(name_of_contact)]}")
    else:
        print(f"Not in list")

# search(input("Who do you want to search for?"))
