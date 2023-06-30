##########################################################################################################

# read VOTI Detection RAW X-ray Image Files - Unsigned 16-bit Image Data; high/low dual-energy X-ray 

# Toby Breckon, Durham University, June 2023

##########################################################################################################

import mmap
import numpy as np
import os
import sys
import matplotlib.pyplot as plt

##########################################################################################################

FILENAME = sys.argv[1] 
IMAGE_WIDTH = 640
DATATYPE = np.dtype('uint16')
LINES_TO_SKIP = 30

##########################################################################################################

with open(FILENAME, 'rb') as file_in:

    # get size of file in bytes

    size_bytes = os.fstat(file_in.fileno()).st_size
    print('file size = ', size_bytes)

    # read whole file into numpy array

    m = mmap.mmap(file_in.fileno(), length=size_bytes, access=mmap.ACCESS_READ)
    buffer = np.frombuffer(m, DATATYPE, offset=(DATATYPE.itemsize * IMAGE_WIDTH * 2 * LINES_TO_SKIP))
    print('data buffer length (px) = ', buffer.shape[0])
    print()

    # reshape to 2D image of high + low X-ray image data (= twice width of X-ray image)

    image = buffer.reshape(int(buffer.shape[0] / (IMAGE_WIDTH * 2)), IMAGE_WIDTH * 2)
    print('total image data shape (H x W, px) = ', image.shape)
    print()

    # split into high and low X-ray images based on left to right order [low | high]

    low_image = image[:,0:IMAGE_WIDTH]
    high_image = image[:,IMAGE_WIDTH:(IMAGE_WIDTH *2)]

    print('low energy range = ', np.min(low_image), ' -> ', np.max(low_image))
    print('high energy range = ', np.min(high_image), ' -> ', np.max(high_image))

    # plot original data + high / low X-ray images

    fig = plt.figure()
    
    fig.add_subplot(1, 3, 1)
    plt.imshow(image)
    plt.title("Raw - colourmapped")
    plt.ylabel("belt direction ->->->")
    plt.xlabel("<-------- scan width across belt (64 x 10 samples x 2 images : high + low X-ray ) -------->")

    fig.add_subplot(1, 3, 2)
    plt.imshow(low_image, cmap='gray')
    plt.title("Low Energy - gray")
    plt.ylabel("belt direction ->->->")

    fig.add_subplot(1, 3, 3)
    plt.imshow(high_image, cmap='gray')
    plt.title("High Energy - gray")
    plt.ylabel("belt direction ->->->")

    fig.tight_layout()

    plt.show()

##########################################################################################################