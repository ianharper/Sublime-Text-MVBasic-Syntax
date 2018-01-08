Sublime Text syntax highlighting, indentation, and sinppets for MultiValue Basic. 

## Features
* MultiValue Syntaxes Supported:
  * D3
  * OpenQM
* "\\" Quotes
* Auto-Indentation while typing
* "wED" Color Scheme (at least this is how I've setup colors in wED)
* Integration with Sublime's Goto Definition for MV Basic line labels 
* Snippets: 
  * if-then if-else if-then-else
  * for dcount-for
  * loop-repeat
  * execute-loop-readnext-read-repeat
  * begin case-case-end case
  * open
  * read-readnext


## Installation
Installation is easy with Sublime's command palate:
~~~~
Package Control: Install Package
MultiValue BASIC
~~~~

## Contributing 
Pull requests are welcome. For major changes please open an issue to discuss what you would like to change.

## TODO
* Add additional MV dialects
* Enable goto definition for subroutine calls
* Add uppercase tab completions for snippets
* Rework syntax definition to suppport meta_scopes for MV blocks (for, if, loop, clauses, etc).
