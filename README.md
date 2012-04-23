# SendText for Sublime Text 2

This package sends text to a terminal (or other program). If text is selected, it will send the selection to the terminal when you press cmd-Enter; if no text is selected, it will send the current line to the terminal and move the cursor to the next line.

This presently works with:

* Terminal.app on Mac OS X
* iTerm on Mac OS X
* tmux on any platform (Linux and Mac OS X)


Presently it just uses the topmost window/terminal for all of these options. Hopefully in the future it will also be possible to do the following:

* Attach a Sublime Text view to a particular terminal window.

This plugin was originally based on Rtools by Karthik Ram: https://github.com/karthikram/Rtools

# Installation

Clone this repo into your `Sublime Text 2/Packages` directory.

```
git clone git@github.com:wch/SendText.git
```

In the future, it will be possible to install via the Package Control plugin.


## Customization

* In the `SendText.sublime-settings` file, uncomment the appropriate line for Terminal.app, iTerm, or tmux.
* If you use tmux, you may need to set the path to make it work. In the settings file, uncomment the line for tmux and set the correct path. (This seems to be necessary for me on Mac OS X and tmux installed in /usr/local/bin, but probably won't be necessary if tmux is in /usr/bin.)


## Key bindings

To preserve or change these key bindings, copy them to your `Key Bindings - User` file.
