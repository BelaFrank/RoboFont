# RoboFont-scripts
A selection of really simple .py / RoboFont / DrawBot scripts that I wrote / use / try and improve when I can. 

Feel free to use or modify any of them. They are tailored after my needs and there's no guarantee they work as you wish or at all. Always use with copies. 

##UFO Groups to FontLab Class

This makeshift, simple script writes an .flc file next to your UFO. It takes care of marking the key glyph of FL kerning classes. 
    
NOTE that for kerning classes it looks for:

- MetricsMachine-like *@MMK_L_...* and *@MMK_R_...* group names (eg it expects your ufo kerning groups set up in MetricsMachine or in the same manner) 

- or it looks for *KERN_LEFT_...* and *KERN_RIGHT_...* 

- or *public.kern1.* and *public.kern2.* UFO3 style kerning groups names.
    
All other groups will be written as OpenType classes.

Note: it's always a good idea to check the FL kerning class key glyphs in generated file.
