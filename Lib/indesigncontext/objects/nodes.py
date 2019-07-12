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

def asNumber(v):
    try:
        vInt = int(v)
        vFloat = float(v)
        if vInt == vFloat:
            v = vInt
        else:
            v = vFloat
    except ValueError:
        pass
    return v

class IdmlNode:
    TAG = None
    PRE_XML = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>']

    def __init__(self, fileName=None, name=None, nsmap=None, prefix=None, 
            nodes=None, text=None, tail=None, attributes=None, **kwargs):
        if name is None:
            name = self.__class__.__name__
        #print('===', name, fileName)
        self.fileName = fileName
        self.tag = self.TAG or name
        self.name = name
        self.nsmap = nsmap
        self.prefix = prefix
        self.text = text
        self.tail = tail
        if nodes is None:
            nodes = []
        self.nodes = nodes
        self.attrs = {}
        if attributes is None:
            attributes = {}
        for attrName, value in attributes.items():
            if value == 'true':
                value = True
            elif value == 'false':
                value = False
            else:
                value = asNumber(value)
            self.attrs[attrName] = value

    def __getitem__(self, index):
        return self.elements[index]

    def __repr__(self):
        return '<%s>' % self.tag

    def writePreXml(self, f):
        for preXml in self.PRE_XML:
            f.write(preXml + '\n')

    def writeXml(self, f, tab=0):
        s = '%s<' % (tab*'\t')
        if self.prefix:
            s += self.prefix + ':'
        s += self.tag
        if tab == 0 and self.nsmap:
            for nsKey, nsValue in self.nsmap.items():
                if nsKey is None:
                    s += ' xmlns="%s"' % nsValue
                else:
                    s += ' xmlns:%s="%s"' % (nsKey, nsValue)
        for attrName, value in self.attrs.items():
            if value in (True, False):
                value = {True:'true',False:'false'}[value]
            elif isinstance(value, str):
                value = value.replace('&','&amp;') # Order matters
                value = value.replace('"','&quot;')  
                value = value.replace('<','&lt;')  
                value = value.replace('>','&gt;')  
            s += ' %s="%s"' % (attrName, value)
        if self.text or self.nodes:
            s += '>\n'
            f.write(s)
            if self.text is not None:
                f.write(self.text.strip())
            for node in self.nodes:
                node.writeXml(f, tab+1)
            if self.nodes:
                s = tab*'\t'
            else:
                s = ''
            s += '</'
            if self.prefix:
                s += self.prefix + ':'
            s += '%s>\n' % self.tag
            f.write(s)
        else:
            s += '/>\n'
            f.write(s)
        if self.tail is not None:
            f.write(self.tail) 

class Page(IdmlNode):
    def __init__(self, **kwargs):
        IdmlNode.__init__(self,  **kwargs)

class Properties(IdmlNode):
    pass

class Label(IdmlNode):
    pass

class KeyValuePair(IdmlNode):
    pass

class Language(IdmlNode):
    pass

class idPkg_Graphic(IdmlNode):
    TAG = 'idPkg:Graphic'

class idPkg_Fonts(IdmlNode):
    TAG = 'idPkg:Fonts'

class idPkg_Styles(IdmlNode):
    TAG = 'idPkg:Styles'

class idPkg_Preferences(IdmlNode):
    TAG = 'idPkg:Preferences'

class idPkg_Tags(IdmlNode):
    TAG = 'idPkg:Tags'

class idPkg_MasterSpread(IdmlNode):
    TAG = 'idPkg:MasterSpread'

#class idPkg_Spread(IdmlNode):
#    TAG = 'idPkg:Spread'

class idPkg_BackingStory(IdmlNode):
    TAG = 'idPkg:BackingStory'

class NumberingList(IdmlNode):
    pass

class NamedGrid(IdmlNode):
    pass

class GridDataInformation(IdmlNode):
    pass

class EndnoteOption(IdmlNode):
    pass

class TextFrameFootnoteOptionsObject(IdmlNode):
    pass

class LinkedStoryOption(IdmlNode):
    pass

class LinkedPageItemOption(IdmlNode):
    pass

class TaggedPDFPreference(IdmlNode):
    pass

class WatermarkPreference(IdmlNode):
    pass

class ConditionalTextPreference(IdmlNode):
    pass

class AdjustLayoutPreference(IdmlNode):
    pass

class HTMLFXLExportPreference(IdmlNode):
    pass

class PublishExportPreference(IdmlNode):
    pass

class TextVariable(IdmlNode):
    pass

class ChapterNumberVariablePreference(IdmlNode):
    pass

class DateVariablePreference(IdmlNode):
    pass

class FileNameVariablePreference(IdmlNode):
    pass

class CaptionMetadataVariablePreference(IdmlNode):
    pass

class PageNumberVariablePreference(IdmlNode):
    pass

class MatchParagraphStylePreference(IdmlNode):
    pass

class Layer(IdmlNode):
    pass

class Section(IdmlNode):
    pass

class DocumentUser(IdmlNode):
    pass

class CrossReferenceFormat(IdmlNode):
    pass

class BuildingBlock(IdmlNode):
    pass

class IndexingSortOption(IdmlNode):
    pass

class ColorGroup(IdmlNode):
    pass

class ColorGroupSwatch(IdmlNode):
    pass

class ABullet(IdmlNode):
    pass

class Assignment(IdmlNode):
    pass


class IdmlValueNode(IdmlNode):
    def writeXml(self, f, tab=0):
        f.write(('\t'*tab) + '<%s type="%s">%s</%s>\n' % (
            self.tag, self.attrs['type'], self.attrs['value'], self.tag)
        )

class AppliedFont(IdmlValueNode):
    pass
class EndnoteNumberingStyle(IdmlValueNode):
    pass
class RestartEndnoteNumbering(IdmlValueNode):
    pass
class EndnoteMarkerPositioning(IdmlValueNode):
    pass
class ScopeValue(IdmlValueNode):
    pass
class FrameCreateOption(IdmlValueNode):
    pass
class FrameColor(IdmlValueNode):
    pass
class ShowEndnotePrefixSuffix(IdmlValueNode):
    pass
class WatermarkFontColor(IdmlValueNode):
    pass
class LayerColor(IdmlValueNode):
    pass
class PageNumberStyle(IdmlValueNode):
    pass
class UserColor(IdmlValueNode):
    pass
class BulletsFont(IdmlValueNode):
    pass
class BulletsFontStyle(IdmlValueNode):
    pass


NODE_CLASSES = {
    # Expanding set of IdmlNode classes, that know more about their
    # content so the can generate, manipulate and validate. 
    'IdmlNode': IdmlNode,
    'Page': Page,
    'Properties': Properties,
    'Label': Label,
    'KeyValuePair': KeyValuePair,
    'Language': Language,
    'idPkg:Graphic': idPkg_Graphic,
    'idPkg:Fonts': idPkg_Fonts,
    'idPkg:Styles': idPkg_Styles,
    'idPkg:Preferences': idPkg_Preferences,
    'idPkg:Tags': idPkg_Tags,
    'idPkg:MasterSpread': idPkg_MasterSpread,
    #'idPkg:Spread': idPkg_Spread,
    'idPkg:BackingStory': idPkg_BackingStory,
    'NumberingList': NumberingList,
    'NamedGrid': NamedGrid,
    'GridDataInformation': GridDataInformation,
    'EndnoteOption': EndnoteOption,
    'AppliedFont': AppliedFont,
    'EndnoteNumberingStyle': EndnoteNumberingStyle,
    'RestartEndnoteNumbering': RestartEndnoteNumbering,
    'EndnoteMarkerPositioning': EndnoteMarkerPositioning,
    'ScopeValue': ScopeValue,
    'FrameCreateOption': FrameCreateOption,
    'ShowEndnotePrefixSuffix': ShowEndnotePrefixSuffix,
    'TextFrameFootnoteOptionsObject': TextFrameFootnoteOptionsObject,
    'LinkedStoryOption': LinkedStoryOption,
    'LinkedPageItemOption': LinkedPageItemOption,
    'TaggedPDFPreference': TaggedPDFPreference,
    'WatermarkPreference': WatermarkPreference,
    'WatermarkFontColor': WatermarkFontColor,
    'ConditionalTextPreference': ConditionalTextPreference,
    'AdjustLayoutPreference': AdjustLayoutPreference,
    'HTMLFXLExportPreference': HTMLFXLExportPreference,
    'PublishExportPreference': PublishExportPreference,
    'ChapterNumberVariablePreference': ChapterNumberVariablePreference,
    'DateVariablePreference': DateVariablePreference,
    'FileNameVariablePreference': FileNameVariablePreference,
    'CaptionMetadataVariablePreference': CaptionMetadataVariablePreference,
    'PageNumberVariablePreference': PageNumberVariablePreference,
    'MatchParagraphStylePreference': MatchParagraphStylePreference,
    'Layer': Layer,
    'LayerColor': LayerColor,
    'PageNumberStyle': PageNumberStyle,
    'UserColor': UserColor,
    'CrossReferenceFormat': CrossReferenceFormat,
    'BuildingBlock': BuildingBlock,
    'IndexingSortOption': IndexingSortOption,
    'ColorGroup': ColorGroup,
    'ColorGroupSwatch': ColorGroupSwatch,
    'ABullet': ABullet,
    'BulletsFont': BulletsFont,
    'BulletsFontStyle': BulletsFontStyle,
    'Assignment': Assignment,
    'FrameColor': FrameColor,
}

if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
