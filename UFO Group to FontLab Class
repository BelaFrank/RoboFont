
    

def print_flc_file():
    '''
    This script write an .flc file based on the groups in CurrentFont.
    
    NOTE that for kerning classes it looks for the MetricsMachine-like
    '@MMK_L_...' and '@MMK_R_...' groups names eg it expects your ufo groups 
    set up in MetricsMachine or in the same manner
    
    OR
    
    it looks for 'KERN_LEFT_...' and 'KERN_RIGHT_...' groups names (this is
    useful when you open up a binary font with kerning in RoboFont.
    
    All other groups will be written as OpenType classes.
    
    '''

    if CurrentFont():

        f = CurrentFont()
        groups = sorted(f.groups.keys())
    
        temp = '%%FONTLAB CLASSES\n'
    
        for i in groups:
            if f.groups[i]:
                if i[0] == '@':
                    fl_class_name = i.replace('@', '_')
                else:
                    fl_class_name = i
                
                temp += '%%CLASS %s\n' %fl_class_name
                temp += '%%GLYPHS '
        
                glyphs = [ x for x in f.groups[i]] 
        
                if i[0] == '@':
                    glyphs[0] = glyphs[0] + '\''
                else:
                    pass
        
                glyphs_str = ''
                x = 0
                for n in range(0, len(glyphs)):
                    glyphs_str += glyphs[n] + ' '
                    x += 1
                
                temp += '%s\n' %glyphs_str 
        
                if 'MMK_L' in i or 'KERN_LEFT' in i:
                    temp += '%%KERNING L 0\n'
                elif 'MMK_R' or 'KERN_RIGHT' in i:
                    temp += '%%KERNING R 0\n'
                else:
                    pass
        
                temp += '%%END\n\n'
        
        # Write it to an .flc file    
        flc_path = (CurrentFont().path).replace('ufo', 'flc')
    
        f = open(flc_path, 'w')
        f.write(temp)
        f.close()
        
        print 'An .flc file was written next to your UFO.'
        
        
        # test block below
        #print temp
        
            
    else:
        print 'Open a UFO first.'
        

print_flc_file()
