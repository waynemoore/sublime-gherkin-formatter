# Sublime Gherkin Formatter

## Features

At this stage all it really does is format example group tables.

### Spacing

Tables that look like this:

```
|cat breeds|country|
|Manx|Isle of Man|
|Octocat|The Web|
```

Will be reformatted to:

```
| cat breeds | country     |
| Manx       | Isle of Man |
| Octocat    | The Web     |
```

### Indentation

Usually, people like to indent their tables from the rest of the text.  This plugin respects the first line of the group's indent.  So the following:

```
Then the "<cat breed>" is from "<country>"
    | cat breeds | country     |
| Manx       | Isle of Man |
            | Octocat    | The Web     |
```

Will be indented to:

```
Then the "<cat breed>" is from "<country>"
    | cat breeds | country     |
    | Manx       | Isle of Man |
    | Octocat    | The Web     |
```

## Installing

### Package control

You can now install this plugin using [Sublime Package Control](http://wbond.net/sublime_packages/package_control).

1. Open Command Palette (`<Cmd> + <Shift> + P` on a Mac, or access via Tools menu)
2. Find and select "Package Control: Install Package"
3. Find and install "Gherkin (Cucumber) Formatter"

### Manual

You can install this plugin manually by cloning it to your Sublime plugins directory:

```
$ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
$ git clone git://github.com/waynemoore/sublime-gherkin-formatter.git
```

## Usage

There are a few ways to use it:

- `<Cmd> + <Shift> + |` - This matches the TextMate cucumber plugin's key binding.
- `<Ctrl> + <Alt> + G` - DEPRECATED. Original key binding still set to avoid surprise when upgrading the plugin.
- Select "Gherkin/Cucumber: Format" from the Command Palette.

## Contributing

It's a python project, so I recommend you make use of [virtualenv](http://www.virtualenv.org/) to manage dependencies.

1. Clone repository
2. `$ pip install -r requirements.pip`
3. `$ nosetests`
4. Write a test
5. Implement your feature / bugfix
6. Open a pull request

## Contributors
- Paul Tyng (@paultyng)
