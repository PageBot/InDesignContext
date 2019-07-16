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

    def getWH(self, w, h, e):
        if e is not None:
            w = w or e.w
            h = h or e.h
        else:
            w = w or DEFAULT_WIDTH
            h = h or DEFAILT_HEIGHT
        return w, h

    def _out(self, s):
        self.jsOut.append(s)

    def newDocument(self, w, h, doc):
        self._out('/* Document */')
        self._out(JSX_LIB)
        self._out('var pbDoc = app.documents.add();')
        self._out('pbDoc.documentPreferences.pagesPerDocument = %d;' % len(doc.pages))
        if w is not None and h is not None:
            self._out('pbDoc.documentPreferences.pageWidth = "%s";' % w)
            self._out('pbDoc.documentPreferences.pageHeight = "%s";' % h)
            if w > h:
                self._out('pbDoc.documentPreferences.pageOrientation = PageOrientation.landscape;')
            else:
                self._out('pbDoc.documentPreferences.pageOrientation = PageOrientation.portrait;')
        self._out('var pbPage;')
        self._out('var pbPageIndex = 0;')
        self.outDocumentStyles(self, doc)

    def outDocumentStyles(self, doc):    
        # If there are styles defined, then exporg them a paragraph styles
        #pbDoc.paragraphStyles.add({name:"Title", appliedFont:"Upgrade", fontStyle:'Bold', 
        #    justification:Justification.CENTER_ALIGN,
        #    pointSize:300, leading:300, fillColor: pbGetColor(pbDoc, [255, 255, 255])});
        for name, style in doc.styles.items():
            self._out('pbDoc.paragraphStyles.add({')
            self._out('')
            self._out(')};')

    def newPage(self, w=None, h=None, page=None):
        w, h = self.getWH(w, h, page)
        self._out('/* Page */')
        self._out('if (pbPage){')
        self._out('    pbPageIndex += 1;')
        self._out('}')
        self._out('pbPage = pbDoc.pages.item(pbPageIndex);')
        self._out('pbPage.resize(CoordinateSpaces.INNER_COORDINATES,')
        self._out('    AnchorPoint.CENTER_ANCHOR,')
        self._out('    ResizeMethods.REPLACING_CURRENT_DIMENSIONS_WITH,')
        self._out('    [%d, %d]);' % (w.pt, h.pt))
        mt, mr, mb, ml = page.padding
        self._out('pbPage.marginPreferences.top = "%s";' % mt)
        self._out('pbPage.marginPreferences.right = "%s";' % mr)
        self._out('pbPage.marginPreferences.bottom = "%s";' % mb)
        self._out('pbPage.marginPreferences.left = "%s";' % ml)
        self._out('var pbElement;')
 
    def rect(self, px, py, w=None, h=None, e=None):
        w, h = self.getWH(w, h, e)
        self._out('/* Rect */')
        self._out('pbElement = pbPage.rectangles.add({geometricBounds:["%s", "%s", "%s", "%s"]});' % (py+h, px, py, px+w))
        self._outElementFillColor(e)
        self._outElementStrokeColor(e)

    def oval(self, px, py, w=None, h=None, e=None):
        w, h = self.getWH(w, h, e)
        self._out('/* Oval */')
        self._out('pbElement = pbPage.ovals.add({geometricBounds:["%s", "%s", "%s", "%s"]});' % (py+h, px, py, px+w))
        self._outElementFillColor(e)
        self._outElementStrokeColor(e)

    def fill(self, c):
        self._fillColor = c

    def stroke(self, c, w=None):
        self._strokeColor = c
        self.strokeWidth(w)

    def strokeWidth(self, w):
        if w is not None:
            self._strokeWidth = w
            
    def _outElementFillColor(self, e):
        """Set the fill color of pbElement to the current self._fillColor."""
        jsColor = None
        if e is not None:
            fillColor = e.fill
        else:
            fillColor = self._fillColor
        if fillColor not in (None, noColor):
            if fillColor.isRgb:
                r, g, b = self._fillColor.rgb
                jsColor = (r*255, g*255, b*255)
            elif fillColor.isCmyk:
                c, m, y, k = fillColor.cmyk
                jsColor = (c*100, m*100, y*100, k*100)
        if jsColor is not None:
            self._out('pbElement.fillColor = pbGetColor(pbDoc, %s);' % (list(jsColor),))
        if fillColor is not None and fillColor.a < 1:
            self._out('pbElement.transparencySettings.blendingSettings.opacity = %s' % (fillColor.a * 100))
        return None
            
    def _outElementStrokeColor(self, e):
        """Set the fill color of pbElement to the current self._strokeColor."""
        jsColor = None
        if e is not None:
            strokeColor = e.stroke
            strokeWidth = e.strokeWidth
        else:
            strokeColor = self._strokeColor
            strokeWidth = self._strokeWidth
        if strokeColor not in (None, noColor):
            if strokeColor.isRgb:
                r, g, b = strokeColor.rgb
                jsColor = (r*255, g*255, b*255)
            elif strokeColor.isCmyk:
                c, m, y, k = strokeColor.cmyk
                jsColor = (c*100, m*100, y*100, k*100)
        if jsColor is not None:
            self._out('pbElement.strokeColor = pbGetColor(pbDoc, %s);' % (list(jsColor),))
            self._out('pbElement.strokeWeight = "%s"' % strokeWidth)
        #if strokeColor.a < 1:
        #    self._out('pbElement.transparencySettings.blendingSettings.opacity = %s' % (strokeColor.a * 100))
        return None

    def image(self, path, p, alpha=None, pageNumber=1, w=None, h=None, scaleType=None, e=None):
        px, py, _ = point3D(p)
        w, h = self.getWH(w, h, e)
        self._out('/* Image %s */' % path)
        self._out('pbElement = pbPage.rectangles.add({geometricBounds:["%s", "%s", "%s", "%s"]});' % (py+h, px, py, px+w))
        self._outElementFillColor(e)
        self._outElementStrokeColor(e)
        #self._out('alert(myScriptPath() + "%s");' % path)
        self._out('pbElement.place(File(myScriptPath() + "%s"));' % path)
        # FitOptions: http://jongware.mit.edu/idcs4js/pe_FitOptions.html
        self._out('pbElement.fit(FitOptions.CONTENT_TO_FRAME);')
        self._out('pbElement.fit(FitOptions.CENTER_CONTENT);')
        if scaleType is None and e is not None:
            scaleType = e.scaleType
        if scaleType  != SCALE_TYPE_FITWH:
            self._out('pbElement.fit(FitOptions.PROPORTIONALLY);')
        
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
