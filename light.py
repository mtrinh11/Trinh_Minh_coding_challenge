import tkinter as tk

class Light(tk.Frame):
    """
    A class used to represent a Light.

    ...

    Attributes
    ----------
    time_on : int
        The number of milliseconds the light should be on for

    Methods
    -------
    on()
        Draws the light in its on appearance. 
    off()
        Draws the light in its off appearance.
    """
    time_on = 0

    def __init__(self, parent_frame, canvas, time_on, color, x0, y0, x1, y1):
        """
        Parameters
        ----------
        parent_frame : tkinter.Frame
            The parent frame that the light will be drawn within.
        canvas : tkinter.Canvas
            The canvas that the light will be drawn on.
        time_on : int
            The amount of time the light should be on for in milliseconds. 
        color : str
            The color of the light.
        x0 : int
            The x-value of the top left coordinate.
        y0 : int
            The y-value of the top left coordinate.
        x1 : int
            The x-value of the bottom right coordinate.
        y1 : int
            The y-value of the bottom right coordinate.
        """
        super().__init__(parent_frame)
        self.parent_frame = parent_frame
        self.canvas = canvas
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.color = color
        self.time_on = time_on
        self.pack()
   
    def on(self):
        """
        Draws the ellipse within the coordinates 
        defined in creation of the Light object. The ellipse has the color defined 
        in the creation of the Light object. 

        Parameters
        ----------
        None

        Returns
        -------
        None

        """
        self.canvas.delete(f"{self.color}off")
        self.canvas.create_oval(self.x0, self.y0, self.x1, self.y1, fill=self.color, width=5)
        self.canvas.pack()

    def off(self):
        """
        Draws the ellipse within the coordinates 
        defined in the creation of the Light object. The ellipse has a grey color to 
        display that it is off to the user.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.canvas.delete(f"{self.color}on")
        self.canvas.create_oval(self.x0, self.y0, self.x1, self.y1, fill="grey", width=5)
        self.canvas.pack()

