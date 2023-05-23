####################################################
# NEEF 2022                                        #
#                                                  #
# Colocar Logos de Forma automática numa imagem    #
#                                                  # 
# João Maria Machado - 10/2022                     #
####################################################


from PIL import Image
import os 
import PIL 
import glob
import cv2
import numpy as np
import math
import sys


def watermark_with_transparency(input_image_path,
                                output_image_path,
                                watermark_image_path,
                                position,alpha):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    watermark=watermark.resize((math.ceil(100*alpha),math.ceil(50*alpha)))
    width, height = base_image.size
    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.show()
    transparent.save(output_image_path)

def bottom_left(image,logo,alpha,displace):

    im = Image.open(image)
    width, height = im.size

    im2 = Image.open(logo)
    im2=im2.resize((math.ceil(100*alpha),math.ceil(50*alpha)))
    width1, height1 = im2.size
    print(width-width1,height-height1)
    return width-width1-displace[1],height-height1-displace[1]

if __name__ == '__main__':

    if len(sys.argv)!=4:
        print(" Tens de me dizer o nome da imagem em que queres meter os logos e dos logos em .png (de preferência)")
        print(" Tenta assim:")
        print("\n \t python3  autoLogo.py Imagem_sem_Logos.jpeg  logos_pre_feitos.png alpha \n")
        print(" O parâmetro Alpha aumenta ou diminui o seu tamanho para que possas ajustar ao tamanho da imagem")

    if len(sys.argv)==4:
        img=str(sys.argv[1])
        logo=str(sys.argv[2])
        alpha=float(sys.argv[3])

        img_out=img.replace(".png", "")+"comLogo.png"

        im2 = Image.open(logo)
        im = Image.open(img)

        if  im.size == () or  im2.size == () :
        # Fizeste merda a ler as imagens
            print("Image file could not be open!")
            exit(-1)

        displace=[5,5]  #afasta os logos da extemidade da imagem 
        watermark_with_transparency(img, img_out,logo, position=bottom_left(img,logo,alpha,displace),alpha=alpha)