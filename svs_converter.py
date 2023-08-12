"""
Created on Thu May  4 20:42:34 2023

@author: Utku Turkbey
"""

import os
import csv

OPENSLIDE_PATH = r'C:\Users\uturk\Desktop\svs_converter\openslide-win64-20230414\bin'
if hasattr(os, 'add_dll_directory'):
    with os.add_dll_directory(OPENSLIDE_PATH):
        from openslide import OpenSlide
else:
    from openslide import OpenSlide

input_folder = 'svs_slides'
output_folder = 'converted_slides'
output_format = 'png'
csv_file = 'thyroid_data.csv'

# loop through all rows in the CSV file
# if necessary create output folders for unique class names
# convert to output_format and save to the related output folder
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip header row
    for row in reader:
        filename = row[0]
        class_name = row[1]
        class_folder = os.path.join(output_folder, class_name)
        if not os.path.exists(class_folder):
            os.makedirs(class_folder)
        input_path = os.path.join(input_folder, filename + ".svs")
        # open the .svs file
        try:
            slide = OpenSlide(input_path)
            # create a image from the slide
            image = slide.read_region((0, 0), slide.level_count - 1, slide.level_dimensions[slide.level_count - 1])
            # save the image in the output folder for the corresponding class name
            output_filename = filename + '.' + output_format
            output_path = os.path.join(class_folder, output_filename)
            image.save(output_path)
        except:
            print(f"File {filename} not found in {input_folder}")