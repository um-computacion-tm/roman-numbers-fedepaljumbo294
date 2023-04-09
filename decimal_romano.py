import unittest
def decimal_to_roman(decimal):
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerales = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

    numeral = ""
    i = 0

    while decimal > 0:
        for j in range(decimal//numeros[i]):
            numeral += numerales[i]
            decimal -= numeros[i]
    
        i += 1
    return numeral
      
if __name__ == '__main__':
    unittest.main()
    
    