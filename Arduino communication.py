

import serial
import tkinter as tk
import threading

ser = serial.Serial('COM3',115200,timeout=2) 
#change the port as per your Arduino connection

def read_serial():
    while True:
        data = ser.readline().decode().strip()
        if data:
            text1= f"Resistance value = {data}"
            label1.configure(text=text1)
def led_on():
    ser.write(b'1')
def led_off():
    ser.write(b'0')

root = tk.Tk()
root.geometry('300x300')
root.title('Arduino controller')
root.configure(bg='beige')

btn1=tk.Button(root, text='on', command=led_on,font=('Arial',20),bg='gold',fg='white')
btn2=tk.Button(root, text='off', command=led_off,font=('Arial',20),bg='gold',fg='white')
label1=tk.Label(root, text='',font=('Arial',20),bg='gold')
label1.pack(padx=10,pady=10)
btn1.pack(padx=10,pady=10)
btn2.pack(padx=10,pady=10)
threading.Thread(target=read_serial).start()


root.mainloop()
