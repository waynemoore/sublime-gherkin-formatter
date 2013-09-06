from __future__ import unicode_literals

import sure
import unittest

from formatter import ViewFormatter
from .mocks import *


class FormatterTestCase(unittest.TestCase):

  def setUp(self):
    self.sublime = MockSublimePackage

  def test_view_is_formatted(self):
    view = MockView("Feature: test\n  |item1|\n|item2|")
    view.sel().add(MockRegion(0, 0))

    formatter = ViewFormatter(self.sublime, view)
    formatter.format_view(None)

    view.buffer.should.equal("Feature: test\n  | item1 |\n  | item2 |\n")

  def test_caret_position_is_preserved(self):
    view = MockView("Feature: test\n  |item1|\n|item2|")
    view.sel().add(MockRegion(5, 5))

    formatter = ViewFormatter(self.sublime, view)
    formatter.format_view(None)

    view.sel()[0].begin().should.equal(5)
