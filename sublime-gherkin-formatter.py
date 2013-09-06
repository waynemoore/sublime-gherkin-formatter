import sublime, sublime_plugin

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib.formatter import ViewFormatter


class FormatGherkinCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    ViewFormatter(sublime, self.view).format_view(edit)
