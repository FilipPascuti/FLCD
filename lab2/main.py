from simbol_table import Symbol_table


def main():

    table = Symbol_table(17)

    print(table.add("a1"))
    print(table.add("a2"))
    print(table.add("b1"))
    print(table.add("b2"))
    print(table.add("c1"))
    print(table.add("c1"))

    print(table.position("a1"))
    print(table.position("a2"))
    print(table.position("b1"))
    print(table.position("b2"))
    print(table.position("c1"))
    print(table.position("v1"))

    print(table)

    print(table.remove("a1"))
    print(table.remove("a2"))
    print(table.remove("b1"))
    print(table.remove("b2"))
    print(table.remove("v2"))


    print(table)


if __name__ == "__main__":
    main()
