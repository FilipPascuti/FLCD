from domain.scanner import Scanner

def main():
    scanner = Scanner(filename="lab3/input/token.in")

    pif, identifier_table, constant_table, error_message = scanner.scan(problem_file="lab3/input/p2.txt")

    with open("lab3/output/pif.out", "w") as file:
        file.write(str(pif))

    with open("lab3/output/st_id.out", "w") as file:
        file.write(str(identifier_table))

    with open("lab3/output/st_const.out", "w") as file:
        file.write(str(constant_table))

    if error_message:
        print(error_message)
    else:
        print("Lexically correct")

if __name__ == '__main__':
    main()
