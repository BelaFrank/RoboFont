
from  vanilla import *

url = ''

class GroupToClass(object): 
    
    def __init__(self):
        self.f = ''
        self.writeAsIs = False
        self.reorder = True
        self.rename = False
        self.w = FloatingWindow(    (-260, 100, 220, 90), 
                                    title = 'UFO Group to FL Class'    )
        self.w.button_save_to_flc = SquareButton(
                                    (10,10, -10, 30),
                                    title = 'Save to .flc file',
                                    sizeStyle = 'small',
                                    callback = self.main    )
        self.w.line1 = HorizontalLine((0, 40, -0, 30))
        self.w.writeAsIs = CheckBox(    (10, 61, 100, 20), 
                                        title = 'As is',
                                        callback=self.swap,
                                        sizeStyle = 'small',
                                        value=self.writeAsIs    )
        self.w.reorder = CheckBox(    (70, 61, 100, 20),
                                        title = 'Reorder',
                                        callback=self.swap,
                                        sizeStyle = 'small',
                                        value=self.reorder    )
        self.w.rename = CheckBox(    (148, 61, 100, 20),
                                        title = 'Rename',
                                        callback=self.renameCallback,
                                        sizeStyle = 'small',
                                        value=self.rename    )
        self.w.open()
        

    
    def swap(self, sender):
        if self.writeAsIs == False:
            self.writeAsIs = True
            self.w.writeAsIs.set(True)
            
            self.reorder = False
            self.w.reorder.set(False)
        else:
            self.writeAsIs = False
            self.w.writeAsIs.set(False)
            
            self.reorder = True
            self.w.reorder.set(True)
              
              
    def renameCallback(self, sender):
        if self.rename == False:
            self.rename = True
        else: 
            self.rename = False


    def generate_flc_file(self):       
        f = self.f   
        fontname = f.info.familyName + ' ' + f.info.styleName
        groups = sorted(f.groups.keys())

        leftMark = ['@MMK_L_', '@KERN_LEFT_'] #'public.kern1.'
        rightMark = [ '@MMK_R_', '@KERN_RIGHT_'] #'public.kern2.'
        
        temp = '%%FONTLAB CLASSES\n\n'
        

        for i in groups:
            if f.groups[i]:
                isLeft = False
                isRight = False
                
                fl_class_name = i
                                                
                for j in leftMark:
                    if j in i:
                        isLeft = True
                        nameKey = i.replace(j, '')
                        if self.rename == True:
                            fl_class_name = i.replace(j, '_') + '_1ST'
                        else:
                            fl_class_name = i.replace('@', '_')
                        
                for j in rightMark:
                    if j in i:
                        isRight = True
                        nameKey = i.replace(j, '')
                        if self.rename == True:
                            fl_class_name = i.replace(j, '_') + '_2ND'
                        else:
                            fl_class_name = i.replace('@', '_')
                
                
                temp += '%%CLASS ' + fl_class_name
                temp += '\n%%GLYPHS '

                glyphs = [ x for x in f.groups[i]]
                
                if self.reorder == True and (isLeft == True or isRight == True):
                    if nameKey in glyphs:
                        pos = glyphs.index(nameKey)
                        glyphs[0], glyphs[pos] =  glyphs[pos], glyphs[0]
                                   
                glyphs = ' '.join(glyphs)
                temp += '%s\n' %glyphs
                temp += '%%END\n\n'
                
                
        # Write it to an .flc file    
        flc_path = (f.path).replace('.ufo', '.flc')        
        f = open(flc_path, 'w')
        f.write(temp)
        f.close()

        print 'An .flc file with %i classes was written next to your UFO.' %len(groups)
        
                                              
    def main(self, sender):
        
        if url and not CurrentFont():
            self.f = OpenFont(url, showUI=False)
            self.generate_flc_file()
            
        elif CurrentFont() and CurrentFont().path:
            self.f = CurrentFont()
            self.generate_flc_file()
        
        elif CurrentFont() and not CurrentFont().path:
            print 'Save the UFO first.'
        
        elif not CurrentFont():
            print 'Open a UFO or give me a path.'
        
        
GroupToClass()
