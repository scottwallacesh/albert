# -*- coding: utf-8 -*-

"""
The extension will generate a random string of the
specified length and copy it to the clipboard.
"""

import os
import base64

from albertv0 import *

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Password Generator"
__version__ = "1.0"
__trigger__ = "genpw "
__author__ = "Scott Wallace"
__dependencies__ = []


ICON_PATH = iconLookup('dialog-password')


def handleQuery(query):
    if query.isTriggered:
        return generatePassword(query)

def generatePassword(query):
    length = int(query.string.strip())

    return [Item(
        id=__prettyname__,
        icon=ICON_PATH,
        text='Generate a new %s-character password' % length,
        subtext='',
        completion="%s %s" % (__trigger__, query.string),
        actions=[
            ClipAction('Copy the new password to clipboard',
                       base64.encodestring(os.urandom(256))[:length])
        ]
    )]
