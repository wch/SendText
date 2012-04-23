# SendText for Sublime Text 2

This package sends text to a terminal (or other program). If text is selected, it will send the selection to the terminal when you press cmd-Enter; if no text is selected, it will send the current line to the terminal and move the cursor to the next line.

This presently works only on Mac OS X and Terminal.app. In the future I hope to add the following features:

* Work on Linux and Windows
* Allow easy customization of the target program
* Allow customizing the target program based on the file type

Hopefully it will also be possible to do the following:

* Attach a Sublime Text view to a particular terminal window.

This plugin was originally based on Rtools by Karthik Ram: https://github.com/karthikram/Rtools

# Installation

Clone this repo into your `Sublime Text 2/Packages` directory.

```
git clone git@github.com:wch/SendText.git
```

In the future, it will be possible to install via the Package Control plugin.


## Customization

1. It sends text to 

## Key bindings

To preserve or change these key bindings, copy them to your `Key Bindings - User` file.
