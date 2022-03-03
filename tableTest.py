from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib

values = [[sg.Input(),"b","a"],["b","c","j"]]
headings =["X Values","Y Values", "Y Errors"]
table = sg.Table(values,headings=headings,expand_x = True,expand_y = True)

layout = [[sg.Text("Table Title")], [table]]
window = sg.Window('Matplotlib Single Graph', layout, location=(0, 0), finalize=True, element_justification='center',
                   font='Helvetica 18',size=(1200, 800),resizable=True)

# add the plot to the window
fig_agg = None
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
window.close()
