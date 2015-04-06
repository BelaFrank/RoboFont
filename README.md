# RoboFont-scripts
A selection of really simple RoboFont scripts

##UFO Groups to FontLab Class

This makeshift, simple script writes an .flc file next to your UFO. It takes care of marking the key glyph of FL kerning classes. 
    
NOTE that for kerning classes it looks for the MetricsMachine-like '@MMK_L_...' and '@MMK_R_...' group names (eg it expects your ufo kerning groups set up in MetricsMachine or in the same manner) or it looks for 'KERN_LEFT_...' and 'KERN_RIGHT_...' or 'public.kern1.' and 'public.kern2.' UFO3 style kerning groups names.
    
All other groups will be written as OpenType classes.

Note: it's a good idea to check the FL kerning class key glyphs in your file.
