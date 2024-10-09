import tkinter as tk

class interface(tk.Frame):
    
    def __init__ (self, master=None):
        super().__init__(master) 
        self.master = master
        self.pack()
        
        self.game_mode()
        
    def game_mode(self):
        
        tk.Button(self, text="Fácil", command=easy_w)
        tk.Button(self, text="Intermadio", command="Algo")
        tk.Button(self, text="Difícil", command="Algo")
        
    def entradas(self):
        tk.Entry(self, str, width= 4)

def main():
    app = tk.Tk()
    app.title("Juego de palabras")
    
    ventana = interface(app)
    ventana.mainloop()

def easy_w():
    window = tk.Tk
    window.title("Modo fácil")
    
    window.mainloop()
if __name__ == "__main__": 
    main() 