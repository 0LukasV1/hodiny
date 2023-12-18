import tkinter as tk
from datetime import datetime
win = tk.Tk()
canvas = tk.Canvas(win, width=900, height=300, bg="white")
canvas.pack()
class line:
    def __init__(self, point: tuple, dx: int, dy: int, canvas, colour):
        self.coords = point
        self.dx = dx
        self.dy = dy
        self.canvas = canvas
        self.colour = colour
        self.id = canvas.create_polygon(point[0], point[1], point[0]+dx/2, point[1]-dy/7, point[0] + dx, point[1],
                                        point[0] + dx, point[1] + dy, point[0]+dx/2, point[1]+(7/6)*dy, point[0],
                                        point[1] + dy, fill=colour, outline="")
    def on(self):
            self.canvas.itemconfig(self.id, fill=self.colour)
    def off(self):
            self.canvas.itemconfig(self.id, fill="white")
class horline(line):
    def __init__(self, point: tuple, dx: int, dy: int, canvas, colour):
        self.coords = point
        self.dx = dx
        self.dy = dy
        self.canvas = canvas
        self.colour = colour
        self.id = canvas.create_polygon(point[0]-dx/7, point[1]+dy/2, point[0] + dx/7, point[1],point[0] + (6/7)*dx,
                                        point[1], point[0]+dx*(8/7), point[1]+dy/2, point[0]+(6/7)*dx, point[1] + dy,
                                        point[0]+dx/7, point[1]+dy, fill=colour, outline="")
class segment:
    def __init__(self, point: tuple, small: int, big: int, canvas, colour: str):
        self.parts = []
        self.colour = colour
        sx = point[0]
        sy = point[1]
        self.coords = point
        self.parts.append(horline((sx + small, sy), big, small, canvas, colour))  # segment0
        self.parts.append(line((sx + small + big, sy + small), small, big, canvas, colour))  # segment1
        self.parts.append(horline((sx + small, sy + small + big), big, small, canvas, colour))
        self.parts.append(line((sx, sy + small), small, big, canvas, colour))
        self.parts.append(line((sx + small + big, sy + 2 * small + big), small, big, canvas, colour))
        self.parts.append(horline((sx + small, sy + 2 * big + 2 * small), big, small, canvas, colour))
        self.parts.append(line((sx, sy + 2 * small + big), small, big, canvas, colour))
    def reset(self):
        for part in self.parts:
            part.off()
    def error(self):
        for part in self.parts:
            part.on()
    def display(self, number: int):
        if number == 0:
            self.error()
            self.parts[2].off()
        if number == 1:
            self.reset()
            self.parts[1].on()
            self.parts[4].on()
        elif number == 2:
            self.error()
            self.parts[3].off()
            self.parts[4].off()
        elif number == 3:
            self.error()
            self.parts[3].off()
            self.parts[6].off()
        elif number == 4:
            self.error()
            self.parts[0].off()
            self.parts[5].off()
            self.parts[6].off()
        elif number == 5:
            self.error()
            self.parts[1].off()
            self.parts[6].off()
        elif number == 6:
            self.error()
            self.parts[1].off()
        elif number == 7:
            self.error()
            self.parts[2].off()
            self.parts[3].off()
            self.parts[6].off()
            self.parts[5].off()
        elif number == 8:
            self.error()
        elif number == 9:
            self.error()
            self.parts[6].off()
class Clock:
    def __init__(self, point: tuple, big: int, small: int, canvas, colour):
        self.numms = []
        self.coords = point
        self.coordzies = []
        self.small = small
        self.big = big
        self.point = point
        self.canvas = canvas
        self.colour = colour
        for i in range(6):
            self.coordzies.append(segment((self.point[0] + i * (2 * self.small + self.big + 10), self.point[1]), self.big, self.small, self.canvas, self.colour))
        self.bod1 = canvas.create_oval(320, 130, 340, 150, fill="white")
        self.bod2 = canvas.create_oval(320, 210, 340, 230, fill="white")
        self.bod3 = canvas.create_oval(570, 130, 590, 150, fill="white")
        self.bod4 = canvas.create_oval(570, 210, 590, 230, fill="white")
    def hodziny(self):
        self.numms = []
        cas = datetime.now().strftime('%H%M%S')
        for i in range(6):
            cisliica = cas[i]
            self.coordzies[i].display(int(cisliica))
        if datetime.now().second % 2 == 0:
            self.canvas.itemconfig(self.bod1, fill="blue")
            self.canvas.itemconfig(self.bod2, fill="blue")
            self.canvas.itemconfig(self.bod3, fill="blue")
            self.canvas.itemconfig(self.bod4, fill="blue")
        else:
            self.canvas.itemconfig(self.bod1, fill="white")
            self.canvas.itemconfig(self.bod2, fill="white")
            self.canvas.itemconfig(self.bod3, fill="white")
            self.canvas.itemconfig(self.bod4, fill="white")
        win.after(1000, skuska.hodziny)
skuska = Clock((100, 100), 15, 50, canvas, "blue")
skuska.hodziny()
win.mainloop()
