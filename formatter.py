from gherkin import GherkinParser, GherkinFormatter


class ViewFormatter(object):

  def __init__(self, sublime, view):
    self._sublime = sublime
    self._view = view

  def format_view(self, edit):
    entire_buffer = self._sublime.Region(0, self._view.size())

    parser = GherkinParser(self._view.substr(entire_buffer))
    parsed = parser.parse()
    result = GherkinFormatter().format(parsed)

    self._view.replace(edit, entire_buffer, result)
