import Image
im = Image.open("logo_1.jpg")
width, height = im.size   # Get dimensions

left = (width - new_width)/2
top = (height - new_height)/2
right = (width + new_width)/2
bottom = (height + new_height)/2

im.crop((left, top, right, bottom))
