def statement_generator(statement, decoration):

    sides = decoration * 1

    statement = f"{sides}{statement}{sides}"
    top_bottom = decoration * 4
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


statement_generator("    Welcome to the Lucky Unicorn Game    ",
                    "(👉ﾟヮﾟ)👉👈(ﾟヮﾟ👈))")
print()
statement_generator("    Congratulations you got a Unicorn    ",
                    "(^///^)(^///^)(^///^)")

statement_generator("You got a donkey", "D")