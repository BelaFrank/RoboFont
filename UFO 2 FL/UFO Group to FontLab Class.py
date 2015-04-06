
    

def print_flc_file():
    '''
    This script write an .flc file based on the groups in CurrentFont.    
    '''

    if CurrentFont():

        f = CurrentFont()
        groups = sorted(f.groups.keys())
    
        temp = '%%FONTLAB CLASSES\n'
    
        for i in groups:
            if f.groups[i]:
                if i[0] == '@':
                    fl_class_name = i.replace('@', '_') # FL kern class name must start with underscore
                else:
                    fl_class_name = i
                
                temp += '%%CLASS %s\n%%GLYPHS ' %fl_class_name
        
                glyphs = [ x for x in f.groups[i]] 
        
                if i[0] == '@':
                    glyphs[0] = glyphs[0] + '\'' # make first glyph a key glyph if kerning class.
        
                glyphs = ' '.join(glyphs)
                
                temp += '%s\n' %glyphs
        
                is_left = 'MMK_L' in i or 'KERN_LEFT' in i or 'public.kern1.' in i
                is_right = 'MMK_R' in i or 'KERN_RIGHT' in i or 'public.kern2.' in i                
        
                if is_left:
                    temp += '%%KERNING L 0\n'
                    
                if is_right:
                    temp += '%%KERNING R 0\n'
                    
                else:
                    pass
                            
                temp += '%%END\n\n'
        
        # Write it to an .flc file    
        flc_path = (CurrentFont().path).replace('ufo', 'flc')
    
        f = open(flc_path, 'w')
        f.write(temp)
        f.close()
        
        print 'An .flc file with %i classes was written next to your UFO.' %len(groups)
        
        
        # test block below
        #print temp
        
            
    else:
        print 'Open a UFO first.'
        

print_flc_file()
