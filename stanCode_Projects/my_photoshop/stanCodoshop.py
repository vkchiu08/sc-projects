"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage
import math                             # 為了計算開根號


def get_pixel_dist(pixel, red, green, blue):        # 計算各個pixel的rgb與n張圖片平均rgb值的距離差
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    dist = math.sqrt((red-pixel.red)**2+(green-pixel.green)**2+(blue-pixel.blue)**2)
    return dist


def get_average(pixels):                            # 用一個list回傳n張圖片的平均rgb值，
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red = 0
    green = 0
    blue = 0
    for px in pixels:
        red += px.red
        green += px.green
        blue += px.blue
    rgb = [red // len(pixels), green // len(pixels), blue // len(pixels)]
    return rgb


def get_best_pixel(pixels):        # 製造一個dict key=pixel的(x,y), value=distance距離,回傳距離最短的pixel(x,y)
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    dist = {}
    for px in pixels:
        red = get_average(pixels)[0]
        green = get_average(pixels)[1]
        blue = get_average(pixels)[2]
        distance = get_pixel_dist(px, red, green, blue)
        dist[px] = distance
    return min(dist, key=dist.get)

    # dist = []
    # for px in pixels:
    #     best = px
    #     red = get_average(pixels)[0]
    #     green = get_average(pixels)[1]
    #     blue = get_average(pixels)[2]
    #     dist.append(get_pixel_dist(px, red, green, blue))
    # if min(dist):               # 因為0是false 就不會return  #best=px所以best會回傳最後一個px
    #     return best
    # else:
    #     return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect

    for x in range(width):
        for y in range(height):
            image = []                      # 製造一個list裝images的pixel(寫在for loop外面list才不會變動)
            for img in images:
                img_point = img.get_pixel(x, y)
                image.append(img_point)
            blank1 = result.get_pixel(x, y)
            blank1.red = get_best_pixel(image).red
            blank1.green = get_best_pixel(image).green
            blank1.blue = get_best_pixel(image).blue

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
