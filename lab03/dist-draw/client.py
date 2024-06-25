import socket
import tkinter as tk

line_id = None
line_points = []
line_options = {}
connected = False


def draw(event):
    global line_id
    line_points.extend((event.x, event.y))
    if line_id is not None:
        canvas.delete(line_id)
    line_id = canvas.create_line(line_points, **line_options)
    s.send(f"draw {line_id} {event.x} {event.y}".encode())


def start(event):
    line_points.extend((event.x, event.y))


def end(event=None):
    global line_id
    line_points.clear()
    line_id = None
    s.send(f"del".encode())


root = tk.Tk()
root.title("Client")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

canvas.bind('<Button-1>', start)
canvas.bind('<B1-Motion>', draw)
canvas.bind('<ButtonRelease-1>', end)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 3000))

root.mainloop()
