import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib

# ------------------------------- Beginning of Matplotlib helper code -----------------------
matplotlib.use('TkAgg')


def draw_figure(x_values, y_values, canvas):
    fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    fig.add_subplot(111).scatter(x_values, y_values)

    figure_canvas_agg = FigureCanvasTkAgg(fig, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg



sg.theme('Dark Amber')  # Let's set our own color theme

leftLayout = [
    [sg.Text("X values")],
    [sg.Input(key='-XVALS-')],
    [sg.Text("Y values")],
    [sg.Input(key='-YVALS-')],
    [sg.StatusBar('StatusBar')],
    [sg.Button("Plot")]
]
rightLayout = [
    [sg.Canvas(key='-CANVAS-')]
]
# STEP 1 define the layout
layout = [[sg.Text('Plot test')],
          [sg.Col(leftLayout), sg.Col(rightLayout)],
          [sg.Button('Ok'), sg.Button('Exit')]]

# create the form and show it without the plot
window = sg.Window('Matplotlib Single Graph', layout, location=(0, 0), finalize=True, element_justification='center',
                   font='Helvetica 18')

# add the plot to the window
fig_agg = None
while True:
    event, values = window.read()
    print(event, values)
    if event == 'Plot':
        x_values = list(map(float, (values['-XVALS-'].split(","))))
        y_values = list(map(float, (values['-YVALS-'].split(","))))
        if fig_agg is not None:
            fig_agg.get_tk_widget().forget()
        fig_agg = draw_figure(x_values, y_values, window['-CANVAS-'].TKCanvas)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
window.close()
