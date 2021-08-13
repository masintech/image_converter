import os
import argparse
from PIL import Image
import sys


def get_args():
    parser = argparse.ArgumentParser(description="Please list the file and format")
    parser.add_argument(
        "-f", "--filename", nargs="+",  default=[],
        required=True, help="The image file you want to convert"
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


def image_convert(file, fmt):
    if file[-4:] == "HEIC" or file[-4:] == "heic":
        import pyheif as heif
        heif_read = heif.read(file)
        img = Image.frombytes(
            heif_read.mode,
            heif_read.size,
            heif_read.data,
            "raw",
            heif_read.mode,
            heif_read.stride,
        )
        try:
            os.mkdir('converted_imgs')
        except OSError as error:
            print(error)
        img.save(os.path.join("./converted_imgs" ,os.path.splitext(file)[0] + '.' + fmt))
    else:
        img = Image.open(file)
        try:
            os.mkdir('converted_imgs')
        except OSError as error:
            print(error)
        img.save(os.path.join("./converted_imgs" ,os.path.splitext(file)[0] + '.' + fmt))


def main():
    args = get_args()
    for name in args.filename:
        image_convert(name, args.format)


if __name__ == "__main__":
    main()
