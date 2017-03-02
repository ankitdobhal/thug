#!/usr/bin/env python

from .HTMLElement import HTMLElement
from .attr_property import attr_property

import logging
log = logging.getLogger("Thug")


class HTMLMetaElement(HTMLElement):
    def __init__(self, doc, tag):
        HTMLElement.__init__(self, doc, tag)

    content         = attr_property("content")
    httpEquiv       = attr_property("http-equiv")
    name            = attr_property("name", default = "")
    scheme          = attr_property("scheme")
    _charset        = attr_property("charset", default = "")

    def __getattr__(self, name):
        if name in ('charset', ) and log.ThugOpts.Personality.isIE():
            return self._charset

        raise AttributeError
