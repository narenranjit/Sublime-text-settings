# Sublime TODOs

A Sublime Text 2 plugin to extract and list TODO comments from open files and 
project folders.


# Install & Config

    $ cd Sublime Text 2/Packages
    $ git clone https://robcowie@github.com/robcowie/SublimeTODO.git

Or use the Sublime Package manager

## Adding comment patterns

Extraction uses regular expressions that return one match group 
representing the message. Default patterns are provided for `TODO`, `NOTE`, `FIXME` 
and `CHANGED` comments.
To override or provide more patterns, add `patterns` to user settings, e.g.

    "patterns": {
        'TODO': r'TODO[\s]*?:+(?P<todo>.*)$',
        'NOTE': r'NOTE[\s]*?:+(?P<note>.*)$',
        'FIXME': r'FIX ?ME[\s]*?:+(?P<fixme>\S.*)$',
        'CHANGED': r'CHANGED[\s]*?:+(?P<changed>\S.*)$'
    }

Note that the pattern _must_ provide at least one named group which will be used to group the comments in results.

## Results title

Override the results view title by setting `result_title`

    "result_title": "TODO Results

# Usage

`Show TODOs` command can be triggered from the command palette. No default 
key bindings are provided.

# License

All of SublimeTODO is licensed under the MIT license.

Copyright (c) 2012 Rob Cowie <szaz@mac.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.