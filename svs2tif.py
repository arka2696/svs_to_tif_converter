import os

# Add the directory containing the OpenSlide DLLs to the PATH
os.add_dll_directory(r'C:\Openslide\bin')

import argparse
import openslide
from PIL import Image

def convert_svs_to_tif(input_path, output_path, level=1):
    # Open the .svs file
    slide = openslide.OpenSlide(input_path)
    
    # Get the dimensions of the specified level
    dimensions = slide.level_dimensions[level]
    
    # Read the image at the specified level
    img = slide.read_region((0, 0), level, dimensions)
    
    # Convert to RGB (remove alpha channel)
    img = img.convert("RGB")
    
    # Save the image as .tif without compression to preserve quality
    img.save(output_path, format='TIFF', compression=None)

def main(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.svs'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.tif')
            convert_svs_to_tif(input_path, output_path, level=1)
            print(f'Converted {filename} to .tif')

    print('Conversion completed.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert SVS files to TIF format.')
    parser.add_argument('--input', type=str, required=True, help='Path to the input folder containing SVS files.')
    parser.add_argument('--output', type=str, required=True, help='Path to the output folder to save TIF files.')

    args = parser.parse_args()
    main(args.input, args.output)
