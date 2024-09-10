import tkinter as tk
from tkinter import ttk
import time

def start():
    GB = 100
    download = 0
    speed = 1
    
    while download < GB:
        time.sleep(0.05)
        progress_bar['value'] += (speed/GB)*100
        download += speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download) +"/"+str(GB)+" GB completed")
        window.update_idletasks()

window = tk.Tk()

percent = tk.StringVar()
text = tk.StringVar()

progress_bar = ttk.Progressbar(window, orient=tk.HORIZONTAL, length=300)
progress_bar.pack(pady=10)

percent_label = tk.Label(window, textvariable=percent).pack()
task_label = tk.Label(window, textvariable=text).pack()

button = tk.Button(window, text='Download', command=start).pack()

window.mainloop()