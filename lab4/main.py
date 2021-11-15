from domain.finite_automata import FiniteAutomata

def show_states(automata: FiniteAutomata):
    print(f"the set of states is {automata.states}\n")

def show_alphabet(automata: FiniteAutomata):
    print(f"the alphabet is {automata.alphabet}\n")

def show_transitions(automata: FiniteAutomata):
    string = ""
    for key in automata.transitions:
        for value in automata.transitions[key]:
            string += f"({key[0]},{key[1]}) -> {value}\n"
    print(string)

def show_final_states(automata: FiniteAutomata):
    print(f"the final states are {automata.final_states}\n")

def main():
    automata = FiniteAutomata.read_from_file("lab4/input/interger.txt")

    while True:
        command = input(">>> ")
        if command == "x":
            break
        elif command == "1":
            show_states(automata)
        elif command == "2":
            show_alphabet(automata)
        elif command == "3":
            show_transitions(automata)
        elif command == "4":
            show_final_states(automata)
        elif command == "5":
            sequence = input("input sequence\n")
            print(f"{automata.check_sequence(sequence)}\n")

if __name__ == "__main__":
    main()























