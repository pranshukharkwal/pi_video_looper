import os
from PIL import Image
import moviepy.video.io.ImageSequenceClip
image_folder='images'
fps=0.25
mean_height = 0
mean_width = 0


images = os.listdir(image_folder)
num_of_images = len(images)

for file in images:
    im = Image.open(os.path.join(image_folder , file))
    width , height = im.size
    mean_height += height
    mean_width += width

mean_width = int(mean_width / num_of_images) 
mean_height = int(mean_height / num_of_images) 

for file in images:
    im = Image.open(os.path.join(image_folder , file))
    imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)  
    imResize.save(os.path.join(image_folder , file), 'PNG' , quality = 95)
    print(file , "resized")


image_files = [image_folder+'/'+img for img in os.listdir(image_folder) if img.endswith(".png")]
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('videopi.mp4')