import PIL
from PIL import Image
import cv2
def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)


if __name__ == '__main__':

    img = cv2.imread('resized_imagea.jpg')
    height = img.shape[0]
    width = img.shape[1]
    wsize = height/4
    wsize = wsize*3
    if width < wsize:
        hsize = width/3
        hsize = hsize*4
        middle = hsize/2
        heightpoints = [int(height/2+middle),int(height/2-middle)]
        image = 'image.jpg'
        crop(image, (0, heightpoints[1], width, heightpoints[0]), 'resized_image.jpg')
    else:
        middle = wsize/2
        widthpoints = [int(width/2+middle),int(width/2-middle)]
        image = 'image.jpg'
        crop(image, (widthpoints[1], 0, widthpoints[0], height), 'resized_image.jpg')
