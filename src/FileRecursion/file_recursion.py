import os


class FileRecursion:
    @staticmethod
    def find_files_with_built_in(suffix, path):
        """
        Find all files beneath path with file name suffix.

        Note that a path may contain further subdirectories
        and those subdirectories may also contain further subdirectories.

        There are no limit to the depth of the subdirectories can be.

        @param suffix: suffix if the file name to be found
        @param path: path of the file system
        @return: a list of paths
        """
        file_paths = set()
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(suffix):
                    file_paths.add(os.path.join(root, file))
        return file_paths

    def find_files(self, suffix, path):
        """
        Find all files beneath path with file name suffix.

        Note that a path may contain further subdirectories
        and those subdirectories may also contain further subdirectories.

        There are no limit to the depth of the subdirectories can be.

        Args:
          suffix(any): suffix if the file name to be found
          path(str): path of the file system

        Returns:
           a list of paths
        """
        if suffix is None or len(suffix) == 0:
            return []

        suffix = suffix.strip(".")
        found_directories = set()
        current_directories = os.listdir(path=path)

        for directory in current_directories:
            pathname = "{}\\{}".format(path, directory)

            if os.path.isdir(pathname):
                found_directories = found_directories.union(self.find_files(suffix, pathname))

            if os.path.isfile(pathname):
                _, file_suffix = directory.rsplit(".", 1)
                if file_suffix == suffix:
                    found_directories.add(pathname)

        return found_directories


fileRec = FileRecursion()
path_base = os.getcwd() + '/testdir'
# Testcase 1 built-in
print("Testcase 1 built-in")
print(fileRec.find_files_with_built_in('.c', 'testdir'))
# Testcase 2 built-in
print("Testcase 2 built-in")
print(fileRec.find_files_with_built_in('c', path_base))
# Testcase 1
print("Testcase 1")
print(fileRec.find_files(suffix='c', path=path_base))

# Testcase 2
print("Testcase 2")
print(fileRec.find_files(suffix='h', path=path_base))

# Testcase 3
print("Testcase 3")
print(fileRec.find_files(suffix='x', path=path_base))
