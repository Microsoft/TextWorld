#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by TatSu.
#
#    https://pypi.python.org/pypi/tatsu/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.

from __future__ import print_function, division, absolute_import, unicode_literals

from tatsu.objectmodel import Node
from tatsu.semantics import ModelBuilderSemantics


class TextGrammarModelBuilderSemantics(ModelBuilderSemantics):
    def __init__(self):
        types = [
            t for t in globals().values()
            if type(t) is type and issubclass(t, ModelBase)
        ]
        super(TextGrammarModelBuilderSemantics, self).__init__(types=types)


class ModelBase(Node):
    pass


class AdjectiveNoun(ModelBase):
    adjective = None
    noun = None


class Match(ModelBase):
    lhs = None
    rhs = None


class ProductionRule(ModelBase):
    alternatives = None
    symbol = None


class TextGrammar(ModelBase):
    rules = None
