import albumentations as A
from PIL import Image
import numpy as np
import time
import os

# Read an image with OpenCV and convert it to the RGB colorspace
image_path = "dataset/sitting"
save_path = "augmented/sitting/"
image_file_list = os.listdir(image_path)

# Declare an augmentation pipeline
transform = A.Compose([
	A.HorizontalFlip(p=0.5),
	A.Lambda(),
	A.Perspective(),
	A.PiecewiseAffine()
])


for x in image_file_list:
	image = Image.open(os.path.join(image_path,x))
	images_list = [image]
	image = np.array(image)
	for i in range(2):
		transformed = transform(image=image)
		transformed_image = transformed["image"]
		PIL_image = Image.fromarray(np.uint8(transformed_image)).convert('RGB')
		format = str(time.time())+".jpg"
		file_name = os.path.join(save_path,format)
		PIL_image.save(file_name)