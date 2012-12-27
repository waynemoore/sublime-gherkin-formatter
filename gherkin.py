import re

from StringIO import StringIO


class Tokens(object):
  TEXT = 1
  GROUP = 2


class GherkinParser(object):

  def __init__(self, gherkin_text):
    self._gherkin_text = StringIO(gherkin_text)
    self._tokens = []
    self._group = []

  def parse(self):
    example_re = re.compile(r'\s*\|[^|]+\|\s*')

    for line in self._gherkin_text.readlines():
      line = line.strip()

      if example_re.match(line):
        self._collect_group_item(line)
      else:
        self._store_and_reset_group()
        self._add_text_token(line)

    self._finish()

    return self._tokens

  def _collect_group_item(self, line):
    elements = [item.strip() for item in line.split('|')[1:-1]]
    self._group.append(elements)

  def _new_group(self):
    self._group = []

  def _store_and_reset_group(self):
    if len(self._group) > 0:
      self._tokens.append((Tokens.GROUP, self._group))
      self._new_group()

  def _add_text_token(self, text):
    self._tokens.append((Tokens.TEXT, text))

  def _finish(self):
    self._store_and_reset_group()


class GherkinFormatter(object):

  def __init__(self):
    self._result = StringIO()

  def format(self, parsed):
    for token_type, token in parsed:

      if token_type == Tokens.TEXT:
        self._emit(token)
      elif token_type == Tokens.GROUP:
        self._format_group(token)
      else:
        raise Exception('unsupported token type %s' % token_type)

    result = self._result.getvalue()
    self._result.close()

    return result

  def _format_group(self, group):
    widths = self._determine_column_widths(group)

    for line in group:
      buf = StringIO()
      buf.write('|')

      for idx, col in enumerate(line):
        width = widths[idx]
        padding = width - len(col)
        buf.write(' ')
        buf.write(col)
        buf.write(' ' * padding)
        buf.write(' |')

      self._emit(buf.getvalue())
      buf.close()

  def _determine_column_widths(self, group):
    widths = []

    for i in range(len(group[0])):
      width = 0
      for j in range(len(group)):
        width = max(len(group[j][i]), width)
      widths.append(width)

    return widths

  def _emit(self, text):
    self._result.write(text)
    self._result.write('\n')
