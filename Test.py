import unittest
from Romano_decimal import roman_to_decimal
from decimal_romano import decimal_to_roman

class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado = roman_to_decimal('I')
        self.assertEqual(resultado, 1)
    def test_II(self):
        resultado = roman_to_decimal('II')
        self.assertEqual(resultado, 2)
    def test_III(self):
        resultado = roman_to_decimal('III')
        self.assertEqual(resultado, 3)

    def test_V(self):
        resultado = roman_to_decimal('V')
        self.assertEqual(resultado, 5)
    def test_X(self):
        resultado = roman_to_decimal('X')
        self.assertEqual(resultado, 10)
    def test_VI(self):
        resultado = roman_to_decimal('VI')
        self.assertEqual(resultado, 6)
    def test_VII(self):
        resultado = roman_to_decimal('VII')
        self.assertEqual(resultado, 7)
    def test_IV(self):
        resultado = roman_to_decimal('IV')
        self.assertEqual(resultado, 4)
    def test_IX(self):
        resultado = roman_to_decimal('IX')
        self.assertEqual(resultado, 9)
             
class TestDecimalToRoman(unittest.TestCase):

 def test_1(self):
        resultado = decimal_to_roman(1000)
        self.assertEqual(resultado, 'M')     
               
 def test_2(self):
        resultado = decimal_to_roman(900)
        self.assertEqual(resultado, 'CM')     
        
 def test_3(self):
        resultado = decimal_to_roman(500)
        self.assertEqual(resultado, 'D')     
               
 def test_4(self):
        resultado = decimal_to_roman(400)
        self.assertEqual(resultado, 'CD')     
               
 def test_5(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, 'C')     
        
 def test_6(self):
        resultado = decimal_to_roman(90)
        self.assertEqual(resultado, 'XC') 
        
 def test_7(self):
        resultado = decimal_to_roman(50)
        self.assertEqual(resultado, 'L')     
               
 def test_8(self):
        resultado = decimal_to_roman(40)
        self.assertEqual(resultado, 'XL')     
        
 def test_9(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')   
        
 def test_10(self):
        resultado = decimal_to_roman(9)
        self.assertEqual(resultado, 'IX')     
               
 def test_11(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')     
        
 def test_12(self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado, 'I') 

if __name__ == '__main__':
    unittest.main()
    
