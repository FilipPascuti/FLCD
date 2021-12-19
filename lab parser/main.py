from grammar import Grammar
from recursive_descendent import RecursiveDescendent

def main():
    grammar = Grammar()
    grammar.read_grammar("g1.txt")

    rd = RecursiveDescendent(grammar, "aacbc", False)

    productions, result = rd.start()

    print(result)
    if result == "success":
        print(productions)

if __name__ == "__main__":
    main()
