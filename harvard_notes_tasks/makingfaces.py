# ัreat a convert thing
# creat a main


def convert(argument):
    argument = argument.replace("c:", "๐").replace(":c", "๐")
    print(argument)


def main():
    sentence = input("")
    convert(sentence)


main()
