class CPF:
    def __init__(self, cpf_number):
        self.cpf = cpf_number
        self.__clean = self.__clean_cpf()
        self.__proper_size = self.__has_valid_length()
        
        self.__divide()
        self.is_valid = self.__is_valid()
        

    def __clean_cpf(self):
        '''Remove non digits chars from String'''
        return ''.join(l for l in self.cpf if l.isdigit())
    
    def __has_valid_length(self):
        '''Check if cleaned String composed just by digits has 11 chars'''
        if len(self.__clean) == 11:
            return True
        else:
            return False

    def __divide(self):
        '''Define auxiliar atributes if String has 11 digits'''
        self.body = ""
        self.validation_digits = ""
        self.first_digit = ""
        self.second_digit = ""
        if self.__proper_size:
            self.body = self.__clean[:9]
            self.validation_digits = self.__clean[9:]
            self.first_digit = int(self.validation_digits[0])
            self.second_digit = int(self.validation_digits[1])
    
    def __remainder(self, values_sum):
        '''Returns the remainder of the division by 11. If remainder == 10 returns 0'''
        remainder = values_sum % 11
        if remainder == 10:
            return 0
        else:
            return remainder

    def __is_valid(self):
        '''Returns boolean stating if CPF is valid or not'''
        self.sum1 = 0
        self.sum2 = 0
        for i, j in enumerate(self.body):
            self.sum1 += (int(j) * (i+1)) # sum of product of cpf digits and its integer
            self.sum2 += (int(j) * (9 - i)) # sum of product of difits and its reverse integer
        if (self.__remainder(self.sum1) == self.first_digit) and (self.__remainder(self.sum2) == self.second_digit):
            return True
        else:
            return False

if __name__ == "__main__":
    cpf_file_path = r'./test/cpfs.txt' # file with cpfs to be tested
    
    with open(cpf_file_path, 'r') as f:
        for i, l in enumerate(f.readlines()): # iterates over each CPF checking and each if it's valid
            cpf = CPF(l)
            print('{} - \t CPF {} \t valid = {}'.format(i + 1, cpf.cpf.strip(), cpf.is_valid))