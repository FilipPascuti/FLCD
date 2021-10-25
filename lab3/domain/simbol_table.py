
class Symbol_table:

    def __init__(self, size: int) -> None:
        self.__table = [[] for i in range(size)]
        self.__size = size


    def hash_symbol(self, symbol: str) -> int:
        ascii_sum = 0

        for char in symbol:
            ascii_sum += ord(char) - ord("a")

        return ascii_sum % self.__size


    def add(self, symbol: str) -> bool:
        hash_value = self.hash_symbol(symbol)
        if self.search(symbol):
            return False
        self.__table[hash_value].append(symbol)
        return True


    def search(self, symbol: str) -> bool:
        if symbol in self.__table[self.hash_symbol(symbol)]:
            return True
        return False

    def position(self, symbol: str):
        if not self.search(symbol):
            self.add(symbol)

        hash_value = self.hash_symbol(symbol)
        return (hash_value, self.__table[hash_value].index(symbol))

    def remove(self, symbol: str) -> bool:
        if not self.search(symbol):
            return False

        hash_value = self.hash_symbol(symbol)
        self.__table[hash_value].remove(symbol)

        return True

    def __str__(self) -> str:
        return f"Simbol table of size: {self.__size} and elements: {self.__table}"
