import os
import argparse
from PIL import Image


def get_args():
    parser = argparse.ArgumentParser(description="Please list the file and format")
    parser.add_argument(
        "-f", "--filename", required=True, help="The image file you want to convert"
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
        img.save(os.path.splitext(file)[0] + '.' + fmt)
    else:
        img = Image.open(file)
        img.save(os.path.splitext(file)[0] + '.' + fmt)


def main():
    args = get_args()
    image_convert(args.filename, args.format)


if __name__ == "__main__":
    main()
