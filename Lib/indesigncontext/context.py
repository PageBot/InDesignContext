
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
#     context.py
#
#     InDesign JavaScript file specifications here:
#     InDesign_ScriptingGuids_JS.df
#
from pagebot.contexts.base.context import BaseContext
from pagebot.constants import FILETYPE_IDML
from pagebot.toolbox.units import pt
from indesigncontext.indesignbuilder import InDesignBuilder
#from indesigncontext.string import InDesignString
    
class InDesignContext(BaseContext):

    # Used by the generic BaseContext.newString( )
    #STRING_CLASS = InDesignString
    EXPORT_TYPES = (FILETYPE_IDML,)

    def __init__(self):
        """Constructor of InDesignContext.

        >>> from pagebot.document import Document
        >>> from pagebot.elements import *
        >>> from pagebot.toolbox.color import color
        >>> context = InDesignContext()
        >>> doc = Document(w=600, h=800, context=context)
        >>> page = doc[1]
        >>> e = newRect(parent=page, w=400, h=400, x=100, y=100, fill=color(1, 0, 0))
        >>> doc.export('./Image.jsx')

        """
        super().__init__()
        self.b = InDesignBuilder() # cls.b builder for this context.
        self.name = self.__class__.__name__

    def newDrawing(self, path=None):
        self.b.newDocument(path)

    def newPage(self, w, h):
        """Ignore for now in this context."""
        self.b.newPage(w, h)

    def frameDuration(self, frameDuration):
        """Ignore for now in this context."""
        pass

    def fill(self, c):
        """Ignore for now in this context."""
        pass

    def stroke(self, c, w=None):
        """Ignore for now in this context."""
        pass

    # Basic shapes.

    def rect(self, x, y, w, h):
        """Ignore for now in this context."""
        self.b.rect(x, y, w, h)

    def oval(self, x, y, w, h):
        """Ignore for now in this context."""
        pass

    def newString(self, s, e=None, style=None, w=None, h=None, pixelFit=True):
        """Creates a new styles BabelString instance of self.STRING_CLASS from
        `s` (converted to plain unicode string), using e or style as
        typographic parameters. Ignore and just answer `s` if it is already a
        self.STRING_CLASS instance and no style is forced. PageBot function.

        Ignore for now in this context."""
        return ''

    def text(self, sOrBs, p):
        """Ignore for now in this context."""
        pass

    def image(self, path, p, alpha=1, pageNumber=None, w=None, h=None):
        """Ignore for now in this context."""
        pass

    def imageSize(self, path):
        """Answers the (w, h) image size of the image file at path. If the path is an SVG
        image, then determine by parsing the SVG-XML.

        if path.lower().endswith('.'+FILETYPE_SVG):
            import xml.etree.ElementTree as ET
            svgTree = ET.parse(path)
            print(svgTree)
            return pt(1000, 1000)

        return pt(self.b.imageSize(path))
        """
        return pt(1000, 1000)

    def saveDocument(self, path, multiPage=True):
        self.b.saveDocument(path)

    saveImage = saveDocument

    def getFlattenedPath(self, path=None):
        pass

    def getFlattenedContours(self, path=None):
        pass

    def getGlyphPath(self, glyph, p=None, path=None):
        pass

if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
