from PIL import Image
from io import BytesIO
from django.core.files import File

#RECEIVES AN IMAGE PATH AND CHANGES IMAGE SIZE
def reduce_image_size(image, new_name=None, new_quality=None, new_size=None):
    with Image.open(image) as img:
        thumb_io = BytesIO() #Later load image in bytedata. Necesary to link PIL image with django file
        
        #JPG doesn't have alfa property. For this files is necesary to convert them
        if img.mode in ("RGBA", "P"): 
            rgb_img = img.convert("RGB")
            img = rgb_img

        if new_name: #If you want to change the image name
            image_name = new_name    
        else:
            image_name = image.name

        if new_size:
            img.thumbnail(new_size, Image.ANTIALIAS) #Like resize but mantains image aspect ratio
            img.save(thumb_io, format='JPEG')

        elif new_quality:
            img.save(thumb_io, format='JPEG', quality=new_quality)
        
        new_image = File(thumb_io, name=image_name)

        return new_image

#NOT IMPLEMENTED YET
def verify_image_file(image, valid_image_format=None):
    valid_format = False
    image_format = None

    try:
        imgage.verify()
        valid_image = True
        image_format = image.format

    except:
        valid_image = False

    if valid_image:
        if image_format:
            for extensions in valid_image_format:
                if extensions.upper() == image_format:
                    valid_format = True
                    break
        
    return valid_image, valid_format 


    
