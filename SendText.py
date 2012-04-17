import sublime
import sublime_plugin
import subprocess
import string

class SendSelectionCommand(sublime_plugin.TextCommand):
    @staticmethod
    def cleanString(str):
        str = string.replace(str, '\\', '\\\\')
        str = string.replace(str, '"', '\\"')
        return str

    def run(self, edit):
        # get selection
        selection = ""
        for region in self.view.sel():
            if region.empty():
                selection += self.view.substr(self.view.line(region)) + "\n"
                self.advanceCursor(region)
            else:
                selection += self.view.substr(region) + "\n"

        selection = (selection[::-1].replace('\n'[::-1], '', 1))[::-1]

        # only proceed if selection is not empty
        if(selection == ""):
            return

        # split selection into lines
        selection = self.cleanString(selection).split("\n")
        # define osascript arguments
        args = ['osascript']
        # add code lines to list of arguments
        for part in selection:
            args.extend(['-e', 'tell app "Terminal" to do script "' + part +
                '" in window 1',])
        # execute code
        subprocess.Popen(args)


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
