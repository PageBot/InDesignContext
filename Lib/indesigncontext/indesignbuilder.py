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
from lxml import etree

from indesigncontext.constants import JSX_LIB
from pagebot.contexts.base.builder import BaseBuilder
from pagebot.toolbox.color import noColor

class InDesignBuilder(BaseBuilder):

    PB_ID = 'inds'

    SCRIPT_PATH = '/Users/petr/Library/Preferences/Adobe InDesign/Version 14.0/en_US/Scripts/Scripts Panel/PageBot/'
    SCRIPT_PATH1 = '_export/'

    def __init__(self):
        self.fillColor = noColor
        self.strokeColor = noColor
        self.strokeWidth = 0

        self.jsOut = []

    def _out(self, s):
        self.jsOut.append(s)

    def newDocument(self, path):
        self._out(JSX_LIB)
        self._out('var pbDoc = app.documents.add();')
        self._out('var pbPage = pbDoc.pages.item(0);')
        self._out('var pbElement;')

    def rect(self, x, y, w, h):
        self._out('pbElement = pbPage.rectangles.add({geometricBounds:["%s", "%s", "%s", "%s"]});' % (y+h, x, y, x+w))
        self._outElementFillColor()

    def fill(self, c):
        self.fillColor = c

    def _outElementFillColor(self):
        """Set the fill color of pbElement to the current self.fillColor."""
        jsColor = None
        if self.fillColor not in (None, noColor):
            if self.fillColor.isRgb:
                r, g, b = self.fillColor.rgb
                jsColor = (r*255, g*255, b*255)
            elif self.fillColor.isCmyk:
                c, m, y, k = self.fillColor.cmyk
                jsColor = (c*100, m*100, y*100, k*100)
        if jsColor is not None:
            self._out('pbElement.fillColor = pbGetColor(pbDoc, %s);' % (list(jsColor),))
        if self.fillColor.a < 1:
            self._out('pbElement.transparencySettings.blendingSettings.opacity = %s' % (self.fillColor.a * 100))
        return None

    def lineDash(self, line):
        pass

    def line(self, p1, p2):
        pass

    def save(self):
        pass

    def restore(self):
        pass

    def newPage(self, w, h):
        pass
        
    def saveDocument(self, path):
        """Write the IDML file from idmlRoot, indicated by path.
        """
        for basePath in (self.SCRIPT_PATH, self.SCRIPT_PATH1):
            f = codecs.open(basePath + path, 'w', encoding='utf-8')
            f.write('\n'.join(self.jsOut))
            f.close()
         
     

if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
