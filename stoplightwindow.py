import tkinter as tk
from tkinter import messagebox

from light import Light
from stoplight import Stoplight

class StoplightWindow(tk.Frame):
    """
    A class used to represent a tkinter Window used for displaying
    a stoplight.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    create_stoplight_input()
        Prints the input information and the textbox to be used by the user
        to control the stoplight timers
    create_stoplight_radiobutton()
        Prints the radiobuttons used to select which light the user wants
        to change the timer for. 
    create_quit_button()
        Displays a quit button on the frame for the user to exit the program.
    create_stoplight()
        Creates and starts the Stoplight.
    """
    def __init__(self, parent_frame, width, height):
        """
        Parameters
        ----------
        parent_frame : tkinter.Frame
            The parent frame that the light will be drawn within.
        width : int
            The width of the window.
        height : int
            The height of the window.
        """
        super().__init__(parent_frame)
        self.pack()
        self.parent_frame = parent_frame
        self.width = width
        self.height = height
        self.stoplight_frame = tk.Frame(parent_frame, width=width, height=height)
        self.canvas = tk.Canvas(self.stoplight_frame, width=width, height=height, background="white")
        
        self.light_state = [
            [1200, "red", 150, 150, 250, 250],
            [400, "yellow", 150, 300, 250, 400],
            [400, "green", 150, 450, 250, 550]
        ]

        self.lights = self.__create_lights(self.light_state)
        
    def create_stoplight_input(self):
        """
        Prints the relevant input information and the textbox to be used by the user
        to control the stoplight timers

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        tk.Label(self.parent_frame, text="How long should the lights blink in milliseconds? \n Press enter to submit.").pack()
        self.time_input = tk.Entry(self.parent_frame)
        self.time_input["textvariable"] = tk.StringVar(self.parent_frame, value="")
        self.time_input.bind('<Key-Return>', self.__update_stoplight)
        self.time_input.pack()
            
    def create_stoplight_radiobutton(self):
        """
        Prints the options to select which light to change the timer for.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.selected = tk.StringVar(value=0)
        light_radiobutton = []
        for i in range(len(self.lights)):
            light_radiobutton.append(
                tk.Radiobutton(
                    self.parent_frame,
                    text=f"{self.lights[i].color}", 
                    variable=self.selected, 
                    value=f"{i}").pack(),
            )
            
    def __create_lights(self, light_data):
        """
        Creates the light of Lights from light_data that will be used in creation
        of the stoplight.

        Parameters
        ----------
        light_data : list
            A list of lists that contain information for instantiating Light
            instances.

        Returns
        -------
        None
        """
        lights_arr = []
        for light in light_data:
            lights_arr.append(Light(self.stoplight_frame, self.canvas, light[0], light[1], light[2], light[3], light[4], light[5]))
        return lights_arr
    
    def create_quit_button(self):
        """
        Displays a quit button on the window that the user can use to quit the program.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.quit_button = tk.Button(self.parent_frame, text="Quit", command=self.__close_program_normal)
        self.quit_button.pack()

    def __close_program_normal(self):
        """
        Prints to the screen "Exiting Traffic Light Simulator" and exits the
        program after 1sec.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        tk.Label(self.parent_frame, text="Exiting Traffic Light Simulator", bg= "white", font="3000").pack()
        self.quit_button.config(state="disabled")
        self.after(1000, self.parent_frame.destroy)

    def create_stoplight(self):
        """
        Configures and draws the Stoplight.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        stoplight = Stoplight(self.stoplight_frame, self.canvas, 100, 100, 300, 600, self.lights)
        stoplight.configure_lights()
        stoplight.create_label()
        stoplight.create_frame()
        stoplight.start_lights(0)
        self.stoplight_frame.pack()

    def __update_stoplight(self, event):
        """
        Redraws the Stoplight using the new light_data. Also displays any errors
        if the input is invalid.

        Parameters
        ----------
        event : any
            Unused in execution but present since when submitting, the event sends event data to the binded function

        Returns
        -------
        None
        """
        self.time_input.config(state="disabled")
        if self.time_input.get().isnumeric():
            if int(self.time_input.get()) < 100:
                 messagebox.showerror("Input Error", "Please enter a number above 100. \nThe fastest recorded human reaction time is 120ms.")
            else:
                self.light_state[int(self.selected.get())][0] = int(self.time_input.get())
                self.canvas.destroy()
                self.stoplight_frame.destroy()
                self.stoplight_frame = tk.Frame(self.parent_frame, width=self.width, height=self.height)
                self.canvas = tk.Canvas(self.stoplight_frame, width=self.width, height=self.height, background="white")
                self.lights = self.__create_lights(self.light_state)
                self.create_stoplight()
        else:
            messagebox.showerror("Input Error", "Negative numbers, decimals, non-numbers, and numbers below 100 are not allowed. Please enter a whole, positive number above 100.")
        self.after(100, self.time_input.config(state="normal"))
