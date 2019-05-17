# This program uses tkinter and calculates the windchill
# from the fahrenheit temperature and wind speed.

# Author: Giancarlo D'Ambrosio

import tkinter

class WindchillConverterGUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create three frames to group widgets.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create widgets for the top frame.
        self.title_label = tkinter.Label(self.top_frame, text = 'Windchill Calculator', bg='yellow')
        self.temp_label = tkinter.Label(self.top_frame, text ='Enter the temperature in degrees Fahrenheit:')
        self.temp_entry = tkinter.Entry(self.top_frame, width = 10)
        # Pack the top frame's widgets.
        self.title_label.pack(side='top')
        self.temp_label.pack(side='left')
        self.temp_entry.pack(side='left')

        # Create widgets for the middle frame.
        self.speed_label = tkinter.Label(self.mid_frame, text = 'Enter the wind speed in mph:')
        self.speed_entry = tkinter.Entry(self.mid_frame, width = 10)
        # Pack the middle frame's widgets.
        self.speed_label.pack(side='left')
        self.speed_entry.pack(side='left')

        # Create button widget for bottom frame.
        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate Windchill', command=self.windchillCalc)
        # Create widget for bottom.
        self.descr_label = tkinter.Label(self.bottom_frame, text = 'The windchill temperature is: ')
        # Get a StringVar object to use.
        self.value = tkinter.StringVar()
        # Create label associated with StringVar.
        self.miles_label = tkinter.Label(self.bottom_frame, textvariable=self.value)

        # Pack the bottom frame's widgets.
        self.calc_button.pack(side='top')
        self.descr_label.pack(side='left')
        self.miles_label.pack(side = 'left')

        # Pack the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
    # Create function to callback in the Calculate button.
    def windchillCalc(self):
        # Get temperature and speed values entered by user.
        temperature = float(self.temp_entry.get())
        windSpeed = float(self.speed_entry.get())
        # Calculate then round the windchill.
        windchill_raw = 35.74 + 0.6215 * temperature - 35.75 * windSpeed**0.16 +\
                        0.4275 * temperature * windSpeed**0.16
        windchill = round(windchill_raw, 2)
        # Convert the windchill to a string and store it in the StringVar object.
        self.value.set(str(windchill) + ' degrees fahrenheit')

windchill_conv = WindchillConverterGUI()
