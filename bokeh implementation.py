import cv2
from PIL import Image, ImageDraw
import numpy as np
import scipy.signal as sg
y=150
x=400
h=450
w=400
img = cv2.imread("image-test3.jpg")

crop_img = img[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)
cv2.imshow("without crop", img)

img22 = cv2.blur(img,(5,5))
#cv2.imshow("with blur", img2)
img22[y:y+h, x:x+w]=crop_img
cv2.imshow("final", img22)


# import tensorflow as tf

# #tf.executing_eagerly()

# img = tf.compat.v2.random.normal(tf.float32(img),dtype=tf.float32) # replace with your image data

# grad_components = tf.image.sobel_edges(img)

# grad_mag_components = grad_components**2

# grad_mag_square = tf.math.reduce_sum(grad_mag_components,axis=-1) # sum all magnitude components

# grad_mag_img = tf.sqrt(grad_mag_square) # this is the image tensor you want

# print(grad_mag_img.shape())

cv2.waitKey(0)
