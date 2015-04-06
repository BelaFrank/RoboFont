# RoboFont-scripts
RoboFont scripts

UFO Groups to FontLab Class
===========================

This makeshift, simple script write an .flc file based on the groups in CurrentFont. It takes care of the key glyph marking in kerning groups. 
    
NOTE that for kerning classes it looks for the MetricsMachine-like '@MMK_L_...' and '@MMK_R_...' groups names eg it expects your ufo kerning groups set up in MetricsMachine or in the same manner
    
OR
    
it looks for 'KERN_LEFT_...' and 'KERN_RIGHT_...' groups names.
    
All other groups will be written as OpenType classes.

TODO: 
- update with UFO3 style group naming sceme detection. Not that I expect many people to convert from UFO to .vfb in the future. It came handy once though.
- code clean-up as it is messt now
