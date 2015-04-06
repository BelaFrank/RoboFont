# RoboFont-scripts
A selection of really simple RoboFont scripts

##UFO Groups to FontLab Class

This makeshift, simple script writes an .flc file next to your UFO. It takes care of marking the key glyph of FL kerning classes. 
    
NOTE that for kerning classes it looks for the MetricsMachine-like '@MMK_L_...' and '@MMK_R_...' group names (eg it expects your ufo kerning groups set up in MetricsMachine or in the same manner) or it looks for 'KERN_LEFT_...' and 'KERN_RIGHT_...' or 'public.kern1.' and 'public.kern2.' UFO3 style kerning groups names.
    
All other groups will be written as OpenType classes.

Note: the script marks the first glyph in a group as the key glyph of the FL kerning class. However it may not be the one you want it to be. RoboFont seems to sort the glyphs in groups alphabetically and so you can end up with a key glyph you didn't want. The ordering can be changed manually.
