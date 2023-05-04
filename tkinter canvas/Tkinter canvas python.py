import tkinter as tk
import time
ventana = tk.Tk()
ventana.title("League of Legends")
ventana.geometry("300x400+600+150")
ventana.resizable(False,False)
ventana.config(bg = "#FF5733")
dibujo = tk.Canvas(ventana, height = 400, width = 300, bg = "Purple")
dibujo.pack()
dibujo.create_rectangle(100,50,200,350,fill = "#FF5733", width = 2)
a = 10
while True:
    def green():
        
        for i in range(a):
            green = dibujo.create_oval(100,250,200,350,fill = "Green", width = 2)
            ventana.update()
            time.sleep(0.5)
            
    def greenb():
        
        for i in range(a):
            greenb = dibujo.create_oval(100,250,200,350,fill = "Black", width = 2)
            ventana.update()
            time.sleep(0.0001)
            
    def yellow():
        
        for i in range(a):
            green = dibujo.create_oval(100,150,200,250,fill = "Yellow", width = 2)
            ventana.update()
            time.sleep(0.5)
            
    def yellowb():
        
        for i in range(a):
            greenb = dibujo.create_oval(100,150,200,250,fill = "Black", width = 2)
            ventana.update()
            time.sleep(0.0001)
            
    def red():
        
        for i in range(a):
            green = dibujo.create_oval(100,50,200,150,fill = "Red", width = 2)
            ventana.update()
            time.sleep(0.5)
    
    def redb():
        
        for i in range(a):
            greenb = dibujo.create_oval(100,50,200,150,fill = "Black", width = 2)
            ventana.update()
            time.sleep(0.0001)
    
    green()
    greenb()
    yellow()
    yellowb()
    red()
    redb()
            
ventana.mainloop()
            
            
            
            
            
            