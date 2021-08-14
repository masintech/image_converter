import pathlib as pl
import unittest
from image_converter import get_file_string, process_file_extention, image_convert
import os


class TestCaseBase(unittest.TestCase):
    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))


class ActualTest(TestCaseBase):
    def testFrom_heic_to_jpg(self):
        filename = "sample1.heic"
        fmt = "jpg"
        file_str = get_file_string(filename)  # filename without path
        file_name, file_ext = process_file_extention(file_str)
        image_convert(filename, fmt)
        path = pl.Path(os.path.join("./converted_imgs", file_name + "." + fmt))
        self.assertIsFile(path)

    def testFrom_heic_to_png(self):
        filename = "sample1.heic"
        fmt = "png"
        file_str = get_file_string(filename)  # filename without path
        file_name, file_ext = process_file_extention(file_str)
        image_convert(filename, fmt)
        path = pl.Path(os.path.join("./converted_imgs", file_name + "." + fmt))
        self.assertIsFile(path)

    def testFrom_jpeg_to_png(self):
        filename = "sample3.jpeg"
        fmt = "png"
        file_str = get_file_string(filename)  # filename without path
        file_name, file_ext = process_file_extention(file_str)
        image_convert(filename, fmt)
        path = pl.Path(os.path.join("./converted_imgs", file_name + "." + fmt))
        self.assertIsFile(path)

    def testFrom_jpeg_to_tiff(self):
        filename = "sample3.jpeg"
        fmt = "tiff"
        file_str = get_file_string(filename)  # filename without path
        file_name, file_ext = process_file_extention(file_str)
        image_convert(filename, fmt)
        path = pl.Path(os.path.join("./converted_imgs", file_name + "." + fmt))
        self.assertIsFile(path)

    def testFrom_png_to_jpeg(self):
        filename = "sample2.png"
        fmt = "jpeg"
        file_str = get_file_string(filename)  # filename without path
        file_name, file_ext = process_file_extention(file_str)
        image_convert(filename, fmt)
        path = pl.Path(os.path.join("./converted_imgs", file_name + "." + fmt))
        self.assertIsFile(path)

    def testFrom_png_to_bpm(self):
        filename = "sample2.png"
        fmt = "bmp"
        file_str = get_file_string(filename)  # filename without path
        file_name, file_ext = process_file_extention(file_str)
        image_convert(filename, fmt)
        path = pl.Path(os.path.join("./converted_imgs", file_name + "." + fmt))
        self.assertIsFile(path)

if __name__ == "__main__":
    unittest.main(verbosity=2)
