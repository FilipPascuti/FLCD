from domain.PIF import PIF
from domain.simbol_table import Symbol_table
from domain.finite_automata import FiniteAutomata

import re


NUMBER_OF_RESERVED_WORDS = 9
NUMBER_OF_OPERATORS = 14
NUMBER_OF_SEPARATORS = 8

class Scanner:

    def __init__(self, filename) -> None:
        self.__operators = []
        self.__separators = []
        self.__reserved_words = []

        with open(filename, "r") as file:
            for i in range(NUMBER_OF_RESERVED_WORDS):
                self.__reserved_words.append(file.readline().strip())
            for i in range(NUMBER_OF_OPERATORS):
                self.__operators.append(file.readline().strip())
            for i in range(NUMBER_OF_SEPARATORS):
                separator = file.readline().strip()
                if separator == "space":
                    separator = " "
                self.__separators.append(separator)

        self.identifier_automata = FiniteAutomata.read_from_file("lab3/input/identifier.txt")
        self.integer_constant = FiniteAutomata.read_from_file("lab3/input/interger.txt")


        # print(self.__operators, self.__separators, self.__reserved_words, sep="\n")

    def scan(self, problem_file):
        pif = PIF()
        identifier_table = Symbol_table(17)
        constant_table = Symbol_table(17)
        error_message = ""

        with open(problem_file, "r") as file:
            line_counter = 0

            for line in file.read().splitlines():
                line_counter += 1
                for token in self.__tokenize(line):
                    if token in self.__reserved_words + self.__separators + self.__operators:
                        if token == " ":
                            continue
                        pif.add(token, (-1, -1))
                    elif self.__is_identifier(token):
                        position = identifier_table.position(token)
                        pif.add("identifier", position)
                    elif self.__is_constant(token):
                        position = constant_table.position(token)
                        pif.add("constant", position)
                    else:
                        error_message += f"Lexical error at token: {token} on line: {line_counter} \n" 

        return pif, identifier_table, constant_table, error_message
    

    def __tokenize(self, line):
        token = ''
        index = 0
        tokens = []

        while index < len(line):
            if self.__is_part_of_operator(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.__get_operator_token(line, index)
                tokens.append(token)
                token = ''

            elif line[index] == '"':
                if token:
                    tokens.apend(token)
                token, index = self.__get_string_token(line, index)

            elif line[index] in self.__separators:
                if token:
                    tokens.append(token)
                token, index = line[index], index + 1
                tokens.append(token)
                token = ""

            else:
                token += line[index]
                index += 1

        if token:
            tokens.append(token)
        
        return tokens

    def __is_part_of_operator(self, character):
        for operator in self.__operators:
            if character in operator:
                return True

        return False

    def __get_operator_token(self, line, index):
        token = ''

        while index < len(line) and self.__is_part_of_operator(line[index]):
            token += line[index]
            index += 1

        return token, index

    def __get_string_token(self, line, index):
        token = ''
        quotes = 0

        while index < len(line) and quotes < 2:
            if line[index] == '"':
                quotes += 1
            token += line[index]
            index += 1

        return token, index

    def __is_identifier(self, token):
        # return re.match(r"^([a-zA-Z][a-zA-z0-9_]*)$", token) is not None
        return self.identifier_automata.check_sequence(token)

    def __is_integer_constant(self, token):
        return self.integer_constant.check_sequence(token)

    def __is_string_constant(self, token):
        return re.match(r'^"[a-zA-Z0-9_ ]*"$', token) is not None

    def __is_constant(self, token):
        # return re.match(r'^(0|[+-]?[1-9][0-9]*)$|^"[a-zA-Z0-9_ ]*"$', token) is not None
        return self.__is_integer_constant(token) or self.__is_string_constant(token)




