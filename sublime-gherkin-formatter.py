import sublime, sublime_plugin

from formatter import ViewFormatter


class FormatGherkinCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    ViewFormatter(sublime, self.view).format_view(edit)
