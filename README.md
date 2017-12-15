# Sublime-Text-MVBasic-Syntax

Syntax highlighting/indentation/sinppets for OpenQM and D3 Basic. This will (currently) work well with most versions of Basic for MV databases, not just D3 and QM. I've also included some preferences that help with MV syntax (especially allowing "." as part of a variable name). Even with that I've noticed that Sublime doesn't 100% support this setting with goto definition. The syntax definitions are case insensitive, however, the snippet tab completions are not (I've defined them in lowercase). 

If you have better soultions please contribute to this! This is my first crack at customizing Sublime.

## Features
* D3 Syntax
* OpenQM Syntax
* Auto-Indentation rules (used while typing)
* "wED" Color Scheme (at least this is how I've setup colors in wED)
* Snippets:
  * if-then if-else if-then-else
  * for dcount-for
  * loop-repeat
  * execute-loop-readnext-read-repeat
  * begin case-case-end case
  * open
  * read-readnext

## TODO
* Convert the QM syntax to the sublime-syntax format used the sublime v3.092+
* Add additional MV dialects
