Automatic fly egg counting and measuring
========================================
This code counts and measures Drosophila eggs in photos.  

Example methods text
====================
Eggs were placed on slides... (LAURA FILL IN). Images of the prepared slides 
were obtained by... (LAURA FILL IN). Images were xxx by xxx TIFF format images,
N images for the entire dataset comprising x MB. 

Eggs were automatically counted and measured using routines from the OpenCV 
library (opencv.org) implemented in Python (cv2 version xxx; Python version 
2.7.x).  Each image was converted to grayscale and thresholded to obtain a 
binary image. Eggs were found by identifying contours in the binary images.  
Artifacts and the breathing tube were removed through use of a 3-pixel 
erosion/dilation operation; contours remaining after this operation were 
only (THE MEATY PART OF) eggs. The image moments were then calculated for 
each egg contour to obtain estimates of the area and major and minor axes.
Moments were scaled using an image of a ruler on the microscope stage.  
Major and minor axis measurements were used as the length and width, 
respectively, for each egg.

In a test image that was manually measured, the manual measurements differed
from the automatic measurements by TINY%. 

Contributors
============
Laura Sligar is the egg project lead.  We thank Dennis Evangelista for providing
the Python code for automatic counting and measurement of eggs.

