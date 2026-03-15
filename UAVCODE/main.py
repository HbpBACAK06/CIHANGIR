from tkinter import *
import mission1
from mathexclusive import * 

def startmission1():
    lat1 = float(e1.get('1.0', 'end-1c'))
    lon1 = float(e3.get('1.0', 'end-1c'))
    lat2 = float(e2.get('1.0', 'end-1c'))
    lon2 = float(e4.get('1.0', 'end-1c'))
    det = int(er.get('1.0', 'end-1c'))
    rad = float(ed.get('1.0', 'end-1c'))

    mission1.startmission((lat1,lon1), (lat2,lon2), rad, det)
    

root = Tk()
root.title("UAV Mission Starter")

Label(root, text="First Pylon Latitude").grid(row=0, column=0)
Label(root, text="First Pylon Longitude").grid(row=0, column=3)
Label(root, text="Second Pylon Latitude").grid(row=1, column=0)
Label(root, text="Second Pylon Longitude").grid(row=1, column=3)
Label(root, text="Detail Level").grid(row=2, column=0)
Label(root, text="Turning Radius").grid(row=2, column=3)

e1 = Text(root,height=1, width=15)
e2 = Text(root,height=1, width=15)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

e3 = Text(root,height=1, width=15)
e4 = Text(root,height=1, width=15)
e3.grid(row=0, column=4)
e4.grid(row=1, column=4)
er = Text(root, height=1, width=15)
ed = Text(root, height=1, width=15)
er.grid(row=2, column=1)
ed.grid(row=2, column=4)

button1 = Button(root, 
                   text="Start Mission 1", 
                   command=startmission1,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=1,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   width=20,
                   wraplength=200)

button1.grid(row=3, column=2)

root.mainloop()