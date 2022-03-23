import os
import PIL
import glob
from PIL import Image, ImageFont, ImageDraw
import time
from natsort import natsorted, ns
import random

txtX1val 	= 0
txtX2val 	= 0
imgX1val 	= 0
imgX2val 	= 0
valtop 		= 0
swapval 	= 0
swapvaltxt	= 0
fontsz 		= 0
dstfrtop 	= 0

# This is the main function of the code.
def proxi(direct, savedir, alphapath, side, cordimg, txtsize, rbgval, txtcord):

	#define variables

	alpha 		= alphapath
	centrorl	= side
	fontsz 		= txtsize
	count 		= 0

	#Read input from line and assign variables
	txtX1val, txtX2val ,dstfrtop	= str(txtcord).strip().split(',')
	imgX1val, imgX2val ,valtop 		= str(cordimg).strip().split(',')
	R, G, B 						= str(rbgval).strip().split(',')

	lst 	= os.listdir(direct)
	dirlist = natsorted(lst, alg=ns.PATH | ns.IGNORECASE)

	#forevery file in the specified path folder convert the image depending on what side was specified.
	print("Starting process...\n")

	#will center your images to the right
	if((centrorl == "r") or (centrorl == "R")):
		swapval = int(imgX2val)
		swapvaltxt = int(txtX2val)
		im1 = Image.open(alpha)

		for filename in dirlist:

			im2 = Image.open(direct+"\\"+filename)
			print("Working on image: "+filename)

			back_im = im1.copy()
			back_im.paste(im2, (swapval, int(valtop)))
			num_font = ImageFont.truetype('agencyr.ttf', int(fontsz))

			numstr = str(count)
			pnum = numstr.zfill(3)
			image_editable = ImageDraw.Draw(back_im)
			image_editable.text((int(swapvaltxt), int(dstfrtop)), pnum, (int(R), int(G), int(B)), font=num_font)
			count = count+1
			back_im.save(savedir+"\\"+filename)

			#switch sides
			time.sleep(.3)
			if (swapvaltxt == int(txtX1val)):
				swapvaltxt = int(txtX2val)
			elif (swapvaltxt == int(txtX2val)):
				swapvaltxt = int(txtX1val)
			if (swapval == int(imgX2val)):
				swapval = int(imgX1val)
			elif (swapval == int(imgX1val)):
				swapval = int(imgX2val)







	#will center the images to the left
	elif((centrorl) == "l" or (centrorl == "L")):
		swapval = int(imgX1val)
		swapvaltxt = int(txtX1val)
		im1 = Image.open(alpha)

		for filename in dirlist:

			im2 = Image.open(direct+"\\"+filename)
			print("Working on image: "+filename)

			back_im = im1.copy()
			back_im.paste(im2, (swapval, int(valtop)))
			num_font = ImageFont.truetype('agencyr.ttf', fontsz)

			numstr = str(count)
			pnum = numstr.zfill(3)
			image_editable = ImageDraw.Draw(back_im)
			image_editable.text((int(swapvaltxt), int(dstfrtop)), pnum, (int(R), int(G), int(B)), font=num_font)
			count = count+1
			back_im.save(savedir+"\\"+filename)

			#switch sides
			time.sleep(.3)
			if (swapvaltxt == int(txtX1val)):
				swapvaltxt = int(txtX2val)
			elif (swapvaltxt == int(txtX2val)):
				swapvaltxt = int(txtX1val)
			if (swapval == int(imgX1val)):
				swapval = int(imgX2val)
			elif (swapval == int(imgX2val)):
				swapval = int(imgX1val)





def preview(direct, alphapath, side, cordimg, txtsize, rbgval, txtcord):

	alpha 		= alphapath
	centrorl	= side
	fontsz 		= txtsize
	count 		= 0

	imgX1val, imgX2val ,valtop 		= str(cordimg).strip().split(',')
	txtX1val, txtX2val ,dstfrtop 	= str(txtcord).strip().split(',')
	R, G, B 						= str(rbgval).strip().split(',')

	filename = random.choice(os.listdir(direct))

	if((side) == "l" or (side == "L")):
		swapval = int(imgX1val)
		swapvaltxt = int(txtX1val)
	else:
		swapval = int(imgX2val)
		swapvaltxt = int(txtX2val)

	#Selects one image, processes it, and shows it to the user.
	im1 = Image.open(alpha)
	im2 = Image.open(direct+"\\"+filename)

	back_im = im1.copy()
	back_im.paste(im2, (swapval, int(valtop)))
	num_font = ImageFont.truetype('agencyr.ttf', int(fontsz))

	numstr = str(count)
	pnum = numstr.zfill(3)
	image_editable = ImageDraw.Draw(back_im)
	image_editable.text((swapvaltxt, int(dstfrtop)), pnum, (int(R), int(G), int(B)), font=num_font)
	count = count+1
	back_im.show()