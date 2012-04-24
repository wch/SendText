# SendText for Sublime Text 2

This package sends text to a terminal (or other program). If text is selected, it will send the selection to the terminal when you press cmd-Enter (Mac) or ctrl-Enter (Linux/Windows); if no text is selected, it will send the current line to the terminal and move the cursor to the next line.
This is very useful for coding in interpreted languages.

SendText presently works with:

* Terminal.app on Mac OS X. SendText will send the text to the most recently active Terminal window.
* iTerm on Mac OS X. SendText will send the text to the most recently iTerm window.
* tmux on any platform (Linux and Mac OS X). tmux is a terminal multiplexer (like GNU screen) which you can start in any terminal emulator. SendText will send the text to the most recently active tmux session.

Hopefully in the future it will also be possible to do the following:

* Attach a Sublime Text view to a particular terminal window.

This plugin was originally based on Rtools by Karthik Ram: https://github.com/karthikram/Rtools

## Installation

Clone this repo into your `Sublime Text 2/Packages` directory. This will be in different places depending on the OS:

* Windows: `%APPDATA%\Sublime Text 2\Packages`
* OS X: `~/Library/Application Support/Sublime Text 2/Packages`
* Linux: `~/.config/sublime-text-2`

```
git clone git@github.com:wch/SendText.git
```

In the future, it will be possible to install via the Package Control plugin.

## Configuration

You can configure SendText by editing the file `SendText/SendText.sublime-settings`. 

First, choose which terminal program you want to use, and uncomment the appropriate line. For example, this tells SendText to use Terminal.app:

```
    "program": "Terminal.app",
    // "program": "tmux",
    // "program": "iTerm",
```

If you're using Terminal.app or iTerm, that's all you need to do.
If you use tmux, you may need to explicitly set the path to make it work.
(This seems to be necessary for me on Mac OS X and with tmux installed in `/usr/local/bin`, but YMMV.)
In the `paths`, set the value for tmux to the full path to the executable. For example:

```
    "paths":
    {
        "tmux": "/usr/local/bin/tmux"
    }
```

## Using SendText

Using SendText is simple. Start your terminal program (of the ones listed above), then, in Sublime Text, select some text and press cmd-Enter (or ctrl-Enter).


## Key bindings

To preserve or change the key bindings, copy them to your `Key Bindings - User` file.
