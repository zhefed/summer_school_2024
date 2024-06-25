import socket
import tkinter as tk


line_id = None
line_points = []
line_options = {}


def close():
    root.quit()
    s.close()


def draw(event):
    global line_id
    line_points.extend((event.x, event.y))
    if line_id is not None:
        canvas.delete(line_id)
    line_id = canvas.create_line(line_points, **line_options)


def end():
    global line_id
    line_points.clear()
    line_id = None
    s.send(f"del {line_id}".encode())


def listen():
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            data = data.decode()
            if data.startswith('draw'):
                line_id = data.split()[1]
                x, y = map(int, data.split()[2:])
                event = type('', (object,), {'line_id': line_id, 'x': x, 'y': y})()
                draw(event)
            else:
                end()
            root.update()
        except Exception as e:
            print(e)


root = tk.Tk()
root.title("Server")
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 3000))
s.listen(1)
conn, addr = s.accept()


root.after(0, listen)
root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
