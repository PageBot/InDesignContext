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
#     Supporting Indesign, xxyxyz.org/indesign
# -----------------------------------------------------------------------------
#
#     indesignstring.py
#

import os, re, copy

from pagebot.strings.babelstring import BabelString
from pagebot.style import css
from pagebot.constants import LEFT, DEFAULT_FONT_SIZE, DEFAULT_LEADING
from pagebot.paths import DEFAULT_FONT_PATH
from pagebot.toolbox.units import isUnit
from pagebot.fonttoolbox.objects.font import findFont

class InDesignString(BabelString):
    """InDesignString is a wrapper around the Indesign string."""

    BABEL_STRING_TYPE = 'indesign'

    def __init__(self, s, context, style=None):
        """Constructor of the InDesignString. Optionally store the (latest)
        style that was used to produce the formatted string.

        >>> from indesigncontext.context import InDesignContext
        >>> from pagebot.toolbox.units import pt
        >>> context = InDesignContext()
        >>> bs = context.newString('ABC')
        >>> bs.s, bs.style
        ('ABC', {})
        >>> bs.style['fontSize'] = pt(12)
        >>> bs.style
        {'fontSize': 12pt}
        >>> bs.style = dict(font=findFont('Roboto-Regular'), fontSize=pt(23))
        >>> bs.style['font'], bs.style['fontSize']
        (<Font Roboto-Regular>, 23pt)
        """
        if style is None:
            style = {}
        self.context = context # Store context, in case we need more of its functions.
        self.runs = [[str(s), copy.copy(style)]] # Format is [(s1, style1), (s2, style2), ...]

    def __add__(self, bs):
        """Adds bs to self.

        >>> from indesigncontext.context import InDesignContext
        >>> from pagebot.toolbox.units import pt
        >>> context = InDesignContext()
        >>> bs1 = context.newString('ABCD', style=dict(fontSize=pt(21)))
        >>> bs1.s, bs1.style
        ('ABCD', {'fontSize': 21pt})
        >>> bs2 = context.newString('EFGH', style=dict(fontSize=pt(23)))
        >>> bs2.s, bs2.style
        ('EFGH', {'fontSize': 23pt})
        >>> bs1 += bs2
        >>> bs1.runs
        [['ABCD', {'fontSize': 21pt}], ['EFGH', {'fontSize': 23pt}]]
        >>> bs1 += 'IJKL'
        >>> bs1.runs
        [['ABCD', {'fontSize': 21pt}], ['EFGH', {'fontSize': 23pt}], ['IJKL', {}]]
        """
        if isinstance(bs, self.__class__):
            self.runs += bs.runs
        else:
            self.runs.append([str(bs), {}])
        return self

    def _get_style(self):
        """Answers the last style of the runs. Otherwise answer None.

        >>> from indesigncontext.context import InDesignContext
        >>> from pagebot.toolbox.units import pt
        >>> style = dict(fontSize=pt(21))
        >>> context = InDesignContext()
        >>> bs = context.newString('ABCD', style=style)
        >>> bs.s, bs.style
        ('ABCD', {'fontSize': 21pt})
        """
        if self.runs:
            return self.runs[-1][1]
        return None
    def _set_style(self, style):
        """Replace the style of the last run by a copy of @style.
        If there are no runs, then add the style with an empty string.

        >>> from indesigncontext.context import InDesignContext
        >>> from pagebot.toolbox.units import pt
        >>> style = dict(fontSize=pt(21))
        >>> context = InDesignContext()
        >>> bs = context.newString('ABCD', style=style)
        >>> bs.s, bs.style
        ('ABCD', {'fontSize': 21pt})
        """
        if self.runs:
            self.runs[-1][1] = copy.copy(style)
        else:
            self.runs = ['', copy.copy(style)]
    style = property(_get_style, _set_style)

    def _get_s(self):
        """Answers the embedded InDesign equivalent of a OSX FormattedString by
        property, to enforce checking type of the string. Setting by self.s
        will completely replace the current content of self.runs

        >>> from indesigncontext.context import InDesignContext
        >>> from pagebot.toolbox.units import pt
        >>> context = InDesignContext()
        >>> bs = context.newString('ABCD', style=dict(font=findFont('Roboto-Regular')))
        >>> bs.s
        'ABCD'
        >>> bs.s = 'EFGH' # Replace the runs
        >>> bs.runs
        [('EFGH', {})]
        """
        runs = []
        for s, style in self.runs:
            runs.append(s)
        return ''.join(runs)
    def _set_s(self, s):
        self.runs = [(s, {})]
    s = property(_get_s, _set_s)

    def _get_font(self):
        """Answers the current state of fontName.

        >>> from indesigncontext.context import InDesignContext
        >>> from pagebot.toolbox.units import pt
        >>> context = InDesignContext()
        >>> bs = context.newString('ABCD', style=dict(font=findFont('Roboto-Regular')))
        >>> bs.font
        <Font Roboto-Regular>
        >>> bs.font = findFont('Roboto-Bold') # Set the font of the last run
        >>> bs.font, bs.font == bs.runs[-1][1]['font']
        (<Font Roboto-Bold>, True)
        """
        style = self.style
        if style is not None:
            return style.get('font')
        return None
    def _set_font(self, font):
        style = self.style
        if style is not None and font is not None:
            style['font'] = font
    font = property(_get_font, _set_font)

    def _get_fontSize(self):
        """Answers the current state of the fontSize.

        >>> from indesigncontext.context import InDesignContext
        >>> from pagebot.toolbox.units import pt
        >>> context = InDesignContext()
        >>> bs = context.newString('ABCD', style=dict(fontSize=pt(21)))
        >>> bs.fontSize
        21pt
        >>> bs.fontSize = pt(23)
        >>> bs.fontSize, bs.fontSize == bs.runs[-1][1]['fontSize']
        (23pt, True)
        """
        style = self.style
        if style is not None:
            return style.get('fontSize')
        return None
    def _set_fontSize(self, fontSize):
        style = self.style
        if style is not None and fontSize is not None:
            style['fontSize'] = fontSize
    fontSize = property(_get_fontSize, _set_fontSize)

    def __len__(self):
        """Answers the number of characters in self.s

        >>> from indesigncontext.context import InDesignContext
        >>> context = InDesignContext()
        >>> bs = InDesignString('ABC', context)
        >>> fs
        ABC
        >>> len(fs)
        3
        """
        return len(self.asText())

    def asText(self):
        """Answers as unicode string.

        >>> from indesigncontext.context import InDesignContext
        >>> context = InDesignContext()
        >>> fs = InDesignString('ABC', context)
        >>> bs.runs

        >>> fs.s
        'ABC'
        >>> fs.asText()
        'ABC'
        """
        return str(self.s) # TODO: To be changed to Indesign string behavior.

    def textSize(self, w=None, h=None):
        """Answers the (w, h) size for a given width, with the current text."""
        return 100, 20
        # TODO: Make this work in Indesign same as in DrawBot
        #return self.b.textSize(s)

    def textOverflow(self, w, h, align=LEFT):
        # TODO: Make this work in Indesign same as in DrawBot
        # TODO: Some stuff needs to get here.
        return ''

    def append(self, s):
        """Append string or InDesignString to self."""
        # TODO: Make this to work.
        #try:
        #    self.s += s.s
        #except TypeError:
        #    self.s += repr(s) # Convert to babel string, whatever it is.

    MARKER_PATTERN = '==%s@%s=='
    FIND_FS_MARKERS = re.compile('\=\=([a-zA-Z0-9_\:\.]*)\@([^=]*)\=\=')

    def appendMarker(self, markerId, arg):
        """Append an invisible marker string."""

    def findMarkers(self, reCompiled=None):
        """Answers a dictionary of markers with their arguments in self.s."""
        if reCompiled is None:
            reCompiled= self.FIND_FS_MARKERS
        return reCompiled.findall(u'%s' % self.s)

    @classmethod
    def newString(cls, s, context, e=None, style=None, w=None, h=None, pixelFit=True):
        """Answers a InDesignString instance from valid attributes in *style*.
        Set all values after testing their existence, so they can inherit from
        previous style formats. If target width *w* or height *h* is defined,
        then *fontSize* is scaled to make the string fit *w* or *h*.

        >>> from pagebot.toolbox.units import pt
        >>> from indesigncontext.context import InDesignContext
        >>> context = InDesignContext()
        >>> bs = InDesignString.newString('AAA', context, style=dict(fontSize=pt(30)))
        >>> #bs.s.lines()
        >>> #'indesign.text.text' in str(bs)
        True
        """
        if style is None:
            style = {}

        sUpperCase = css('uppercase', e, style)
        sLowercase = css('lowercase', e, style)
        sCapitalized = css('capitalized', e, style)

        if sUpperCase:
            s = s.upper()
        elif sLowercase:
            s = s.lower()
        elif sCapitalized:
            s = s.capitalize()

        # Since Indesign does not do font GSUB feature compile, we'll make the
        # transformed string here, using Tal's
        #
        # https://github.com/typesupply/compositor
        #
        # This needs to be installed, in case PageBot is running outside of DrawBot.

        font = style.get('font')

        if font is not None and not isinstance(font, str):
            font = font.path
        if font is None or not os.path.exists(font):
            font = DEFAULT_FONT_PATH

        fontSize = style.get('fontSize', DEFAULT_FONT_SIZE)
        assert isUnit(fontSize), ('%s.newString: FontSize %s must be of type Unit' % (cls.__name__, fontSize))
        leading = style.get('leading', DEFAULT_LEADING)
        assert isUnit(leading), ('%s.newString: Leading %s must be of type Unit' % (cls.__name__, leading))
        inDesignFont = findFont(font)
        #strike = context.b.strike(indesignFont)
        #strike.size(fontSize.pt, leading.pt, units='pt')
        #if w is not None:
        #    strike.width = w
        #s = strike.text(s)
        s = ''
        return cls(s, context=context, style=style) # Make real Indesign flavor BabelString here.

if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
