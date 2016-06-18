"""Script to sort my downloaded wallpapers in folders based on resolution"""
# pylint: disable=C0103
import os
import glob
import shutil
from PIL import Image


fileType = ('*.jpg', '*.jpeg', '*.png', '*.bmp') # the tuple of file types
filesGrabbed = [] # the list of pictures
for files in fileType:
    filesGrabbed.extend(glob.glob(files))


i = 0

while i < len(filesGrabbed):
    infile = filesGrabbed[i]
    im = Image.open(infile)
    foldName = ("%dx%d" % im.size)

    if not os.path.exists(foldName): # Create the subdirectory if it isn't already there.
        os.mkdir(foldName) # make directory
        print('Successfully created directory', foldName)

    im.close()

    root_src_dir = os.getcwd()
    root_dst_dir = foldName

    for src_dir, dirs, fyles in os.walk(root_src_dir):
        dst_dir = (root_src_dir+'\\'+foldName)

    shutil.move(infile, dst_dir)
    print('Moving', infile, 'to the', "%dx%d" % im.size, 'directory')

    i = i + 1

print("Done")
