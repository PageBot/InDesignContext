# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#
# -----------------------------------------------------------------------------
#
from idmlcontext.objects.nodes import *

class BackingStory(IdmlNode):
    TAG = 'idPkg:BackingStory'
    PRE_XML = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
    ]
    def __init__(self, attributes=None, **kwargs):
        if attributes is None:
            attributes = {}
            attributes['xmlns:idPkg'] = "http://ns.adobe.com/AdobeInDesign/idml/1.0/packaging"
            attributes['DOMVersion'] = '14.0'
        IdmlNode.__init__(self, attributes=attributes, **kwargs)


if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
