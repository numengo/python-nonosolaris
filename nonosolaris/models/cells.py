# -*- coding: utf-8 -*-

"""Main module Solaris """
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

from .. import settings
from .pdfrw_utils import get_form_fields, create_blank_page
from .pdfrw_utils import ANNOT_KEY, SUBTYPE_KEY, WIDGET_SUBTYPE_KEY, ANNOT_FIELD_KEY, ANNOT_PARENT_KEY
from .personas import Member, Administrator, Coordinator

ROOT_DIR = Path(__file__).parent.parent

FORM_PAGE = Path(settings.FORM_PAGE)
FORM_PAGE = str(FORM_PAGE.resolve()) if FORM_PAGE.exists()\
    else str(ROOT_DIR.joinpath(settings.FORM_PAGE).resolve())


class Cell(with_metaclass(SchemaMetaclass)):
    """Cellule SOLARIS

    Permet le parametrage de la cellule (identifiant, email),
    le parametrage du repertoire de travail contenant les fiches des membres,
    le chargement des fiches des membres en memoire.

    :param cell_id: identifiant de cellule.
    :param email: protonmail de la cellule.
    :param cell_dir: repertoire de travail de la cellule.
    """
    _id = r"https://solaris-france.org/nono#/$defs/cells/$defs/Cell"
    _useContext = True

    def __init__(self, _value=None, **opts):
        """Initialise la cellule."""
        ObjectProtocol.__init__(self, value=_value, **opts)

    def view(self):
        """Affiche les infos de la cellule."""
        ret = ['{']
        for k, v in self.do_serialize().items():
            ret.append(f'\t{k}: {v}')
        ret.append('}')
        return '\n'.join(ret)

    def _read_members(self, member_dir):
        members = []
        cyear = date.today().year
        for x in os.listdir(str(member_dir)):
            if x.endswith(".pdf"):
                self._logger.info('LOAD FILE %s.' % x)
                pdf_fp = member_dir.joinpath(x)
                pdfr = pdfrw.PdfReader(str(pdf_fp))
                member = get_form_fields(pdfr.pages[0])
                if not member.get('GenderField'):
                    # establish gender
                    gender = 'M' if member['MaleCheck'] else ''
                    gender += 'F' if member['FemaleCheck'] else ''
                    # read fields, set gender, compute age and set title
                    member['GenderField'] = gender
                elif 'M' in member['GenderField']:
                    member['MaleCheck'] = True
                elif 'F' in member['GenderField']:
                    member['FemaleCheck'] = True
                firstn = member['FirstNameField']
                lastn = member.get('NameField') or member.get('LastNameField')
                member['LastNameField'] = lastn
                lastn_upper = lastn.upper()
                city = member['CityField']
                city_upper = member['CityUpper'] = city.upper()
                age_suffix = ''
                if member.get('BirthYearField'):
                    byear = int(member['BirthYearField'].replace('.', '/').split('/')[-1])
                    if byear < 100:
                        byear += 1900
                    member['BirthYearField'] = str(byear)
                    age = cyear - byear
                    age_suffix = f'{age}ans'
                member['TitleField'] = f'{firstn} {lastn_upper}, {city_upper}, {gender} {age_suffix}'
                member['IndexEntryField'] = f'{lastn_upper} {firstn}, {city_upper}, {gender} {age_suffix}'
                member['IndexCityEntryField'] = f'{lastn_upper} {firstn}, {gender} {age_suffix}'
                member['PageFilename'] = f'{city_upper} - {lastn_upper} {firstn}.pdf'
                member['FormOrigFilepath'] = pdf_fp
                member['EmailLink'] = f'mailto:{member["EmailField"]}'
                member['TelegramIdLink'] = f'https://t.me/{member["TelegramIdField"]}'
                members.append(member)
        return members

    def _sort_members(self):
        self.members = members = sorted(self.members, key=lambda x: x['IndexEntryField'])
        cities = sorted(list(set([m['CityField'] for m in members])))
        self.members_city = OrderedDict([(c, list()) for c in cities])
        for i, m in enumerate(self.members):
            self.members_city[m['CityField']].append(m)
            m['PageField'] = ip = str(i + 1)

    def load_members(self, member_dir=None):
        """Charge les fiches des membres de la cellule en mémoire.

        :param member_dir: repertoire contenant les fiches des membres
        :return: self
        """
        member_dir = member_dir or self.member_dir
        self.members += self._read_members(member_dir)
        self._sort_members()
        return self

    def write_form(self):
        """Crée une copie locale du formulaire"""
        import shutil
        form_fp1 = FORM_PAGE
        form_fp2 = self.cell_dir.joinpath(form_fp1.name).resolve()
        shutil.copy(str(form_fp1), str(form_fp2))
        self._logger.info('CREATE FILE %s.' % form_fp2)
        return form_fp2
