"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Jacob Bowman.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # Done: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    window = tkinter.Tk()

    # ------------------------------------------------------------------
    # DOne: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame1 = ttk.Frame(window, padding=10)
    frame1.grid()
    # ------------------------------------------------------------------
    # Done: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    button = ttk.Button(frame1, text="Click!")
    # ------------------------------------------------------------------
    # Done: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    button['command'] = (lambda:
                         print_hello())
    button.grid()
    # ------------------------------------------------------------------
    # Done: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    button2 = ttk.Button(frame1, text='Print:')
    button2['command'] = (lambda:
                          print_thing(entry1))
    button2.grid()

    entry1 = ttk.Entry(frame1)
    entry1.grid()
    # ------------------------------------------------------------------
    # Done: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    entry2 = ttk.Entry(frame1)
    entry2.grid()

    button3 = ttk.Button(frame1, text='times.')
    button3['command'] = (lambda:
                          multiple(entry2, entry1))
    button3.grid()
    # ------------------------------------------------------------------
    # TODO: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------
    button4 = ttk.Button(window, text='Change')
    button4['command'] = (lambda:
                          change())
    a = str("Blue")
    window.mainloop()


def print_hello():
    print('Hello')


def print_thing(entry):
    contents = entry.get()
    print(contents)


def multiple(entry_times, entry):
    n = int(entry_times.get())
    for k in range(n):
        print_thing(entry)


def change():
    a = 0
# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
