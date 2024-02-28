import tkinter as tk
from error import program_error

from stoplightwindow import StoplightWindow

def main():
    """
    Start the program. 
    """
    root = tk.Tk()
    root.title("Traffic Light")
    root.geometry("400x1000")
    root.report_callback_exception = program_error

    app = StoplightWindow(root, 400, 700)
    app.create_stoplight_radiobutton()
    app.create_stoplight_input()
    app.create_quit_button()
    app.create_stoplight()
    app.mainloop()

main()