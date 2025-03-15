>>> from pillow import Image
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    from pillow import Image
ModuleNotFoundError: No module named 'pillow'
>>> def sepia(image):
...     grayscale_image = image.convert('L')
...     for y in range(image.height):
...         for x in range(image.width):
...             (r, g, b) = image.getpixel((x, y))
...             new_r = min(255, int(0.393 * r + 0.769 * g + 0.189 * b))
...             new_g = min(255, int(0.349 * r + 0.686 * g + 0.168 * b))
...             new_b = min(255, int(0.272 * r + 0.534 * g + 0.131 * b))
...             image.putpixel((x, y), (new_r, new_g, new_b))
...             return image
...
>>> input_image = Image.open(r'C:\Users\madis\Downloads\images.py\._smokey.gif')
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    input_image = Image.open(r'C:\Users\madis\Downloads\images.py\._smokey.gif')
                  ^^^^^
NameError: name 'Image' is not defined
>>> output_image = sepia(input_image.copy())
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    output_image = sepia(input_image.copy())
                         ^^^^^^^^^^^
NameError: name 'input_image' is not defined
>>> output_image.save('sepia_image.jpg')
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    output_image.save('sepia_image.jpg')
    ^^^^^^^^^^^^
NameError: name 'output_image' is not defined
>>> input_image.show()
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    input_image.show()
    ^^^^^^^^^^^
NameError: name 'input_image' is not defined
>>> output_image.show()
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    output_image.show()
    ^^^^^^^^^^^^
NameError: name 'output_image' is not defined
>>>
