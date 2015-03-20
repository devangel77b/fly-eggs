#!/usr/bin/env python
"""
"""

import argparse
import logging
import cv2

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






    # read in the image as grayscale
    logging.debug("opening {0}".format(args.ifile))
    gray = cv2.imread(args.ifile,cv2.IMREAD_GRAYSCALE) 
    
    # threshold it
    retval,thresh = cv2.threshold(gray,64,255,cv2.THRESH_BINARY_INV)

    # find contours
    working = thresh.copy()
    contours,hierarchy = cv2.findContours(working,cv2.cv.CV_RETR_LIST,
                                          cv2.cv.CV_CHAIN_APPROX_NONE)

    # erosion-dilation operation to get rid of breathing tubes
    # LATER

    # draw stuff
    draw = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
    cv2.drawContours(draw,contours,-1,(0,0,255))
    cv2.imshow("count_eggs",draw)
    cv2.waitKey()

    # compute moments and tabulate output
    # LATER

    logging.debug("cleaning up")
    cv2.destroyAllWindows()

    
