import tkinter as tk
import time
ventana = tk.Tk()
ventana.title("Volunteer-Me")
ventana.geometry("1024x768")
ventana.resizable(True,True)
ventana.config(bg = "#269c8c")
dibujo = tk.Canvas(ventana, height = 1024, width = 768, bg = "#269c8c")
dibujo.pack()
dibujo.create_rectangle(100,50,200,350,fill = "#269c8c", width = 2)
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
            
            
            
            
            
            