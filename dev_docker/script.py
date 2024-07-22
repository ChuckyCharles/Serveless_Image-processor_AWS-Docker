import cv2
import sys

def resize_image(input_path, output_path ,size=(800,800)):
    #readthe image
    image=cv2.imread(input_path)

    #resize the image
    resized_image=cv2.resize(image.size)

    #save the resized image
    cv2.imwrite(output_path,resized_image)

if __name__=='__main__':
    input_path=sys.argv[1]
    output_path=sys.argv[2]
    resize_image(input_path, output_path)
    
