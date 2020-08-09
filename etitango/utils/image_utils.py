from PIL import Image
from io import BytesIO
from django.core.files import File

def reduce_image_size(image, new_name=None, new_quality=None, new_size=None):
    with Image.open(image) as img:
        thumb_io = BytesIO()

        if new_name:
            image_name = new_name    
        else:
            image_name = image.name

        if new_size:
            img.thumbnail(new_size, Image.ANTIALIAS)
            img.save(thumb_io, format='JPEG')

        elif new_quality:
            img.save(thumb_io, format='JPEG', quality=new_quality)

        new_image = File(thumb_io, name=image_name)

        return new_image

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


    
