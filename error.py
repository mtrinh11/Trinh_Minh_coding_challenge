import traceback
from tkinter import messagebox

def program_error(self, *args):
    """
    Prints what the tkinter error is on a popup and exits the program
    """
    message = 'Program error: \n'
    message += traceback.format_exc()
    message += "\n\n\nClosing Program Due to Error "
    messagebox.showerror('Program Error', message)
    exit()