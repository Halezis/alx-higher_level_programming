#!/usr/bin/python3
import unittest
Rectangle = __import__("rectangle").Rectangle
Base = __import__("base").Base

class TestRectangle(unittest.TestCase):
    
    def test_normal_use(self):
        self.assertTrue(Rectangle(2, 5))
        self.assertTrue(Rectangle(10, 2))
        self.assertEqual(Rectangle(2, 5).area(), 10)
        self.assertEqual(Rectangle(2, 5, 0, 0, 12).area(), 10)
        self.assertTrue(Rectangle(2, 10, 0, 0, 3))

    def test_error(self):
        self.assertRaises(TypeError, Rectangle, ("two", 5))
        self.assertRaises(TypeError, Rectangle, (5, "two"))
        self.assertRaises(TypeError, Rectangle, (True, 5))
        self.assertRaises(TypeError, Rectangle, (-3, 5))
        self.assertRaises(TypeError, Rectangle, (9, 5, 1, True, 12))
        self.assertRaises(TypeError, Rectangle, (9, 5, 1, -3, 12))
        self.assertRaises(TypeError, Rectangle, (9, 5, 1, 12))
        self.assertRaises(IndexError, Rectangle.update(), (9, 5, 1, 12, 6, 7))

if __name__ == "__main__":
    unittest.main()
