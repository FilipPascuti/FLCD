from grammar import Grammar
from recursive_descendent import RecursiveDescendent

def process_line(line):
    left, _ = line.strip().split(":")
    return left[1:]


def get_pif_out():
    pif_out = []
    with open("input/pif.out", "r") as file:
        for line in file.readlines():
            pif_out.append(process_line(line)) 
    return pif_out


def get_sequence():
    with open("input/seq.txt", "r") as file:
        line = file.readline()
        sequence = line.strip().split()
    return sequence

def write_tree_to_file(tree):
    with open("output/out2.txt", "w") as file:
        file.write("index label parent sibling\n")
        for elem in tree:
            file.write(f"{elem[0]} {elem[1]} {elem[2]} {elem[3]}\n")

def main():
    grammar = Grammar()
    grammar.read_grammar("g2.txt")

    sequence = get_pif_out()
    # sequence = get_sequence()
    # print(sequence)

    rd = RecursiveDescendent(grammar, sequence, False)

    parsing_tree, result = rd.start()

    print(result)
    if result == "success":
        print(parsing_tree)
        # write_tree_to_file(parsing_tree)


if __name__ == "__main__":
    main()
