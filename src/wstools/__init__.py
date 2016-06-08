#! /usr/bin/env python
"""WSDL parsing services package for Web Services for Python."""

ident = "$Id$"

try:
    from . import WSDLTools
    from . import XMLname
    import logging
except:
    import WSDLTools
    import XMLname
    import logging

