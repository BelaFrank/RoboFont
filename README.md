# RoboFont-scripts
RoboFont scripts

UFO Groups to FontLab Class
===========================

This script write an .flc file based on the groups in CurrentFont.
    
NOTE that for kerning classes it looks for the MetricsMachine-like '@MMK_L_...' and '@MMK_R_...' groups names eg it expects your ufo groups set up in MetricsMachine or in the same manner
    
OR
    
it looks for 'KERN_LEFT_...' and 'KERN_RIGHT_...' groups names.
    
All other groups will be written as OpenType classes.
