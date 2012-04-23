import sublime
import sublime_plugin
import subprocess
import string

settings = sublime.load_settings('SendText.sublime-settings')

class SendSelectionCommand(sublime_plugin.TextCommand):
    @staticmethod
    def escapeString(str):
        str = string.replace(str, '\\', '\\\\')
        str = string.replace(str, '"', '\\"')
        return str

    @staticmethod
    def send(selection, prog):

        if prog == "Terminal.app":
            # Remove trailing newline
            selection = selection.rstrip('\n')
            # Split selection into lines
            selection = SendSelectionCommand.escapeString(selection).split("\n")

            args = ['osascript']
            # add code lines to list of arguments
            for part in selection:
                args.extend(['-e', 'tell app "Terminal" to do script "' + part +
                    '" in window 1',])
            # execute code
            subprocess.call(args)

        elif prog == "tmux":
            subprocess.call(['/usr/local/bin/tmux', 'set-buffer', selection])
            subprocess.call(['/usr/local/bin/tmux', 'paste-buffer', '-d'])


    def run(self, edit):
        # get selection
        selection = ""
        for region in self.view.sel():
            if region.empty():
                selection += self.view.substr(self.view.line(region)) + "\n"
                self.advanceCursor(region)
            else:
                selection += self.view.substr(region) + "\n"

        # only proceed if selection is not empty
        if(selection == "" or selection == "\n"):
            return

        self.send(selection, settings.get('program'))


    def advanceCursor(self, region):
        (row, col) = self.view.rowcol(region.begin())

        # Make sure not to go past end of next line
        nextline = self.view.line(self.view.text_point(row + 1, 0))
        if nextline.size() < col:
            loc = self.view.text_point(row + 1, nextline.size())
        else:
            loc = self.view.text_point(row + 1, col)

        # Remove the old region and add the new one
        self.view.sel().subtract(region)
        self.view.sel().add(sublime.Region(loc, loc))
