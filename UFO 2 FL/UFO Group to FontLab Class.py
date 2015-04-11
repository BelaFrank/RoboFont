
from  vanilla import *
    
    
    
class GroupToClass(object): 
    
    def __init__(self):
        self.writeAsIs = False
        self.reorder = True
        self.w = FloatingWindow(    (-260, 100, 200, 90), 
                                    title = 'UFO Group to FL Class'    )
        self.w.button_save_to_flc = SquareButton(
                                    (10,10, -10, 30),
                                    title = 'Save to .flc File',
                                    sizeStyle = 'small',
                                    callback = self.generate_flc_file    )
        self.w.line = HorizontalLine(    (0, 40, -0, 30)    )
        self.w.writeAsIs = CheckBox(    (10, 61, 100, 20), 
                                        title = 'Write as is',
                                        callback=self.writeAsIsCallback,
                                        sizeStyle = 'small',
                                        value=self.writeAsIs    )
        self.w.reorder = CheckBox(    (100, 61, 100, 20),
                                        title = 'Re-order',
                                        callback=self.reorderCallback,
                                        sizeStyle = 'small',
                                        value=self.reorder    )
        
        self.w.open()
        
    def writeAsIsCallback(self, sender):
        self.w.reorder.set(False)
        self.writeAsIs = True 
        self.reorder = False

       
    def reorderCallback(self, sender):
        self.w.writeAsIs.set(False)
        self.writeAsIs = False
        self.reorder = True
    
                
    def generate_flc_file(self, sender):
        '''
        This script write an .flc file based on the groups in CurrentFont.    
        '''
        
        
        if not CurrentFont():
            print 'Open a UFO first.'
        
        elif CurrentFont() and not CurrentFont().path:
            print 'Save the UFO first.'
        
        elif CurrentFont() and CurrentFont().path:
            f = CurrentFont()
            fontname = f.info.familyName + ' ' + f.info.styleName
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
                        # TRY TO FIX WAY
                        if self.reorder == True:
                            key_should_be = ''
                            kerning_class_mark = [    'MMK_L_', 'KERN_LEFT_', 'public.kern1.', 
                                                    'MMK_R_', 'KERN_RIGHT_', 'public.kern2.']
                            for mark in kerning_class_mark:
                                if mark in i:
                                    key_should_be = i.split(mark)[1]
                                    #temp += key_should_be
                                if key_should_be in glyphs:
                                    pos = glyphs.index(key_should_be)
                                    glyphs[0], glyphs[pos] =  glyphs[pos], glyphs[0]
                
                
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

        
        



        

GroupToClass()
