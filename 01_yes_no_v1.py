show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = input("Have you played this game before? ").lower()

    if show_instructions == "yes":
        print("program continues")

    elif show_instructions =="y":
        print(" program continues")

    elif show_instructions == "no":
        print("show instructions")

    elif show_instructions == "n":
        print("Show instructions")

    else:
        print("Please answer yes / no")