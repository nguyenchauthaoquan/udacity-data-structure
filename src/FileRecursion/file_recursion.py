import os


class FileRecursion:
    def find_files_with_built_in(self, suffix, path):
        file_paths = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(suffix):
                    file_paths.append(file)
        return file_paths

    def find_files(self, suffix, path):
        """
        Find all files beneath path with file name suffix.

        Note that a path may contain further subdirectories
        and those subdirectories may also contain further subdirectories.

        There are no limit to the depth of the subdirectories can be.

        Args:
          suffix(str): suffix if the file name to be found
          path(str): path of the file system

        Returns:
           a list of paths
        """
        if len(suffix) == 0 or len(os.listdir(path=path)) == 0:
            return []

        file_paths = [file_path for file_path in os.listdir(path=path) if ('.' + suffix) in file_path]
        folder_paths = [folder for folder in os.listdir(path=path) if '.' not in folder]

        for folder in folder_paths:
            file_paths.extend(self.find_files(suffix=suffix, path=path + '/' + folder))

        return file_paths


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
