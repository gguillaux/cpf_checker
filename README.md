# Check if a CPF is valid or not
This project implements in different programming languages ways to validate if a given CPF number is valid or not.

CPF means "Cadastro de Pessoa Física" and is like the social security number used by Brazilian citizens.

The test cases are stored in txt and csv files were each record is in the format 999.999.999-99

---

## CPF Composition
The CPF is composed by 11 digits that are build accordingly the below logic:
* The first **9 digits** are the actual numbers that compose the CPF code
* The last **2 digits** are used to verify the 9 first numbers.

The last 2 digits are obtained by:
1. **First digit**: sum of the product of each digit by its index, starting with 1.
   * For example, if we have have a CPF = 123.456.789 we should do: sum(1 * 1, 2 * 2, ... , 9 * 9)
   * The sum should be divided by 11 and the remainder part should be yield as the first digit
2. **Second digit**: sum of the product of each digit by its reverse index, starting with 9.
   * For example, if we have have a CPF = 123.456.789 we should do: sum(1 * 9, 2 * 8, ... , 9 * 1)
   * The sum should be divided by 11 and the remainder part should be yield as the second digit