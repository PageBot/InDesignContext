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

class DesignMap(IdmlNode):
    TAG = 'Document'
    PRE_XML = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<?aid style="50" type="document" readerVersion="6.0" featureSet="257" product="14.0(324)"?>'
    ]
    def __init__(self, attributes=None, **kwargs):
        if attributes is None:
            attributes = {}
            attributes['xmlns:idPkg'] = "http://ns.adobe.com/AdobeInDesign/idml/1.0/packaging"
            attributes['DOMVersion'] = "14.0"
            attributes['Self'] = "d"
            attributes['StoryList'] = "u91"
            attributes['Name'] = "MagentaYellowRectangle.indd"
            attributes['ZeroPoint'] = "0 0" 
            attributes['ActiveLayer'] = "ub1" 
            attributes['CMYKProfile'] = "U.S. Web Coated (SWOP) v2"
            attributes['RGBProfile'] = "sRGB IEC61966-2.1"
            attributes['SolidColorIntent'] = "UseColorSettings"
            attributes['AfterBlendingIntent'] = "UseColorSettings"
            attributes['DefaultImageIntent'] = "UseColorSettings"
            attributes['RGBPolicy'] = "PreserveEmbeddedProfiles"
            attributes['CMYKPolicy'] = "CombinationOfPreserveAndSafeCmyk"
            attributes['AccurateLABSpots'] = False
        IdmlNode.__init__(self, attributes=attributes, **kwargs)

        properties = Properties(
            nodes=[Label(
                nodes=[KeyValuePair(attributes=dict(
                    Key="kAdobeDPS_Version", Value=2
                ))]
            )]
        )
        self.nodes.append(properties)
        self.nodes.append(Language(attributes=dict(Self="Language/$ID/English%3a USA",
            Name="$ID/English: USA",
            SingleQuotes="‘’",
            DoubleQuotes="“”",
            PrimaryLanguageName="$ID/English",
            SublanguageName="$ID/USA",
            Id=269,
            HyphenationVendor="Hunspell",
            SpellingVendor="Hunspell")))
        self.nodes.append(idPkg_Graphic(attributes=dict(src='Resources/Graphic.xml')))
        self.nodes.append(idPkg_Fonts(attributes=dict(src='Resources/Fonts.xml')))
        self.nodes.append(idPkg_Styles(attributes=dict(src='Resources/Styles.xml')))
        self.nodes.append(NumberingList(attributes=dict(
            Self="NumberingList/$ID/[Default]",
            Name="$ID/[Default]",
            ContinueNumbersAcrossStories=False,
            ContinueNumbersAcrossDocuments=False)))
        
        namedGrid = NamedGrid(attributes=dict(
            Self="NamedGrid/$ID/[Page Grid]",
            Name="$ID/[Page Grid]"),
            nodes=[GridDataInformation(attributes=dict(
                FontStyle="Regular",
                PointSize=12,
                CharacterAki=0,
                LineAki=9,
                HorizontalScale=100,
                VerticalScale=100,
                LineAlignment="LeftOrTopLineJustify",
                GridAlignment="AlignEmCenter",
                CharacterAlignment="AlignEmCenter",
                ),
                nodes=[Properties(nodes=[AppliedFont(attributes=dict(type='string', value='Minion Pro'))])]
            )]
        )
        self.nodes.append(namedGrid)
        self.nodes.append(idPkg_Preferences(attributes=dict(src='Resources/Preferences.xml')))

        self.nodes.append(EndnoteOption(attributes=dict(
            EndnoteTitle="Endnotes",
            EndnoteTitleStyle="ParagraphStyle/$ID/NormalParagraphStyle",
            StartEndnoteNumberAt="1",
            EndnoteMarkerStyle="CharacterStyle/$ID/[No character style]",
            EndnoteTextStyle="ParagraphStyle/$ID/NormalParagraphStyle",
            EndnoteSeparatorText="&#x9;",
            EndnotePrefix="",
            EndnoteSuffix=""),
            nodes=[Properties(nodes=[
                EndnoteNumberingStyle(attributes=dict(type='enumeration', value='Arabic')),
                RestartEndnoteNumbering(attributes=dict(type='enumeration', value='Continuous')),
                EndnoteMarkerPositioning(attributes=dict(type='enumeration', value='SuperscriptMarker')),
                ScopeValue(attributes=dict(type='enumeration', value='EndnoteDocumentScope')),
                FrameCreateOption(attributes=dict(type='enumeration', value='NewPage')),
                ShowEndnotePrefixSuffix(attributes=dict(type='enumeration', value='NoPrefixSuffix')),
            ])]
        ))
        self.nodes.append(TextFrameFootnoteOptionsObject(attributes=dict(
            EnableOverrides=False,
            SpanFootnotesAcross=False,
            MinimumSpacingOption=12,
            SpaceBetweenFootnotes=6,
        )))
        self.nodes.append(LinkedStoryOption(attributes=dict(
            UpdateWhileSaving=False,
            WarnOnUpdateOfEditedStory=True,
            RemoveForcedLineBreaks=False,
            ApplyStyleMappings=False,
        )))
        self.nodes.append(LinkedPageItemOption(attributes=dict(
            UpdateLinkWhileSaving=False,
            WarnOnUpdateOfEditedPageItem=True,
            PreserveSizeAndShape=False,
            PreserveAppearance=False,
            PreserveInteractivity=False,
            PreserveFrameContent=False,
            PreserveOthers=False,
        )))
        self.nodes.append(TaggedPDFPreference(attributes=dict(
            StructureOrder="UseXMLStructure",
        )))
        self.nodes.append(WatermarkPreference(attributes=dict(
            WatermarkVisibility=False,
            WatermarkDoPrint=False,
            WatermarkDrawInBack=True,
            WatermarkText="",
            WatermarkFontFamily="Minion Pro",
            WatermarkFontStyle="Regular",
            WatermarkFontPointSize=48,
            WatermarkOpacity=50,
            WatermarkRotation=0,
            WatermarkHorizontalPosition="WatermarkHCenter",
            WatermarkHorizontalOffset=0,
            WatermarkVerticalPosition="WatermarkVCenter",
            WatermarkVerticalOffset=0,
            ),
            nodes=[Properties(nodes=[WatermarkFontColor(attributes=dict(
                type='enumeration', value='Black'))])]
        ))
        self.nodes.append(ConditionalTextPreference(attributes=dict(
            ShowConditionIndicators="ShowIndicators",
            ActiveConditionSet="n"
        )))
        self.nodes.append(AdjustLayoutPreference(attributes=dict(
            EnableAdjustLayout=False,
            AllowLockedObjectsToAdjust=True,
            AllowFontSizeAndLeadingAdjustment=False,
            ImposeFontSizeRestriction=False,
            MinimumFontSize=6,
            MaximumFontSize=324,
            EnableAutoAdjustMargins=False,
        )))
        self.nodes.append(HTMLFXLExportPreference(attributes=dict(
            EpubPageRange="",
            EpubPageRangeFormat="ExportAllPages",
        )))
        self.nodes.append(PublishExportPreference(attributes=dict(
            PublishCover="FirstPage",
            CoverImageFile="",
            PublishPageRange="",
            PublishPageRangeFormat="ExportAllPages",
            ImageConversion="Automatic",
            ImageExportResolution="Ppi96",
            PublishDescription="",
            PublishFileName="",
            PublishFormat="PublishByPages",
            CoverPage="$ID/",
            GIFOptionsPalette="AdaptivePalette",
            JPEGOptionsQuality="High",
            PublishPdf=False
        )))
        self.nodes.append(TextVariable(attributes=dict(
            Self="dTextVariablen&lt;?AID 001b?&gt;TV XRefChapterNumber",
            Name="&lt;?AID 001b?&gt;TV XRefChapterNumber",
            VariableType="XrefChapterNumberType",
        )))
        self.nodes.append(TextVariable(attributes=dict(
            Self="dTextVariablen&lt;?AID 001b?&gt;TV XRefPageNumber",
            Name="&lt;?AID 001b?&gt;TV XRefPageNumber",
            VariableType="XrefPageNumberType",
        )))
        self.nodes.append(TextVariable(attributes=dict(
            Self="dTextVariablenChapter Number",
            Name="Chapter Number",
            VariableType="ChapterNumberType",
            ),
            nodes=[ChapterNumberVariablePreference(attributes=dict(
                TextBefore="",
                Format="Current",
                TextAfter="",
            ))]
        ))
        self.nodes.append(TextVariable(attributes=dict(
            Self="dTextVariablenCreation Date",
            Name="Creation Date",
            VariableType="CreationDateType",
            ),
            nodes=[DateVariablePreference(attributes=dict(
                TextBefore="",
                Format="MM/dd/yy",
                TextAfter="",
            ))]
        ))
        self.nodes.append(TextVariable(attributes=dict(
            Self="dTextVariablenFile Name",
            Name="File Name",
            VariableType="FileNameType",
            ),
            nodes=[FileNameVariablePreference(attributes=dict(
                TextBefore="",
                IncludePath=False,
                IncludeExtension=False,
                TextAfter=""
            ))]
        ))
        self.nodes.append(TextVariable(attributes=dict(
            Self="dTextVariablenImage Name",
            Name="Image Name",
            VariableType="LiveCaptionType",
            ),
            nodes=[CaptionMetadataVariablePreference(attributes=dict(
                TextBefore="",
                MetadataProviderName="$ID/#LinkInfoNameStr",
                TextAfter="" 
            ))]
        ))
        self.nodes.append(TextVariable(attributes=dict(
            Self="dTextVariablenLast Page Number",
            Name="Last Page Number",
            VariableType="LastPageNumberType",
            ),
            nodes=[PageNumberVariablePreference(attributes=dict(
                TextBefore="",
                Format="Current",
                TextAfter="",
                Scope="SectionScope",
            ))]
        ))
        self.nodes.append(TextVariable(attributes=dict(
            Self="dTextVariablenModification Date",
            Name="Modification Date",
            VariableType="ModificationDateType",
            ),
            nodes=[DateVariablePreference(attributes=dict(
                TextBefore="",
                Format="MMMM d, yyyy h:mm aa",
                TextAfter="",
            ))]
        ))
        self.nodes.append(TextVariable(attributes=dict(
            Self="dTextVariablenOutput Date",
            Name="Output Date",
            VariableType="OutputDateType",
            ),
            nodes=[DateVariablePreference(attributes=dict(
                TextBefore="",
                Format="MM/dd/yy",
                TextAfter="",
            ))]
        ))
        self.nodes.append(TextVariable(attributes=dict(
            Self="dTextVariablenRunning Header",
            Name="Running Header",
            VariableType="MatchParagraphStyleType",
            ),
            nodes=[MatchParagraphStylePreference(attributes=dict(
                TextBefore="",
                TextAfter="",
                AppliedParagraphStyle="ParagraphStyle/$ID/NormalParagraphStyle",
                SearchStrategy="FirstOnPage",
                ChangeCase="None",
                DeleteEndPunctuation=False,
            ))]
        ))
        self.nodes.append(idPkg_Tags(attributes=dict(src="XML/Tags.xml")))
        self.nodes.append(Layer(attributes=dict(
            Self="ub1",
            Name="Layer 1",
            Visible=True,
            Locked=False,
            IgnoreWrap=False,
            ShowGuides=True,
            LockGuides=False,
            UI=True,
            Expendable=True,
            Printable=True,
            ),
            nodes=[Properties(nodes=[LayerColor(attributes=dict(
                type='enumeration', value='LightBlue'))]
            )]
        ))
        self.nodes.append(idPkg_MasterSpread(attributes=dict(src='MasterSpreads/MasterSpread_ub2.xml')))
        self.nodes.append(idPkg_Spread(attributes=dict(src='Spreads/Spread_udc.xml')))
        self.nodes.append(Section(attributes=dict(
            Self="uad",
            Length=1,
            Name="",
            ContinueNumbering=True,
            IncludeSectionPrefix=False,
            Marker="",
            PageStart="ue1",
            SectionPrefix="",
            AlternateLayoutLength=1,
            AlternateLayout="Letter V",
            ),
            nodes=[Properties(nodes=[PageNumberStyle(attributes=dict(
                type='enumeration', value='Arabic'))]
            )]
        ))
        self.nodes.append(DocumentUser(attributes=dict(
            Self="dDocumentUser0",
            UserName="$ID/Unknown User Name",
            ),
            nodes=[Properties(nodes=[UserColor(attributes=dict(
                type='enumeration', value='Gold'))]
            )]
        ))
        self.nodes.append(CrossReferenceFormat(attributes=dict(
            Self="ue4",
            Name="Full Paragraph &amp; Page Number",
            AppliedCharacterStyle="n",
            ),
            nodes=[
                BuildingBlock(attributes=dict(
                    Self="ue4BuildingBlock0",
                    BlockType="CustomStringBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="&quot;",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
                BuildingBlock(attributes=dict(
                    Self="ue4BuildingBlock1",
                    BlockType="FullParagraphBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="$ID/",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
                BuildingBlock(attributes=dict(
                    Self="ue4BuildingBlock2",
                    BlockType="CustomStringBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="&quot; on page ",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
                BuildingBlock(attributes=dict(
                    Self="ue4BuildingBlock3",
                    BlockType="PageNumberBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="$ID/",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False))
            ]
        ))
        self.nodes.append(CrossReferenceFormat(attributes=dict(
            Self="ue5",
            Name="Full Paragraph",
            AppliedCharacterStyle="n",
            ),
            nodes=[
                BuildingBlock(attributes=dict(
                    Self="ue5BuildingBlock0",
                    BlockType="CustomStringBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="&quot;",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
                BuildingBlock(attributes=dict(
                    Self="ue5BuildingBlock1",
                    BlockType="FullParagraphBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="$ID/",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
                BuildingBlock(attributes=dict(
                    Self="ue5BuildingBlock2",
                    BlockType="CustomStringBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="&quot;",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
            ]
        ))
        self.nodes.append(CrossReferenceFormat(attributes=dict(
            Self="ue6",
            Name="Paragraph Text &amp; Page Number",
            AppliedCharacterStyle="n",
            ),
            nodes=[
                BuildingBlock(attributes=dict(
                    Self="ue6BuildingBlock0",
                    BlockType="CustomStringBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="&quot;",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
                BuildingBlock(attributes=dict(
                    Self="ue6BuildingBlock1",
                    BlockType="ParagraphTextBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="$ID/",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
                BuildingBlock(attributes=dict(
                    Self="ue6BuildingBlock2",
                    BlockType="CustomStringBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="&quot; on page ",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
                BuildingBlock(attributes=dict(
                    Self="ue6BuildingBlock3",
                    BlockType="PageNumberBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="$ID/",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
            ]
        ))
        self.nodes.append(CrossReferenceFormat(attributes=dict(
            Self="ue7",
            Name="Paragraph Text",
            AppliedCharacterStyle="n",
            ),
            nodes=[
                BuildingBlock(attributes=dict(
                    Self="ue7BuildingBlock0",
                    BlockType="CustomStringBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="&quot;",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
                BuildingBlock(attributes=dict(
                    Self="ue7BuildingBlock1",
                    BlockType="ParagraphTextBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="$ID/",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
                BuildingBlock(attributes=dict(
                    Self="ue7BuildingBlock2",
                    BlockType="CustomStringBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="&quot;",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
            ]
        ))
        self.nodes.append(CrossReferenceFormat(attributes=dict(
            Self="ue8",
            Name="Paragraph Number &amp; Page Number",
            AppliedCharacterStyle="n",
            ),
            nodes=[
                BuildingBlock(attributes=dict(
                    Self="ue8BuildingBlock0",
                    BlockType="ParagraphNumberBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="$ID/",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
                BuildingBlock(attributes=dict(
                    Self="ue8BuildingBlock1",
                    BlockType="CustomStringBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText=" on page ",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
                BuildingBlock(attributes=dict(
                    Self="ue8BuildingBlock2",
                    BlockType="PageNumberBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="$ID/",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
            ]
        ))
        self.nodes.append(CrossReferenceFormat(attributes=dict(
            Self="ue9",
            Name="Paragraph Number",
            AppliedCharacterStyle="n",
            ),
            nodes=[
                BuildingBlock(attributes=dict(
                    Self="ue9BuildingBlock0",
                    BlockType="ParagraphNumberBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="$ID/",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
            ]
        ))
        self.nodes.append(CrossReferenceFormat(attributes=dict(
            Self="uea",
            Name="Text Anchor Name &amp; Page Number",
            AppliedCharacterStyle="n",
            ),
            nodes=[
                BuildingBlock(attributes=dict(
                    Self="ueaBuildingBlock0",
                    BlockType="CustomStringBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="&quot;",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
                BuildingBlock(attributes=dict(
                    Self="ueaBuildingBlock1",
                    BlockType="BookmarkNameBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="$ID/",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
                BuildingBlock(attributes=dict(
                    Self="ueaBuildingBlock2",
                    BlockType="CustomStringBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="&quot; on page ",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
                BuildingBlock(attributes=dict(
                    Self="ueaBuildingBlock3",
                    BlockType="PageNumberBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="$ID/",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
            ]
        ))
        self.nodes.append(CrossReferenceFormat(attributes=dict(
            Self="ueb",
            Name="Text Anchor Name",
            AppliedCharacterStyle="n",
            ),
            nodes=[
                BuildingBlock(attributes=dict(
                    Self="uebBuildingBlock0",
                    BlockType="CustomStringBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="&quot;",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
                BuildingBlock(attributes=dict(
                    Self="uebBuildingBlock1",
                    BlockType="BookmarkNameBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="$ID/",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
                BuildingBlock(attributes=dict(
                    Self="uebBuildingBlock2",
                    BlockType="CustomStringBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="&quot;",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
            ]
        ))
        self.nodes.append(CrossReferenceFormat(attributes=dict(
            Self="uec",
            Name="Page Number",
            AppliedCharacterStyle="n",
            ),
            nodes=[
                BuildingBlock(attributes=dict(
                    Self="uecBuildingBlock0",
                    BlockType="CustomStringBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="page ",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
                BuildingBlock(attributes=dict(
                    Self="uecBuildingBlock1",
                    BlockType="PageNumberBuildingBlock",
                    AppliedCharacterStyle="n",
                    CustomText="$ID/",
                    AppliedDelimiter="$ID/",
                    IncludeDelimiter=False)),
            ]
        ))
        self.nodes.append(idPkg_BackingStory(attributes=dict(src='XML/BackingStory.xml')))
        self.nodes.append(IndexingSortOption(attributes=dict(
            Self="dIndexingSortOptionnkIndexGroup_Symbol",
            Name="$ID/kIndexGroup_Symbol",
            Include=True,
            Priority=0,
            HeaderType="Nothing")))
        self.nodes.append(IndexingSortOption(attributes=dict(
            Self="dIndexingSortOptionnkIndexGroup_Alphabet",
            Name="$ID/kIndexGroup_Alphabet",
            Include=True,
            Priority=1,
            HeaderType="BasicLatin")))
        self.nodes.append(IndexingSortOption(attributes=dict(
            Self="dIndexingSortOptionnkIndexGroup_Numeric",
            Name="$ID/kIndexGroup_Numeric",
            Include=False,
            Priority=2,
            HeaderType="Nothing")))
        self.nodes.append(IndexingSortOption(attributes=dict(
            Self="dIndexingSortOptionnkWRIndexGroup_GreekAlphabet",
            Name="$ID/kWRIndexGroup_GreekAlphabet",
            Include=False,
            Priority=3,
            HeaderType="Nothing")))
        self.nodes.append(IndexingSortOption(attributes=dict(
            Self="dIndexingSortOptionnkWRIndexGroup_CyrillicAlphabet",
            Name="$ID/kWRIndexGroup_CyrillicAlphabet",
            Include=False,
            Priority=4,
            HeaderType="Russian")))
        self.nodes.append(IndexingSortOption(attributes=dict(
            Self="dIndexingSortOptionnkIndexGroup_Kana",
            Name="$ID/kIndexGroup_Kana",
            Include=False,
            Priority=5,
            HeaderType="HiraganaAll")))
        self.nodes.append(IndexingSortOption(attributes=dict(
            Self="dIndexingSortOptionnkIndexGroup_Chinese",
            Name="$ID/kIndexGroup_Chinese",
            Include=False,
            Priority=6,
            HeaderType="ChinesePinyin")))
        self.nodes.append(IndexingSortOption(attributes=dict(
            Self="dIndexingSortOptionnkIndexGroup_Korean",
            Name="$ID/kIndexGroup_Korean",
            Include=False,
            Priority=7,
            HeaderType="KoreanConsonant")))
        self.nodes.append(IndexingSortOption(attributes=dict(
            Self="dIndexingSortOptionnkWRIndexGroup_ArabicAlphabet",
            Name="$ID/kWRIndexGroup_ArabicAlphabet",
            Include=False,
            Priority=8,
            HeaderType="Nothing")))
        self.nodes.append(IndexingSortOption(attributes=dict(
            Self="dIndexingSortOptionnkWRIndexGroup_HebrewAlphabet",
            Name="$ID/kWRIndexGroup_HebrewAlphabet",
            Include=False,
            Priority=9,
            HeaderType="Nothing")))
        self.nodes.append(ColorGroup(attributes=dict(
            Self="ColorGroup/[Root Color Group]",
            Name="[Root Color Group]",
            IsRootColorGroup=True),
            nodes=[
                ColorGroupSwatch(attributes=dict(
                    Self="u12ColorGroupSwatch0",
                    SwatchItemRef="Swatch/None")),
                ColorGroupSwatch(attributes=dict(
                    Self="u12ColorGroupSwatch1",
                    SwatchItemRef="Color/Registration")),
                ColorGroupSwatch(attributes=dict(
                    Self="u12ColorGroupSwatch2",
                    SwatchItemRef="Color/Paper")),
                ColorGroupSwatch(attributes=dict(
                    Self="u12ColorGroupSwatch3",
                    SwatchItemRef="Color/Black")),
                ColorGroupSwatch(attributes=dict(
                    Self="u12ColorGroupSwatch4",
                    SwatchItemRef="Color/C=0 M=0 Y=100 K=0")),
                ColorGroupSwatch(attributes=dict(
                    Self="u12ColorGroupSwatch5",
                    SwatchItemRef="Color/C=0 M=100 Y=0 K=0")),
                ColorGroupSwatch(attributes=dict(
                    Self="u12ColorGroupSwatch6",
                    SwatchItemRef="Color/C=100 M=0 Y=0 K=0")),
                ColorGroupSwatch(attributes=dict(
                    Self="u12ColorGroupSwatch7",
                    SwatchItemRef="Color/C=100 M=90 Y=10 K=0")),
                ColorGroupSwatch(attributes=dict(
                    Self="u12ColorGroupSwatch8",
                    SwatchItemRef="Color/C=15 M=100 Y=100 K=0")),
                ColorGroupSwatch(attributes=dict(
                    Self="u12ColorGroupSwatch9",
                    SwatchItemRef="Color/C=75 M=5 Y=100 K=0"))
            ]
        ))
        self.nodes.append(ABullet(attributes=dict(
            Self="dABullet0",
            CharacterType="UnicodeOnly",
            CharacterValue=8226),
            nodes=[
                Properties(nodes=[
                    BulletsFont(attributes=dict(type="string", value='$ID')),
                    BulletsFontStyle(attributes=dict(type="string", value='$ID'))
                ])
            ]
        ))
        self.nodes.append(ABullet(attributes=dict(
            Self="dABullet1",
            CharacterType="UnicodeOnly",
            CharacterValue=42),
            nodes=[
                Properties(nodes=[
                    BulletsFont(attributes=dict(type="string", value='$ID')),
                    BulletsFontStyle(attributes=dict(type="string", value='$ID')),
                ])
            ]
        ))
        self.nodes.append(ABullet(attributes=dict(
            Self="dABullet2",
            CharacterType="UnicodeOnly",
            CharacterValue=9674),
            nodes=[
                Properties(nodes=[
                    BulletsFont(attributes=dict(type="string", value='$ID')),
                    BulletsFontStyle(attributes=dict(type="string", value='$ID')),
                ])
            ]
        ))
        self.nodes.append(ABullet(attributes=dict(
            Self="dABullet3",
            CharacterType="UnicodeWithFont",
            CharacterValue=187),
            nodes=[
                Properties(nodes=[
                    BulletsFont(attributes=dict(type="string", value='Myriad Pro')),
                    BulletsFontStyle(attributes=dict(type="string", value='$ID/Regular')),
                ])
            ]
        ))
        self.nodes.append(ABullet(attributes=dict(
            Self="dABullet4",
            CharacterType="GlyphWithFont",
            CharacterValue=503),
            nodes=[
                Properties(nodes=[
                    BulletsFont(attributes=dict(type="string", value='Minion Pro')),
                    BulletsFontStyle(attributes=dict(type="string", value='$ID/Regular')),
                ])
            ]
        ))
        self.nodes.append(Assignment(attributes=dict(
            Self="uc0",
            Name="$ID/UnassignedInCopy",
            UserName="$ID/",
            ExportOptions="AssignedSpreads",
            IncludeLinksWhenPackage=True,
            FilePath="$ID/"),
            nodes=[
                Properties(nodes=[
                    FrameColor(attributes=dict(type="enumeration", value='Nothing')),
                ])
            ]
        ))

if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
