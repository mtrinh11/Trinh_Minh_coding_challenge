from light import Light
from stoplight import Stoplight
from stoplightwindow import StoplightWindow
import tkinter as tk
import unittest

class TestLight(unittest.TestCase):
    def setUp(self):
        self.test_frame = tk.Tk()
        self.test_canvas = tk.Canvas(self.test_frame, width=100, height=100, background="white")
        self.test_light = Light(self.test_frame, self.test_canvas, 400, "green", 150, 450, 250, 550)

    def test_light_creation(self):
        assert len(self.test_frame.winfo_children()) == 2
        assert len(self.test_canvas.find_all()) == 0

    def test_light_on(self):
        assert len(self.test_canvas.find_all()) == 0
        assert len(self.test_frame.winfo_children()) == 2
        self.test_light.on()
        assert len(self.test_canvas.find_all()) == 1
        assert len(self.test_frame.winfo_children()) == 2

    def test_light_off(self):
        assert len(self.test_canvas.find_all()) == 0
        assert len(self.test_frame.winfo_children()) == 2
        self.test_light.off()
        assert len(self.test_canvas.find_all()) == 1
        assert len(self.test_frame.winfo_children()) == 2

class TestStoplight(unittest.TestCase):
    def setUp(self):
        self.test_frame = tk.Tk()
        self.test_canvas = tk.Canvas(self.test_frame, width=100, height=100, background="white")
        self.test_lights_arr = [
            Light(self.test_frame, self.test_canvas, 1000, "red", 150, 150, 250, 250),
            Light(self.test_frame, self.test_canvas,  500, "yellow", 150, 300, 250, 400),
            Light(self.test_frame, self.test_canvas,  200, "green", 150, 450, 250, 550)
        ]
        self.test_stoplight = Stoplight(self.test_frame, self.test_canvas, 100, 100, 300, 600, self.test_lights_arr)
    
    def test_stoplight_creation(self):
        assert len(self.test_frame.winfo_children()) == 5
        assert len(self.test_canvas.find_all()) == 0
        
    def test_create_frame(self):
        assert len(self.test_canvas.find_all()) == 0
        assert len(self.test_frame.winfo_children()) == 5
        self.test_stoplight.create_frame()
        assert len(self.test_canvas.find_all()) == 1
        assert len(self.test_frame.winfo_children()) == 5
        
    def test_configure_lights(self):
        assert len(self.test_canvas.find_all()) == 0
        assert len(self.test_frame.winfo_children()) == 5
        self.test_stoplight.configure_lights()
        assert len(self.test_canvas.find_all()) == 3
        assert len(self.test_frame.winfo_children()) == 5

    def test_create_label(self):
        assert len(self.test_canvas.find_all()) == 0
        assert len(self.test_frame.winfo_children()) == 5
        self.test_stoplight.create_label()
        assert len(self.test_canvas.find_all()) == 0
        assert len(self.test_frame.winfo_children()) == 6

class TestStoplightWindows(unittest.TestCase):
    def setUp(self):
        self.test_frame = tk.Tk()
        self.test_width = 500
        self.test_length = 1000
        self.test_stoplight_window = StoplightWindow(self.test_frame, self.test_width, self.test_length)
        
    def test_stoplight_window_creation(self):
        assert len(self.test_frame.winfo_children()) == 2

    def test_create_stoplight_input(self):
        assert len(self.test_frame.winfo_children()) == 2
        self.test_stoplight_window.create_stoplight_input()
        assert len(self.test_frame.winfo_children()) == 4

    def test_create_stoplight_radiobutton(self):
        assert len(self.test_frame.winfo_children()) == 2
        self.test_stoplight_window.create_stoplight_radiobutton()
        assert len(self.test_frame.winfo_children()) == 5

    def test_create_quit_button(self):
        assert len(self.test_frame.winfo_children()) == 2
        self.test_stoplight_window.create_quit_button()
        assert len(self.test_frame.winfo_children()) == 3

    def test_create_stoplight(self):
        assert len(self.test_frame.winfo_children()) == 2
        self.test_stoplight_window.create_stoplight()
        assert len(self.test_frame.winfo_children()) == 2

if __name__ == "__main__":
    unittest.main()