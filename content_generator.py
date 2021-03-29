import generator
import sys
import widgets


def display_in_GUI():
    """Displays paragraph from Wikipedia in GUI."""
    widgets.window.mainloop()


def display_in_output():
    """Displays paragraph from Wikipedia in output file."""
    generator.generate_output()


if __name__ == '__main__':
    # if program is being run in via GUI...
    if 'input.csv' not in sys.argv:
        display_in_GUI()
    # if program is being run via command line/terminal...
    else:
        display_in_output()
