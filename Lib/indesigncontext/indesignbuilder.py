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
#     idmlbuilder.py
#
import codecs
import os, shutil
import zipfile
from lxml import etree

from pagebot.contexts.base.builder import BaseBuilder
from idmlcontext.objects.designmap import DesignMap
from idmlcontext.objects.spread import SpreadRoot

class InDesignBuilder(BaseBuilder):

    PB_ID = 'inds'

    SCRIPT_PATH = '/Users/petr/Library/Preferences/Adobe InDesign/Version 14.0/en_US/Scripts/Scripts Panel/PageBot/'

    def __init__(self):
        self.jsOut = []

    def _out(self, s):
        self.jsOut.append(s)

    def newDocument(self, path):
        self._out('var myDoc = app.documents.add();')
        self._out('var myPage = myDoc.pages.item(0);')

    def rect(self, x, y, w, h):
        self._out('myRectangle = myPage.rectangles.add({geometricBounds:[100, 100, 200, 200]});')

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
        f = codecs.open(self.SCRIPT_PATH + path, 'w', encoding='utf-8')
        f.write('\n'.join(self.jsOut))
        f.close()
         

if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
