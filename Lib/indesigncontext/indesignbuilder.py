#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
#     Supporting usage of InDesign API-scripting
# -----------------------------------------------------------------------------
#
#     indesignbuilder.py
#
import codecs
import os, shutil
import zipfile

from indesigncontext.constants import JSX_LIB
from pagebot.contexts.base.builder import BaseBuilder
from pagebot.toolbox.color import noColor
from pagebot.toolbox.units import pt, point3D
from pagebot.constants import *

class InDesignBuilder(BaseBuilder):

    PB_ID = 'inds'

    SCRIPT_PATH = '/Users/petr/Library/Preferences/Adobe InDesign/Version 14.0/en_US/Scripts/Scripts Panel/PageBot/'
    SCRIPT_PATH1 = '_export/'

    def __init__(self):
        self._fillColor = noColor
        self._strokeColor = noColor
        self._strokeWidth = pt(1)

        self.jsOut = []

    def _out(self, s):
        self.jsOut.append(s)

    def newDocument(self, w, h, **kwargs):
        self._out('/* Document */')
        self._out(JSX_LIB)
        self._out('var pbDoc = app.documents.add();')
        if w is not None and h is not None:
            self._out('pbDoc.documentPreferences.pageWidth = "%s";' % w)
            self._out('pbDoc.documentPreferences.pageHeight = "%s";' % h)
            if w > h:
                self._out('pbDoc.documentPreferences.pageOrientation = PageOrientation.landscape;')
            else:
                self._out('pbDoc.documentPreferences.pageOrientation = PageOrientation.portrait;')

    def newPage(self, w, h, **kwargs):
        self._out('/* Page */')
        self._out('var pbPage = pbDoc.pages.item(0);')
        self._out('pbPage.resize(CoordinateSpaces.INNER_COORDINATES,')
        self._out('    AnchorPoint.CENTER_ANCHOR,')
        self._out('    ResizeMethods.REPLACING_CURRENT_DIMENSIONS_WITH,')
        self._out('    [%d, %d]);' % (w.pt, h.pt))
        padding = kwargs.get('padding')
        if padding is not None:
            mt, mr, mb, ml = padding
            self._out('pbPage.marginPreferences.top = "%s";' % mt)
            self._out('pbPage.marginPreferences.right = "%s";' % mr)
            self._out('pbPage.marginPreferences.bottom = "%s";' % mb)
            self._out('pbPage.marginPreferences.left = "%s";' % ml)
        self._out('var pbElement;')
 
    def rect(self, x, y, w, h):
        self._out('/* Rect */')
        self._out('pbElement = pbPage.rectangles.add({geometricBounds:["%s", "%s", "%s", "%s"]});' % (y+h, x, y, x+w))
        self._outElementFillColor()
        self._outElementStrokeColor()

    def oval(self, x, y, w, h):
        self._out('/* Oval */')
        self._out('pbElement = pbPage.ovals.add({geometricBounds:["%s", "%s", "%s", "%s"]});' % (y+h, x, y, x+w))
        self._outElementFillColor()
        self._outElementStrokeColor()

    def fill(self, c):
        self._fillColor = c

    def stroke(self, c, w=None):
        self._strokeColor = c
        self.strokeWidth(w)

    def strokeWidth(self, w):
        if w is not None:
            self._strokeWidth = w
            
    def _outElementFillColor(self):
        """Set the fill color of pbElement to the current self._fillColor."""
        jsColor = None
        if self._fillColor not in (None, noColor):
            if self._fillColor.isRgb:
                r, g, b = self._fillColor.rgb
                jsColor = (r*255, g*255, b*255)
            elif self._fillColor.isCmyk:
                c, m, y, k = self._fillColor.cmyk
                jsColor = (c*100, m*100, y*100, k*100)
        if jsColor is not None:
            self._out('pbElement.fillColor = pbGetColor(pbDoc, %s);' % (list(jsColor),))
        if self._fillColor is not None and self._fillColor.a < 1:
            self._out('pbElement.transparencySettings.blendingSettings.opacity = %s' % (self._fillColor.a * 100))
        return None
            
    def _outElementStrokeColor(self):
        """Set the fill color of pbElement to the current self._strokeColor."""
        jsColor = None
        if self._strokeColor not in (None, noColor):
            if self._strokeColor.isRgb:
                r, g, b = self._strokeColor.rgb
                jsColor = (r*255, g*255, b*255)
            elif self._strokeColor.isCmyk:
                c, m, y, k = self._strokeColor.cmyk
                jsColor = (c*100, m*100, y*100, k*100)
        if jsColor is not None:
            self._out('pbElement.strokeColor = pbGetColor(pbDoc, %s);' % (list(jsColor),))
            self._out('pbElement.strokeWeight = "%s"' % self._strokeWidth)
        #if self._strokeColor.a < 1:
        #    self._out('pbElement.transparencySettings.blendingSettings.opacity = %s' % (self._strokeColor.a * 100))
        return None

    def image(self, path, p, alpha=1, pageNumber=1, w=None, h=None, scaleType=None):
        x, y, _ = point3D(p)
        w = w or pt(100)
        h = h or pt(100)
        self._out('/* Image %s */' % path)
        self._out('pbElement = pbPage.rectangles.add({geometricBounds:["%s", "%s", "%s", "%s"]});' % (y+h, x, y, x+w))
        self._outElementFillColor()
        self._outElementStrokeColor()
        #self._out('alert(myScriptPath() + "%s");' % path)
        self._out('pbElement.place(File(myScriptPath() + "%s"));' % path)
        #self._out('pbElement.place((File("/Users/petr/Library/Preferences/Adobe InDesign/Version 14.0/en_US/Scripts/Scripts Panel/PageBot/resources/images/cookbot10.jpg")));')
        # FitOptions: http://jongware.mit.edu/idcs4js/pe_FitOptions.html
        self._out('pbElement.fit (FitOptions.CONTENT_TO_FRAME);')
        if scaleType != SCALE_TYPE_FITWH:
            self._out('pbElement.fit (FitOptions.PROPORTIONALLY);')
        self._out('pbElement.fit (FitOptions.CENTER_CONTENT);')
        
    def scale(self, sx, sy, center=None):
        pass

    def lineDash(self, line):
        pass

    def line(self, p1, p2):
        pass

    def save(self):
        pass

    def restore(self):
        pass
       
    def saveDocument(self, path):
        """Write the IDML file from idmlRoot, indicated by path.
        """
        for basePath in (self.SCRIPT_PATH, self.SCRIPT_PATH1):
            f = codecs.open(basePath + path, 'w', encoding='utf-8')
            f.write('\n'.join(self.jsOut))
            f.write('\n' * 4)
            f.close()
         
     

if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
