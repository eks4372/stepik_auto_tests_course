import unittest
from lesson import registration


class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(registration('http://suninjuly.github.io/registration1.html'),
                         "Congratulations! You have successfully registered!", "Registration failed")

    def test_reg2(self):
        self.assertEqual(registration('http://suninjuly.github.io/registration2.html'),
                         "Congratulations! You have successfully registered!", "Registration failed")


if __name__ == "__main__":
    unittest.main()
