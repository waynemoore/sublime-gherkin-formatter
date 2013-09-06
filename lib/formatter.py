from __future__ import unicode_literals

from lib.gherkin import GherkinParser, GherkinFormatter


class ViewFormatter(object):

  def __init__(self, sublime, view):
    self._sublime = sublime
    self._view = view

  def format_view(self, edit):
    self._store_caret_position()
    self._format_and_replace(edit)
    self._reset_caret_position()

  def _format_and_replace(self, edit):
    entire_buffer = self._sublime.Region(0, self._view.size())

    parser = GherkinParser(self._view.substr(entire_buffer))
    parsed = parser.parse()
    result = GherkinFormatter().format(parsed)

    self._view.replace(edit, entire_buffer, result)

  def _store_caret_position(self):
    self._pos = self._view.sel()[0].begin()

  def _reset_caret_position(self):
    self._view.sel().clear()
    self._view.sel().add(self._sublime.Region(self._pos, self._pos))
