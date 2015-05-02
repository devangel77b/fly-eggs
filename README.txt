Automatic fly egg counting and measuring
========================================
This code counts and measures Drosophila eggs in photos.  

Example methods text
--------------------
Wash collect: Eggs were laid on Drosophila Instant Media (Carolina Biological Supply) and extracted from media by washing in sucrose water following method of Schou 2013 (http://www.tandfonline.com/doi/pdf/10.4161/fly.22758)
Apple plate collect: Eggs were laid on agar plates made from apple juice, agar, sucrose, and colored with food coloring. Individual eggs were manually removed from media and placed on slides.
Images of the prepared slides were obtained from the UNC Microscopy Lab WILD macroscope. Images were xxx by xxx TIFF format images,
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
------------
Laura Sligar is the egg project lead.  We thank Dennis Evangelista for providing
the Python code for automatic counting and measurement of eggs.

