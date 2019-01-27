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


    baseheight = 400
    img = Image.open('image.jpg')
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), Image.ANTIALIAS)
    img.save('resized_image.jpg')
    img = cv2.imread('resized_image.jpg')
    height = img.shape[1]
    width = img.shape[0]
    start = [int(width/2-200),int(height/2-150)];
    end = [int(width/2+200),int(height/2+150)];
    image = 'resized_image.jpg'
    crop(image, (start[1], start[0], end[1], end[0]), 'resized_image.jpg')
