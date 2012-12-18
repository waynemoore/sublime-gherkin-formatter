import sublime, sublime_plugin

from gherkin import GherkinParser, GherkinFormatter

class FormatGherkinCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    entire_buffer = sublime.Region(0, self.view.size())

    parser = GherkinParser(self.view.substr(entire_buffer))
    parsed = parser.parse()
    result = GherkinFormatter().format(parsed)

    self.view.replace(edit, entire_buffer, result)
