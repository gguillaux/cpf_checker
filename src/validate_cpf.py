class CPF:
    def __init__(self, cpf_number):
        self.cpf = cpf_number
        self.__clean = self.__clean_cpf()
        self.__proper_size = self.__has_valid_length()
        self.body = ""
        self.validation_digits = ""
        self.first_digit = ""
        self.second_digit = ""
        self.is_valid = self.__is_valid()

        self.__divide()

    def __clean_cpf(self):
        return ''.join(l for l in self.cpf if l.isdigit())
    
    def __has_valid_length(self):
        if len(self.__clean) == 11:
            return True
        else:
            return False

    def __divide(self):
        if self.__proper_size:
            self.body = self.__clean[:9]
            self.validation_digits = self.__clean[9:]
            self.first_digit = self.validation_digits[0]
            self.second_digit = self.validation_digits[1]

    def __is_valid(self):
        return False

if __name__ == "__main__":
    
    cpf_file_path = r'./test/cpfs.txt'
    with open(cpf_file_path, 'r') as f:
        for i, l in enumerate(f.readlines()):
            cpf = CPF(l)
            print('{} - \t {}'.format(i, cpf.clean))