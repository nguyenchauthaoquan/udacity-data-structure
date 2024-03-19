import os
import unittest

from src.FileRecursion.file_recursion import FileRecursion


class MyTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        """
        Initialize the testing class
        """
        super(MyTestCase, self).__init__(*args, **kwargs)
        self.file_rec = FileRecursion()
        self.absolute_path = os.getcwd() + '/testdir'
        self.relative_path = './testdir'

    def test_edge_case_1(self):
        """
        Tests the File Recursion for absolute file path case in case suffix does not exist
        """
        self.assertEqual(self.file_rec.find_files(suffix='a', path=self.absolute_path), set())

    def test_edge_case_2(self):
        """
        Test the file recursion for absolute path in case suffix exists
        """
        self.assertEqual(self.file_rec.find_files(suffix='c', path=self.absolute_path),
                         {os.getcwd() + '/testdir\\subdir1\\a.c',
                          os.getcwd() + '/testdir\\subdir3\\subsubdir1\\b.c',
                          os.getcwd() + '/testdir\\subdir5\\a.c',
                          os.getcwd() + '/testdir\\t1.c'})

    def test_edge_case_3(self):
        """
         Tests the File Recursion for absolute file path in case suffix exists
        """
        self.assertEqual(self.file_rec.find_files(suffix='h', path=self.absolute_path),
                         {os.getcwd() + '/testdir\\subdir1\\a.h',
                          os.getcwd() + '/testdir\\subdir3\\subsubdir1\\b.h',
                          os.getcwd() + '/testdir\\subdir5\\a.h',
                          os.getcwd() + '/testdir\\t1.h'})

    def test_edge_case_4(self):
        """
        Tests the File Recursion for relative file path in case suffix does not exist
        """
        self.assertEqual(self.file_rec.find_files(suffix='a', path=self.relative_path), set())

    def test_edge_case_5(self):
        """
        Tests the File Recursion for relative file path in case suffix exists
        """
        self.assertEqual(self.file_rec.find_files(suffix='c', path=self.relative_path),
                         {'./testdir\\subdir1\\a.c',
                          './testdir\\subdir3\\subsubdir1\\b.c',
                          './testdir\\subdir5\\a.c',
                          './testdir\\t1.c'})

    def test_edge_case_6(self):
        """
        Tests the File Recursion for relative file path in case suffix exists
        """
        self.assertEqual(self.file_rec.find_files(suffix='h', path=self.relative_path),
                         {'./testdir\\subdir1\\a.h',
                          './testdir\\subdir3\\subsubdir1\\b.h',
                          './testdir\\subdir5\\a.h',
                          './testdir\\t1.h'})

    def test_edge_case_7(self):
        """
         Tests the File Recursion for relative file path equals to built-in solution
        """
        self.assertEqual(self.file_rec.find_files(suffix='h', path=self.absolute_path),
                         self.file_rec.find_files_with_built_in(suffix='h', path=self.absolute_path))

    def test_edge_case_8(self):
        """
        Tests the File Recursion for absolute file path equals to built-in solution
        """
        self.assertEqual(self.file_rec.find_files(suffix='c', path=self.absolute_path),
                         self.file_rec.find_files_with_built_in(suffix='c', path=self.absolute_path))

    def test_edge_case_9(self):
        """
         Tests the File Recursion for absolute file path equals to built-in solution
        """
        self.assertEqual(self.file_rec.find_files(suffix='a', path=self.absolute_path),
                         self.file_rec.find_files_with_built_in(suffix='a', path=self.absolute_path))

    def test_edge_case_10(self):
        """
        Tests the File Recursion for relative file path equals to built-in solution
        """
        self.assertEqual(self.file_rec.find_files(suffix='h', path=self.relative_path),
                         self.file_rec.find_files_with_built_in(suffix='h', path=self.relative_path))

    def test_edge_case_11(self):
        """
        Tests the File Recursion for relative file path equals to built-in solution
        """
        self.assertEqual(self.file_rec.find_files(suffix='c', path=self.relative_path),
                         self.file_rec.find_files_with_built_in(suffix='c', path=self.relative_path))

    def test_edge_case_12(self):
        """
        Tests the File Recursion for relative file path equals to built-in solution
        """
        self.assertEqual(self.file_rec.find_files(suffix='a', path=self.relative_path),
                         self.file_rec.find_files_with_built_in(suffix='a', path=self.relative_path))

    def test_empty_suffix_case_1(self):
        """
        Tests the File Recursion for empty suffix with absolute path.
        """
        self.assertEqual(self.file_rec.find_files(suffix='', path=self.absolute_path), [])

    def test_empty_suffix_case_2(self):
        """
        Tests the File Recursion for empty suffix with relative path.
        """
        self.assertEqual(self.file_rec.find_files(suffix='', path=self.relative_path), [])

    def test_null_suffix_case_1(self):
        """
        Tests the File Recursion for empty suffix with relative path.
        """
        self.assertEqual(self.file_rec.find_files(suffix=None, path=self.relative_path), [])

    def test_null_suffix_case_2(self):
        """
        Tests the File Recursion for empty suffix with absolute path.
        """
        self.assertEqual(self.file_rec.find_files(suffix=None, path=self.absolute_path), [])

    def test_file_not_found_case_1(self):
        """
        Tests the File Recursion for file not found with relative directory
        """
        with self.assertRaises(FileNotFoundError):
            self.file_rec.find_files(suffix='c', path="./abcd")

    def test_file_not_found_case_2(self):
        """
        Tests the File Recursion for file not found with absolute directory
        """
        with self.assertRaises(FileNotFoundError):
            self.file_rec.find_files(suffix='c', path=os.getcwd() + "/abcd")

    def test_file_path_empty_case_1(self):
        """
        Tests the File Recursion for file not found with relative directory
        """
        with self.assertRaises(FileNotFoundError):
            self.file_rec.find_files(suffix='c', path='')

    def test_file_path_empty_case_2(self):
        """
        Tests the File Recursion for file not found with absolute directory
        """
        with self.assertRaises(FileNotFoundError):
            self.file_rec.find_files(suffix='c', path='')


if __name__ == '__main__':
    unittest.main()
