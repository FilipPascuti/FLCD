from enum import Enum

from grammar import Grammar
from tree import LabeledTree


class State(Enum):
    NORMAL = "q"
    BACK = "b"
    FINAL = "f"
    ERROR = "e"


class RecursiveDescendent:
    def __init__(self, grammar: Grammar, sequence, logs=False) -> None:
        self.state = State.NORMAL
        self.grammar = grammar
        self.sequence = sequence
        self.position = 0
        self.working_stack = []
        self.input_stack = [grammar.get_starting_symbol()]
        self.logs = logs

    def expand(self):
        if self.logs:
            print("expand")
        non_terminal = self.input_stack[0]
        # print(non_terminal)
        production = self.grammar.productions[non_terminal][0]
        self.working_stack.append([non_terminal, 0])
        self.input_stack = production + self.input_stack[1:]

    def advance(self):
        if self.logs:
            print("advance")
        self.position += 1
        self.working_stack.append(self.input_stack[0]) 
        self.input_stack = self.input_stack[1:]

    def momentary_insuccess(self):
        if self.logs:
            print("momentary insuccess")
        self.state = State.BACK

    def back(self):
        if self.logs:
            print("back")
        self.position -= 1
        self.input_stack = [self.working_stack[-1]] + self.input_stack 
        self.working_stack.pop()

    def another_try(self):
        if self.logs:
            print("another_try")
        non_terminal, production_number = self.working_stack[-1]

        if production_number < len(self.grammar.productions[non_terminal]) - 1:
            pop_length = len(self.grammar.productions[non_terminal][production_number])
            self.input_stack = (
                    self.grammar.productions[non_terminal][production_number + 1] +
                    self.input_stack[pop_length:]
            )
            self.working_stack[-1][1] += 1
            self.state = State.NORMAL

        else:
            if self.position == 0 and non_terminal == self.grammar.get_starting_symbol():
                self.state = State.ERROR
                return

            self.working_stack.pop()
            pop_length = len(self.grammar.productions[non_terminal][production_number])
            self.input_stack = [non_terminal] + self.input_stack[pop_length:]

    def success(self):
        if self.logs:
            print("success")
        self.state = State.FINAL

    def get_production_string(self):
        production_string = ""
        for elem in self.working_stack:
            if elem in self.grammar.get_terminals():
                continue
            production_string += f"{elem[0]}{elem[1]} "
        return production_string

    def get_terminals_string(self):
        terminals_string = ""
        for elem in self.working_stack:
            if elem in self.grammar.get_terminals():
                terminals_string += f"{elem} "
        return terminals_string

    def get_productions(self):
        production_string = []
        for elem in self.working_stack:
            if elem in self.grammar.get_terminals():
                continue
            production_string.append(elem)
        return production_string

    def get_parsing_tree(self):
        built_tree = LabeledTree()

        def get_rec(node, tree, grammar):
            if self.working_stack[node] in grammar.get_terminals():
                tree.add_label(node, self.working_stack[node])
                return 1
            label, production_number = self.working_stack[node]
            tree.add_label(node, label)
            children_labels = self.grammar.productions[label][production_number]
            size = 1
            current = node + 1
            for child in range(0, len(children_labels)):
                tree.add_son(node, current)
                size += get_rec(current, tree, grammar)
                current = node + size
            return size

        get_rec(0, built_tree, self.grammar)
        return built_tree.get_table()

    def start(self):
        while self.state not in [State.FINAL, State.ERROR]:
            if self.logs:
                print(f"state {self.state}")
                print(f"position:{self.position}")
                print(f"working stack: {self.working_stack}")
                print(f"input stack: {self.input_stack}")
                print("")

            if self.state == State.NORMAL:
                if self.position == len(self.sequence) and not self.input_stack:
                    self.success()
                elif not self.input_stack:
                    self.state = State.BACK
                else:
                    if self.input_stack[0] in self.grammar.get_non_terminals():
                        self.expand()
                    else:
                        if self.position == len(self.sequence):
                            self.momentary_insuccess()
                        elif self.input_stack[0] == self.sequence[self.position]:
                            self.advance()
                        else:
                            self.momentary_insuccess()
            else:
                if self.state == State.BACK:
                    if self.working_stack[-1] in self.grammar.get_terminals():
                        self.back()
                    else:
                        self.another_try()

        if self.state == State.FINAL:
            return self.get_parsing_tree(), "success"
        else:
            return None, "error"
