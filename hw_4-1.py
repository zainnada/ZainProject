# Homework4 Q1
null_error = "Error, null value"
type_error = "Error, wrong value type"

input_name = input("Enter Your name: ")
if input_name.isalpha():
    input_age = input("Enter Your age: ")
    if input_age == "":
        print(null_error)
    else:
        if input_age.isdigit():
            input_address = input("Enter Your address: ")
            if input_address == "":
                print(null_error)
            else:
                print(f"Hello Mr/Ms {input_name}, age {input_age}, located in {input_address}.\n"
                      f"Thanks for being one of our community, Enjoy.")
        else:
            print(type_error)

elif input_name == "":
    print(null_error)

else:
    print(type_error)

#  Done
