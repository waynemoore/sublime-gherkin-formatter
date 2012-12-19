# Sublime Gherkin Formatter

## Installing

I am waiting for my pull request to be merged in so that you can install via the Sublime Package Control system.  In the mean time you can install it by cloning it to your Sublime plugins directory:

```
$ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
$ git clone git://github.com/waynemoore/sublime-gherkin-formatter.git
```

You can use `<Ctrl> + <Alt> + G` to reformat your current buffer.

## Contributing

It's a python project, so I recommend you make use of [virtualenv](http://www.virtualenv.org/) to manage dependencies.

1. Clone repository
2. `$ pip install -r requirements.pip`
3. `$ nosetests`
4. Write a test
5. Implement your feature / bugfix
6. Open a pull request

## Known Issues

### Removes leading whitespace

The plugin currently strips the leading white space from each line, so if you like to indent some of your text, you will probably get annoyed - I plan to fix this soon.

For example:

```
As a developer
  I want my leading whitespace stripped
    Because this indentation is weird

Examples:
  |stuff|
```

Will reformat to:

```
As a developer
I want my leading whitespace stripped
Because this indentation is weird

Examples:
|stuff|
```
