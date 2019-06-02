class CPF:
    def __init__(self, cpf_number):
        self.cpf = cpf_number
        self.cpf_clean = self.clean(cpf)

    def __clean_cpf(self):
        # TODO function to clean CPF by removing . and - chars

if __name__ == "__main__":
    # TODO read txt file with test cases and parse each cpf