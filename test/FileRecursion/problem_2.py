import os
import unittest

from src.FileRecursion.FileRecursion import FileRecursion


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
        self.assertEqual(self.file_rec.find_files(suffix='c', path=self.path), ['t1.c', 'a.c', 'b.c', 'a.c'])

    def test_edge_case_2(self):
        """
        Tests the File Recursion with the auto-generated path
        """
        self.assertEqual(self.file_rec.find_files(suffix='h', path=self.path), ['t1.h', 'a.h', 'b.h', 'a.h'])

    def test_edge_case_3(self):
        """
        Tests the File Recursion with the auto-generated path
        """
        self.assertEqual(self.file_rec.find_files(suffix='a', path=self.path), [])

    def test_edge_case_4(self):
        """
        Tests the File Recursion whether the manual implementation is as same as built-in calling
        """
        self.assertEqual(self.file_rec.find_files(suffix='c', path=self.path),
                         self.file_rec.find_files_with_built_in(suffix='c', path=self.path))

    def test_edge_case_5(self):
        """
        Tests the File Recursion whether the manual implementation is as same as built-in calling
        """
        self.assertEqual(self.file_rec.find_files(suffix='h', path=self.path),
                         self.file_rec.find_files_with_built_in(suffix='h', path=self.path))

    def test_edge_case_6(self):
        """
        Tests the File Recursion whether the manual implementation is as same as built-in calling
        """
        self.assertEqual(self.file_rec.find_files(suffix='a', path=self.path),
                         self.file_rec.find_files_with_built_in(suffix='a', path=self.path))

    def test_edge_case_7(self):
        """
        Tests the File Recursion for relative file path case
        """
        self.assertEqual(self.file_rec.find_files(suffix='c', path='./testdir'), ['t1.c', 'a.c', 'b.c', 'a.c'])

    def test_edge_case_8(self):
        """
        Tests the File Recursion for relative file path case
        """
        self.assertEqual(self.file_rec.find_files(suffix='h', path='./testdir'), ['t1.h', 'a.h', 'b.h', 'a.h'])

    def test_edge_case_9(self):
        """
        Tests the File Recursion for absolute file path case
        """
        self.assertEqual(self.file_rec.find_files(suffix='c', path='D:/udacity/udacity-data-structure/test'
                                                                   '/FileRecursion/testdir'), ['t1.c', 'a.c', 'b.c',
                                                                                               'a.c'])

    def test_edge_case_10(self):
        """
        Tests the File Recursion for absolute file path case
        """
        self.assertEqual(self.file_rec.find_files(suffix='h', path='D:/udacity/udacity-data-structure/test'
                                                                   '/FileRecursion/testdir'), ['t1.h', 'a.h', 'b.h',
                                                                                               'a.h'])


if __name__ == '__main__':
    unittest.main()
