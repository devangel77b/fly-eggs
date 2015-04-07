#!/usr/bin/env python
"""
This script will detect eggs (any dark blobs) in an image and output
.CSV giving the image filename, area, length and width. The latter are taken 
as the major and minor axis lengths, respectively.  This script outputs all
measurements in pixels, e.g. area in pixels^2 and length and width in pixels.
They can be converted afterwards with a photo of a ruler on the same stage.
The filename is expected to be of the form SPECIES_FLYID_DATE.tiff.  If it is
not that this will fail; it can be modified to handle others using re but
for now this works.
Dennis Evangelista, 2015.
"""

import argparse
import logging
import cv2
import numpy as np
import pandas as pd
import os

if __name__ == "__main__":
    # this just gets some command line arguments 
    parser = argparse.ArgumentParser(description="count fly eggs in a photo",
                                     epilog=__doc__)
    parser.add_argument("ifile",nargs="+",help="image(s) to count")
    parser.add_argument("--threshold",default=64,
                        help="upper threshold for egg detection, default 64")
    parser.add_argument("--athreshold",default=9,
                        help="lower threshold for egg area, default 9 pix")
    parser.add_argument("--display",action="store_true",
                        help="display images while working")
    parser.add_argument("--verbose",action="store_true",
                        help="toggle verbosity")
    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("...running in verbose mode")
    else:
        logging.basicConfig(level=logging.INFO)

    # initialize display window
    if args.display:
        cv2.namedWindow("count_eggs",cv2.WINDOW_NORMAL)
        logging.debug("...displaying images while working")

    # initialize morphological kernel
    opening_kernel = np.ones((5,5),np.uint8)
    dilation_kernel = np.ones((3,3),np.uint8)

    # output header
    print("species,flyid,date,area,length,width")



    # read in the image as grayscale
    for eachfname in args.ifile:
        logging.debug("opening {0}".format(eachfname))
        gray = cv2.imread(eachfname,cv2.IMREAD_GRAYSCALE) 
    
        # threshold it
        retval,thresh = cv2.threshold(gray,int(args.threshold),255,
                                      cv2.THRESH_BINARY_INV)

        # erosion-dilation operation to get rid of breathing tubes
        opened = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,opening_kernel)
        dilated = cv2.dilate(opened,dilation_kernel,iterations=1)

        # find contours
        working = dilated.copy()
        contours,hierarchy = cv2.findContours(working,cv2.cv.CV_RETR_LIST,
                                              cv2.cv.CV_CHAIN_APPROX_NONE)

        # strip metadata out of filename
        head,tail = os.path.split(eachfname)
        fname,extension = os.path.splitext(tail)
        splitted = fname.split('_')

        # draw stuff
        if args.display:
            draw = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
            cv2.drawContours(draw,contours,-1,(0,0,255),2)
            cv2.imshow("count_eggs",draw)
            cv2.waitKey()

        # compute moments and tabulate output
        # there should be 24 for the test image
        # copy what we do for turtle size acceptance limits
        for each in contours:
            m = cv2.moments(each)
            center,axes,angle = cv2.fitEllipse(each)
            area = m['m00']
            major = np.argmax(axes)
            minor = 1-major
            if area>float(args.athreshold):
                print("{0},{1},{2},{3},{4},{5}".format(splitted[0],
                                                       splitted[1],
                                                       splitted[2],
                                                       area,axes[major],
                                                       axes[minor]))

    logging.debug("cleaning up")
    if args.display:
        cv2.destroyAllWindows()

    
