
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
#     constants.py
#
JSX_LIB = """
function pbGetColor(doc, c){
    if (c.length == 4){
        colorName = "C=" + Math.round(c[0]) + " M=" + Math.round(c[1]) +" Y=" + Math.round(c[2]) + " K=" + Math.round(c[3]);  
        colorSpace = ColorSpace.cmyk;
        colorModel = ColorModel.process;
    } else {
        colorName = "R=" + Math.round(c[0]) + " G=" + Math.round(c[1]) +" B=" + Math.round(c[2]);  
        colorSpace = ColorSpace.rgb;
        colorModel = ColorModel.process;
    }
    try {
        pbColor = doc.colors.add({
            name: colorName, 
            model: colorModel,
            space: colorSpace, 
            colorValue: c});
    } 
    catch (e) {
        pbColor = doc.swatches.item(colorName);
    }
    //alert(colorName);
    return(pbColor);
}
function myScriptPath(){
    return(File(app.activeScript).parent + '/');
}
"""

if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
