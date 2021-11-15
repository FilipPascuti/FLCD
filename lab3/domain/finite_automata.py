from typing import final
from collections import defaultdict

class FiniteAutomata:
    def __init__(self, states=[], alphabet=[], initial_state="", final_states=[], transitions={}, transitions_by_value={}) -> None:
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions

    @staticmethod
    def read_from_file(filename):
        with open(filename, "r") as file:
            states = file.readline().strip().split(",")
            alphabet = file.readline().strip().split(",")
            initial_state = file.readline().strip()
            final_states = file.readline().strip().split(",")
            transitions = defaultdict(list)
            for line in file:
                current_state, value = line.split("->")[0].strip().split(",")
                value = value.strip()
                next_state = line.split("->")[1].strip()
                transitions[(current_state, value)].append(next_state)

            return FiniteAutomata(states, alphabet, initial_state, final_states, transitions)

    def check_dfa(self):
        for values in self.transitions.values():
            if len(values) > 1:
                return False
        return True
        
    def check_sequence(self, sequence):
        if len(sequence) == 0 and self.initial_state not in self.final_states:
            return False
        elif len(sequence) == 0:
            return True
        
        current_state = self.initial_state

        for symbol in sequence:
            if (current_state, symbol) not in self.transitions:
                return False
            current_state = self.transitions[(current_state, symbol)][0]
        
        return current_state in self.final_states
        
    def __str__(self) -> str:
        return f"""        
            set of states: {self.states}
            alphabet: {self.alphabet}
            initial state: {self.initial_state}
            final states: {self.final_states}
            transitions: {self.transitions}
            """

class Transition:
    def __init__(self, current_state, value, next_state) -> None:
        self.current_state = current_state
        self.value = value
        self.next_state = next_state

    def __str__(self) -> str:
        return f"({self.current_state},{self.value}) -> {self.next_state}\n"











