import sure
import unittest

from gherkin import GherkinParser, GherkinFormatter, Tokens


class GherkinParserTestCase(unittest.TestCase):

  def test_it_should_parse_non_example_tables_as_text(self):
    feature = "\
    Feature: As a tester\n\
    I want my non example table text to remain intact\n\
    So that I don't want kill the author of this plugin"

    tokens = GherkinParser(feature).parse()
    tokens.should.have.length_of(3)
    tokens[0].should.equal((Tokens.TEXT, 'Feature: As a tester'))
    tokens[1].should.equal((Tokens.TEXT, 'I want my non example table text to remain intact'))
    tokens[2].should.equal((Tokens.TEXT, 'So that I don\'t want kill the author of this plugin'))

  def test_it_should_parse_example_groups(self):
    example_text = "\
    |cat breeds|country|\n\
    |Bengal|United States|\n\
    |Burmese|Burma|"

    tokens = GherkinParser(example_text).parse()
    tokens.should.have.length_of(1)

    group = tokens[0]
    group[0].should.equal(Tokens.GROUP)

    examples = group[1]
    examples.should.have.length_of(3)
    examples[0].should.equal(['cat breeds', 'country'])
    examples[1].should.equal(['Bengal', 'United States'])
    examples[2].should.equal(['Burmese', 'Burma'])

  def test_it_should_parse_text_and_groups(self):
    feature = "\
    Feature: As a crazy cat person\n\
    I want to write a list of cat breeds\n\
    So that my codez is odd\n\
    \n\
    |cat breeds|country|\n\
    |Manx|Isle of Man|\n\
    |Octocat|The Web|\n"

    tokens = GherkinParser(feature).parse()
    tokens.should.have.length_of(5)

    tokens[0].should.equal((Tokens.TEXT, 'Feature: As a crazy cat person'))
    tokens[1].should.equal((Tokens.TEXT, 'I want to write a list of cat breeds'))
    tokens[2].should.equal((Tokens.TEXT, 'So that my codez is odd'))
    tokens[3].should.equal((Tokens.TEXT, ''))

    group = tokens[4]
    group[0].should.equal(Tokens.GROUP)

    examples = group[1]
    examples.should.have.length_of(3)
    examples[0].should.equal(['cat breeds', 'country'])
    examples[1].should.equal(['Manx', 'Isle of Man'])
    examples[2].should.equal(['Octocat', 'The Web'])

  def test_it_should_parse_multiple_text_and_group_sections(self):
    feature = "\
    foo\n\
    |exampleA|\n\
    bar\n\
    |example1|example2|\n"

    tokens = GherkinParser(feature).parse()
    tokens.should.have.length_of(4)

    tokens[0].should.equal((Tokens.TEXT, 'foo'))

    group = tokens[1]
    group[0].should.equal(Tokens.GROUP)
    group[1].should.equal([['exampleA']])

    tokens[2].should.equal((Tokens.TEXT, 'bar'))

    group = tokens[3]
    group[0].should.equal(Tokens.GROUP)
    group[1].should.equal([['example1', 'example2']])


class GherkinFormatterTestCase(unittest.TestCase):

  def test_it_should_strip_leading_whitespace_of_text(self):
    feature = "\
    Feature: As a tester\n\
    I want my non example table text to remain intact\n\
    So that I don't want kill the author of this plugin\n"

    parsed = GherkinParser(feature).parse()
    text = GherkinFormatter().format(parsed)

    text.should.equal(_strip_leading_whitespace(feature))

  def test_it_should_format_example_group_columns_to_widest_value(self):
    examples = "\
    |cat breeds|country|\n\
    |Manx|Isle of Man|\n\
    |Octocat|The Web|\n"

    parsed = GherkinParser(examples).parse()
    text = GherkinFormatter().format(parsed)

    lines = text.split('\n')
    lines.should.have.length_of(4)
    lines[0].should.equal('| cat breeds | country     |')
    lines[1].should.equal('| Manx       | Isle of Man |')
    lines[2].should.equal('| Octocat    | The Web     |')
    lines[3].should.equal('')

  def test_it_should_format_combinations_of_text_and_example_groups(self):
    feature = "\
    Feature: As a tester\n\
    I want my non example table text to remain intact\n\
    So that I don't want kill the author of this plugin\n\
    \n\
    |cat breeds|country|\n\
    |Manx|Isle of Man|\n\
    |Octocat|The Web|\n"

    parsed = GherkinParser(feature).parse()
    text = GherkinFormatter().format(parsed)

    lines = text.split('\n')
    lines.should.have.length_of(8)
    lines[0].should.equal('Feature: As a tester')
    lines[1].should.equal('I want my non example table text to remain intact')
    lines[2].should.equal('So that I don\'t want kill the author of this plugin')
    lines[3].should.equal('')
    lines[4].should.equal('| cat breeds | country     |')
    lines[5].should.equal('| Manx       | Isle of Man |')
    lines[6].should.equal('| Octocat    | The Web     |')
    lines[7].should.equal('')


def _strip_leading_whitespace(text):
  lines = map(lambda l: l.lstrip(), text.split("\n"))
  return '\n'.join(lines)

