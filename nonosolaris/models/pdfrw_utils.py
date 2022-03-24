# -*- coding: utf-8 -*-

"""Main module Solaris """
from __future__ import absolute_import
from __future__ import unicode_literals

import pdfrw, pdfrw.errors, pdfrw.objects, pdfrw.objects.pdfname


# PDF ANNOTATIONS
ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_PARENT_KEY = '/Parent'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


def create_blank_page(width=None, height=None):
    blank = pdfrw.PageMerge()
    blank.mbox = [0, 0, width or 595, height or 773]
    return blank.render()


def get_form_fields(page):
    fields = {}
    annotations = page[ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if not annotation[ANNOT_FIELD_KEY]:
                annotation = annotation[ANNOT_PARENT_KEY]
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                v = annotation[ANNOT_VAL_KEY]
                if isinstance(v, pdfrw.objects.PdfString):
                    fields[key] = v.to_unicode()
                if isinstance(v, pdfrw.objects.pdfname.BasePdfName):
                    if v == '/Yes':
                        fields[key] = True
                    if v == '/Off':
                        fields[key] = False
    return fields
