name= input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")

        print("Slytherin")
    case _:
        print("Who?")