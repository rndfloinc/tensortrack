from PIL import Image
im = Image.open("logo_1.jpg")

crop_rectangle = (256, 256, 768, 768)
cropped_im = im.crop(crop_rectangle)

# cropped_im.show()

cropped_im.save('cropped_0_388_image1', 'jpeg')
