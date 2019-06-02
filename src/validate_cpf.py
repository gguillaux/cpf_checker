class CPF:
    def __init__(self, cpf_number):
        self.cpf = cpf_number
        self.cpf_clean = self.__clean_cpf()
        self.first_digit = None
        self.second_digit = None
        self.is_valid = self.__is_valid()

    def __clean_cpf(self):
        # TODO function to clean CPF by removing . and - chars
        return None

    def __is_valid(self):
        return None

if __name__ == "__main__":
    # TODO read txt file with test cases and parse each cpf
    pass