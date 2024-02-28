import tkinter as tk

class Stoplight(tk.Frame):
    """
    A class used to represent a Stoplight

    ...

    Attributes
    ----------
    None

    Methods
    -------
    create_frame()
        Draw the frame of the Stoplight
    configure_lights()
        Draws the lights in the off position in the Stoplight
    start_lights(index)
        Start the stoplight cycle.
    create_label()
        Creates the text that displays the timers of each light
        in the stoplight.
    """

    def __init__(self, parent_frame, canvas, x0, y0, x1, y1, lights):
        """
        Parameters
        ----------
        parent_frame : tkinter.Frame
            The parent frame that the light will be drawn within.
        canvas : tkinter.Canvas
            The canvas that the light will be drawn on.
        x0 : int
            The x-value of the top left coordinate
        y0 : int
            The y-value of the top left coordinate.
        x1 : int
            The x-value of the bottom right coordinate.
        y1 : int
            The y-value of the bottom right coordinate.
        lights : list
            A list of Light objects to be displayed on the Stoplight.
        """
        super().__init__(parent_frame)
        self.parent_frame = parent_frame
        self.canvas = canvas
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.lights = lights
        self.pack()

    def create_frame(self):
        """
        Draw the Stoplight frame using the coordinates 
        defined in the creation of the Stoplight object. 

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, width=5)
        self.canvas.pack()
        
    def configure_lights(self):
        """
        Draws all the Light objects in the self.light array 
        on the canvas in its off configuration.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        for light in self.lights:
            light.off()

    def start_lights(self, index):
        """
        Turns on the Stoplight with the first light being configurable.

        Parameters
        ----------
        index : int
            The index of the first light to be turned on.

        Returns
        -------
        None
        """
        self.lights[index].on()
        self.after(self.lights[index].time_on, lambda: self.__light_switcher(index))   

    def __light_switcher(self, index):
        """
        Contains the logic to turn the lights on and off in the correct
        order with the correct timings.

        Parameters
        ----------
        index : int
            The index of the light to be turned on.

        Returns
        -------
        None
        """
        self.lights[index].off()
        if index == len(self.lights) - 1:
            index = 0
            self.start_lights(index)
        else:
            self.start_lights(index + 1)
    
    def create_label(self):      
        """
        Prints to the screen the current timers for each of the lights.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """  
        label_text = "Current Timers: \n "
        for light in self.lights:
            label_text += f"{light.color}:  {light.time_on} ms \n"
        self.light_timers_label = tk.Label(self.parent_frame, text=f"{label_text}", )
        self.light_timers_label.pack()
