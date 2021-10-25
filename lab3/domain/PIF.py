class PIF:
    def __init__(self) -> None:
        self.__table = []

    def add(self, token, position):
        self.__table.append((token, position))

    def __str__(self) -> str:
        result = ""

        for pair in self.__table:
            result += '[' + pair[0] + ":" + str(pair[1]) + "]\n"

        return result
