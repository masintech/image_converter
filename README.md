# Image Converter using Python
This is a hands-on simple program to convert your image into your desired format by python  

## Usage
Like most python program, you would use them by typing in your terminal
`python3 image_converter.py --filename {filename} --format {format exe}`  
or 
`python3 image_converter.py -f {filename} -fmt {format exe}` . 

ex.  
`python3 image_converter.py -f example.HEIC -fmt jpg`    
`python3 image_converter.py -f example1.HEIC example2.png example3.jpg -fmt jpg`   
You will see your file output with new filename extension in ./converted_imgs 

## Test
Unittest for making sure the sample is ok
`python3 -m unittest test.py`  

## Support format
Common image formats such as .jpg, .png, .bpm, .tiff and HEIC are supported.  
For detailed information you can refer to the link below 
[Pillow Support Format](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html)
* Any formats converting to .HEIC is not supported


## Requirement 
Python 3.6 or later versions
1. Pillow 8.2.0 used here (other versions migh work) . 
   `python3 -m pip install --upgrade Pillow` . 
   Ref.    
   [Pillow Install Page](https://pillow.readthedocs.io/en/stable/installation.html)


2. pyheif 0.5.1 (other versions might work) .  
  `python3 -m pip install --upgrade pyheif` . 
   Ref.    
   [pyheif 0.5.1](https://pypi.org/project/pyheif/)
