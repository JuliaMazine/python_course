import os
import unittest
import shutil

def create_directory_and_file(path):
    try:
        os.makedirs(path)
        file_path = os.path.join(path, "unittest.txt")
        with open(file_path, "w") as f:
            f.write("some text")

    except OSError:
        print(f" couldn't create the directory {path}, sorry")

class test_create_directory_and_file(unittest.TestCase):
    def setUp(self):
        self.dir_path = 'C:\\Users\\jmazi\\OneDrive\\Desktop\\New folder'
        create_directory_and_file(self.dir_path)

    def test_file_content(self):
        file_path = os.path.join(self.dir_path, 'unittest.txt')
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn('some text', content)

    def tearDown(self):
        shutil.rmtree(self.dir_path)

if __name__ == '__main__':
    unittest.main()









