# -*- coding: utf-8 -*-

"""Personas module Solaris """
from __future__ import absolute_import
from __future__ import unicode_literals

import os
import logging
from datetime import date
from pathlib import Path
from collections import OrderedDict
import pdfrw, pdfrw.errors, pdfrw.objects, pdfrw.objects.pdfname

from ngoschema.protocols import with_metaclass, SchemaMetaclass
#from vishuda.models import User


class Member(with_metaclass(SchemaMetaclass)):
    _id = r"https://solaris-france.org/nono#/$defs/personas/$defs/Member"


class Coordinator(with_metaclass(SchemaMetaclass)):
    _id = r"https://solaris-france.org/nono#/$defs/personas/$defs/Coordinator"


class Administrator(with_metaclass(SchemaMetaclass)):
    _id = r"https://solaris-france.org/nono#/$defs/personas/$defs/Administrator"

