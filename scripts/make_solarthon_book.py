from __future__ import absolute_import
from __future__ import unicode_literals

import os
import logging
from datetime import date
from pathlib import Path
from collections import OrderedDict
import pdfrw, pdfrw.errors, pdfrw.objects, pdfrw.objects.pdfname

from ngoschema.protocols import with_metaclass, SchemaMetaclass, ObjectProtocol

from reportlab.platypus import PageTemplate, BaseDocTemplate, SimpleDocTemplate, Frame
from reportlab.platypus import NextPageTemplate, Paragraph, PageBreak, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_JUSTIFY

from nonosolaris import settings
from nonosolaris.models.pdfrw_utils import get_form_fields, create_blank_page
from nonosolaris.models.pdfrw_utils import ANNOT_KEY, SUBTYPE_KEY, WIDGET_SUBTYPE_KEY, ANNOT_FIELD_KEY, ANNOT_PARENT_KEY
from nonosolaris.models.personas import Member, Administrator, Coordinator

ROOT_DIR = Path(__file__).parent

FORM_PAGE = Path(settings.FORM_PAGE)
FORM_PAGE = str(FORM_PAGE.resolve()) if FORM_PAGE.exists()\
    else str(ROOT_DIR.joinpath(settings.FORM_PAGE).resolve())


def _read_members(self, member_dir):
    members = []
    cyear = date.today().year
    for x in os.listdir(str(member_dir)):
        if x.endswith(".pdf"):
            self._logger.info('LOAD FILE %s.' % x)
            pdf_fp = member_dir.joinpath(x)
            pdfr = pdfrw.PdfReader(str(pdf_fp))
            member = get_form_fields(pdfr.pages[0])
            members.append(member)
    return members
