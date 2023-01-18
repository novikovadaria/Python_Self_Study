# сreat a convert thing
# creat a main


def convert(argument):
    argument = argument.replace("c:", "🙂").replace(":c", "🙁")
    print(argument)


def main():
    sentence = input("")
    convert(sentence)


main()
