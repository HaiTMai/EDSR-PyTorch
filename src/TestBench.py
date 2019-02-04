import imageio
import numpy 
import math
import cv2

im1 = cv2.imread('../TestBench/baby.png')
im2 = cv2.imread('../TestBench/baby_x2_SR.png')
im3 = cv2.imread('../TestBench/babyx2_zssr_X2.00X2.00.png')
im4 = cv2.imread('../TestBench/babyx2_zssr_X2.00X2.00_New.png')
im5 = cv2.imread('../TestBench/babyx2_noise_x2_SR.png')
im6 = cv2.imread('../TestBench/babyx2_zssr_X2.00X2.00_Noise.png')

def psnr(img1, img2):
    mse = numpy.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    else:
        PIXEL_MAX = 255.0
        return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

d=psnr(im1,im2)
d1=psnr(im1,im3)
d2=psnr(im1,im4)
d3=psnr(im1,im5)
d4=psnr(im1,im6)
print('\n-------------------------------------------')
print('PNSR Performance of EDSR/ZSSR        : {0:5f}/{1:5f} '.format(d,d1))
print('PNSR Performance of EDSR/EDSR+ZSSR   : {0:5f}/{1:5f} '.format(d,d2))
print('PNSR Performance of EDSR/EDSR+Noise   : {0:5f}/{1:5f} '.format(d,d3))
print('PNSR Performance of EDSR+Noise/EDSR+Noise+ZSSR   : {0:5f}/{1:5f} '.format(d3,d4))
print('-------------------------------------------\n')