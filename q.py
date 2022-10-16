import tkinter
import random
import time

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=400, height=400)
canvas.pack()

colors = ['green', 'blue', 'red']
circles = []

for i in range(5):
    r = random.randint(10, 40)
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    a = {'dx': random.randint(-10, 10),
         'dy': random.randint(-10, 10),
         'id': canvas.create_oval(x - r, y - r, x + r, y + r, fill=random.choice(colors))}
    circles.append(a)

while True:
    for circle in circles:
        x0, y0, x1, y1 = canvas.coords(circle['id'])
        if x0 < 0 or x1 > 400:
            circle['dx'] = -circle['dx']
        if y0 < 0 or y1 > 400:
            circle['dy'] = -circle['dy']
        canvas.move(circle['id'], circle['dx'], circle['dy'])

    canvas.update()
window.mainloop()