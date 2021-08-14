import os
import argparse
from PIL import Image


def get_args():
    parser = argparse.ArgumentParser(description="Please list the file and format")
    parser.add_argument(
        "-f",
        "--filename",
        nargs="+",
        default=[],
        required=True,
        help="The image file you want to convert",
    )
    parser.add_argument(
        "-fmt",
        "--format",
        default="jpg",
        required=True,
        help="The image format you want to convert to",
    )
    args = parser.parse_args()
    return args


def image_convert(filename, fmt):
    file_str = get_file_string(filename)  # filename without path
    file_name, file_ext = process_file_extention(file_str) # abc .jpg
    print(f"file_name {file_name} file_ext {file_ext}")
    if file_ext == ".HEIC" or file_ext == ".heic":
        import pyheif as heif

        heif_read = heif.read(filename)
        img = Image.frombytes(
            heif_read.mode,
            heif_read.size,
            heif_read.data,
            "raw",
            heif_read.mode,
            heif_read.stride,
        )
    else:
        img = Image.open(filename)
    # prepare path to put files in
    try:
        os.mkdir("converted_imgs")
    except OSError as error:
        print(error)
        print("just a reminder, continue")
    if fmt == 'jpg' or fmt == 'jpeg':    
        img_rgb = img.convert('RGB') # JPEG does not support Alpha Channel like PNG rgba
        img_rgb.save(os.path.join("./converted_imgs", file_name + "." + fmt))
    else:
        img.save(os.path.join("./converted_imgs", file_name + "." + fmt))


def get_file_string(file_str):
    """
    extract file name that might contains its parent directory
    """
    # if the path structure is like a/b/c/abc.txt in Linux, MacOS etc.
    if os.name == "posix":
        file_name = os.path.basename(file_str)
    # otherwise, it would be like "C:\Windows\paint.exe" in Windows
    else:
        file_name = str(file_str).split("\\")[-1:][0]
    return file_name


def process_file_extention(file_str):
    """
    remove file name extension, name.exe to name
    """
    return os.path.splitext(file_str)[0], os.path.splitext(file_str)[1]


def main():
    args = get_args()
    for name in args.filename:
        image_convert(name, args.format)


if __name__ == "__main__":
    main()
