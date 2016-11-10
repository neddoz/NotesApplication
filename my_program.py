#!/usr/bin/env python
"""
This Application uses docopt with the built in cmd module to employ an
interactive command application.
Usage:
    notes tcp <host> <port> [--timeout=<seconds>]
    notes serial <port> [--baud=<n>] [--timeout=<seconds>]
    notes (-i | --interactive)
    notes (-h | --help | --version)
    notes create <title>
    notes list
    notes view <note_id>
    notes delete <note_id>
    notes sync
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from functions import Notes


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to the Notes Taking Application!' \
        + ' (type help for a list of commands.)'
    prompt = '(note) '
    file = None
    note = Notes()

    @docopt_cmd
    def do_list(self, arg):
        """Usage: list"""
        self.note.retrieve_notes()

    @docopt_cmd
    def do_create(self, arg):
        """Usage: create <title>
        """
        self.note.save_note(arg["<title>"])

    @docopt_cmd
    def do_view(self, arg):
        """Usage: view <note_id>
        """
        self.note.view_note(arg["<note_id>"])

    @docopt_cmd
    def do_delete(self, arg):
        """Usage: delete <note_id>
        """
        self.note.delete_note(arg["<note_id>"])

    @docopt_cmd
    def do_search(self, arg):
        """Usage: search <title>
        """
        self.note.search_note(arg["<title>"])

    @docopt_cmd
    def do_sync(self, arg):
        """Usage: sync
        """
        self.note.sync()

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Thank you! Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)