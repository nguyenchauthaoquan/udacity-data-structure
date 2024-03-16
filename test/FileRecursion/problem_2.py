import os
import unittest

from src.FileRecursion.file_recursion import FileRecursion


class MyTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        """
        Initialize the test class
        """
        super(MyTestCase, self).__init__(*args, **kwargs)
        self.file_rec = FileRecursion()
        self.path = os.getcwd() + '/testdir'

    def test_edge_case_1(self):
        """
        Tests the File Recursion with the auto-generated path
        """
        self.assertEqual(self.file_rec.find_files(suffix='a', path=self.path), set())

    def test_edge_case_2(self):
        """
        Tests the File Recursion for relative file path case
        """
        self.assertEqual(self.file_rec.find_files(suffix='c', path='./testdir'), {'./testdir\\subdir1\\a.c',
                                                                                  './testdir\\subdir3\\subsubdir1\\b.c',
                                                                                  './testdir\\subdir5\\a.c',
                                                                                  './testdir\\t1.c'})

    def test_edge_case_3(self):
        """
        Tests the File Recursion for relative file path case
        """
        self.assertEqual(self.file_rec.find_files(suffix='h', path='./testdir'), {'./testdir\\subdir1\\a.h',
                                                                                  './testdir\\subdir3\\subsubdir1\\b.h',
                                                                                  './testdir\\subdir5\\a.h',
                                                                                  './testdir\\t1.h'})

    def test_empty_suffix_case_1(self):
        """
        Tests the File Recursion for empty suffix
        """
        self.assertEqual(self.file_rec.find_files(suffix='', path=self.path), [])

    def test_file_not_found_case_1(self):
        """
        Tests the File Recursion for file not found
        """
        with self.assertRaises(FileNotFoundError):
            self.file_rec.find_files(suffix='c', path="./abcd")


if __name__ == '__main__':
    unittest.main()
