def statement_generator(statement, decoration, lines=None):

    sides = decoration * 1

    statement = f"{sides}{statement}{sides}"
    if lines == 4:
        top_bottom = decoration * 4
        print(top_bottom)
        print(statement)
        print(top_bottom)
    else:
        statement = f"{decoration * 5} {statement} {decoration * 5}"
        print(statement)

    return ""


statement_generator("    Welcome to the Lucky Unicorn Game    ",
                    "(👉ﾟヮﾟ)👉👈(ﾟヮﾟ👈))", 4)
print()
statement_generator("    Congratulations you got a Unicorn    ",
                    "(^///^)(^///^)(^///^)", 4)

statement_generator("  You got a donkey  ", "D")
