# RoboFont scripts
A selection of really simple .py / RoboFont / DrawBot scripts that I wrote / use / try and improve when I can. 

Feel free to use or modify any of them. They are tailored after my needs and there's no guarantee they work as you wish or at all. Always use with copies. 

##UFO Groups to FontLab Class
This simple script writes an .flc file next to your UFO. It takes care of marking the key glyph of FL kerning classes. 

![UFO Group to FontLab Class](https://github.com/BelaFrank/RoboFont/blob/master/UFO%202%20FL/UFO%20Group%20to%20FontLab%20Class.png "UFO Group to FontLab Class")

NOTE that for kerning classes it looks for:

- MetricsMachine-like *@MMK_L_...* and *@MMK_R_...* group names (eg it expects your ufo kerning groups set up in MetricsMachine or in the same manner) 

- or it looks for *KERN_LEFT_...* and *KERN_RIGHT_...* 

- or *public.kern1.* and *public.kern2.* UFO3 style kerning groups names.
    
All other groups will be written as OpenType classes.

There are options now—by default, it tries to mark the proper glyph based on group name as kerning class key glyph ('Reorder'). You can make it to convert the groups as they are and mark the first glyph as key selecting the 'Write as is' option.

It's always a good idea to check the FL kerning class key glyphs in generated file.


#Feedback/Suggestions

Issues and pull requests very much appreciated.
