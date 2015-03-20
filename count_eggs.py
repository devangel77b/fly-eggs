#!/usr/bin/env python
"""
"""

import argparse
import logging
import cv2
import numpy as np
import pandas as pd

if __name__ == "__main__":
    # this just gets some command line arguments 
    parser = argparse.ArgumentParser(description="count fly eggs in a photo",
                                     epilog=__doc__)
    parser.add_argument("ifile",help="image to count")
    parser.add_argument("--verbose",action="store_true",
                        help="toggle verbosity")
    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("running in verbose mode")
    else:
        logging.basicConfig(level=logging.INFO)

    # initialize display window
    cv2.namedWindow("count_eggs",cv2.WINDOW_NORMAL)

    # initialize morphological kernel
    opening_kernel = np.ones((5,5),np.uint8)
    dilation_kernel = np.ones((3,3),np.uint8)



    # read in the image as grayscale
    logging.debug("opening {0}".format(args.ifile))
    gray = cv2.imread(args.ifile,cv2.IMREAD_GRAYSCALE) 
    
    # threshold it
    retval,thresh = cv2.threshold(gray,64,255,cv2.THRESH_BINARY_INV)

    # erosion-dilation operation to get rid of breathing tubes
    opened = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,opening_kernel)
    dilated = cv2.dilate(opened,dilation_kernel,iterations=1)

    # find contours
    working = dilated.copy()
    contours,hierarchy = cv2.findContours(working,cv2.cv.CV_RETR_LIST,
                                          cv2.cv.CV_CHAIN_APPROX_NONE)

    # draw stuff
    draw = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
    cv2.drawContours(draw,contours,-1,(0,0,255),2)
    cv2.imshow("count_eggs",draw)
    cv2.waitKey()

    # compute moments and tabulate output
    # LATER
    # there should be 24 for the test image
    # copy what we do for turtle size acceptance limits

    logging.debug("cleaning up")
    cv2.destroyAllWindows()

    
