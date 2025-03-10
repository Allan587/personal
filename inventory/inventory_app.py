import tkinter as tk
from tkinter import Toplevel

#<------------------------------------------------------------------------------------------------------------------------>
class smartfilter_main:
    def __init__(self, root):
        self.root = root
                
        #self.ent()  
        self.lab()
        self.btn()
    
    def lab(self):
        lab = tk.Label(self.root, text="Smart Filter", bg="#E6E6FA", font=("Arial", 16))
        lab.grid(row=0, column=0, columnspan=3, sticky="nsew")
    
    def secondary(self):
        self.secondary_window = sales(self)
        
    def third(self):
        self.third_window = inventory(self)
        
    def forth(self):
        self.forth_window = update_in(self)
           
    def btn(self):
        btn_v = tk.Button(self.root, text="Apartado de Ventas", bg="Grey", command=self.secondary) .place(relx=0.35, rely=0.16, relwidth=0.3,  relheight=0.1)
        btn_i = tk.Button(self.root, text="Inventario", bg="Grey", command=self.third).place(relx=0.35, rely=0.3, relwidth=0.3,  relheight=0.1)
        btn_u = tk.Button(self.root, text="Actualización de Inventario", bg="Grey", command=self.forth).place(relx=0.35, rely=0.44, relwidth=0.3,  relheight=0.1)    
        btn_e = btn_ex = tk.Button(self.root, text="Salir", bg="Red", fg="White", command=self.root.destroy).place(relx=0.35, rely=0.58, relwidth=0.3, relheight=0.05)
#<------------------------------------------------------------------------------------------------------------------------>       
class sales:
    
    def __init__(self, Smartfilter_main):
        self.Smartfilter_main = Smartfilter_main
        
        self.Sales = Toplevel()
        self.Sales.title("Apartado de ventas")
        self.Sales.grab_set()
        self.Sales.minsize(800, 500)
        self.Sales.config(bg="lightblue")
        self.Sales.geometry("800x500")
        
        self.btn()
        self.ent()
        self.lbl()
        
    def lbl(self):
        #inf = list("ID producto", "Nombre", "Marca", "Tipo", "Stock") Finish and make a range with this information
        
        lbl_id = tk.Label(self.Sales, text="ID producto", bg="Grey").place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
        lbl_n = tk.Label(self.Sales, text="Nombre", bg="Grey").place(relx=0.17, rely=0.05, relwidth=0.1, relheight=0.05)
        lbl_b = tk.Label(self.Sales, text="Marca", bg="Grey").place(relx=0.29, rely=0.05, relwidth=0.1, relheight=0.05)
        lbl_a = tk.Label(self.Sales, text="Cantidad", bg="Grey").place(relx=0.41, rely=0.05, relwidth=0.1, relheight=0.05)
        
    def ent(self):  
        # Make entries to display informacion filtered by the user
        ent_id = tk.Entry(self.Sales).place(relx=0.05, rely=0.12, relwidth=0.1, relheight=0.05)
        ent_n =  tk.Entry(self.Sales).place(relx=0.17, rely=0.12, relwidth=0.1, relheight=0.05)
        ent_b =  tk.Entry(self.Sales).place(relx=0.29, rely=0.12, relwidth=0.1, relheight=0.05)
        ent_a =  tk.Entry(self.Sales).place(relx=0.41, rely=0.12, relwidth=0.1, relheight=0.05)
        
    def btn(self):  
        btn_ex = tk.Button(self.Sales, text="Salir", bg="Red", fg="White", command=self.Sales.destroy).place(relx=0.85, rely=0.9, relwidth=0.1, relheight=0.05)
#<------------------------------------------------------------------------------------------------------------------------>       
class inventory:
    
    def __init__(self, Smartfilter_main):
        self.Smartfilter_main = Smartfilter_main
        
        
        self.inventory = Toplevel()
        self.inventory.title("Inventario")
        self.inventory.grab_set()
        self.inventory.minsize(800, 500)
        self.inventory.config(bg="lightblue")
        self.inventory.geometry("800x500")
        
        self.btn()
        self.lbl()
        self.ent()
            
    def lbl(self):    
        lbl_id = tk.Label(self.inventory, text="ID producto", bg="Grey").place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
        lbl_n = tk.Label(self.inventory, text="Nombre", bg="Grey").place(relx=0.17, rely=0.05, relwidth=0.1, relheight=0.05)
        lbl_b = tk.Label(self.inventory, text="Marca", bg="Grey").place(relx=0.29, rely=0.05, relwidth=0.1, relheight=0.05)
        lbl_t = tk.Label(self.inventory, text="Tipo", bg="Grey").place(relx=0.41, rely=0.05, relwidth=0.1, relheight=0.05)
        lbl_s = tk.Label(self.inventory, text="Stock", bg="Grey").place(relx=0.53, rely=0.05, relwidth=0.1, relheight=0.05)
        
    def ent(self):
        #Make entries to show what the users expect
        self.ent_id = tk.Entry(self.inventory).place(relx=0.05, rely=0.12, relwidth=0.1, relheight=0.05)
        self.ent_n =  tk.Entry(self.inventory).place(relx=0.17, rely=0.12, relwidth=0.1, relheight=0.05)
        self.ent_b =  tk.Entry(self.inventory).place(relx=0.29, rely=0.12, relwidth=0.1, relheight=0.05)
        self.ent_t =  tk.Entry(self.inventory).place(relx=0.41, rely=0.12, relwidth=0.1, relheight=0.05)
        self.ent_s =  tk.Entry(self.inventory).place(relx=0.53, rely=0.12, relwidth=0.1, relheight=0.05)
        
    def btn(self):
        btn_ex = tk.Button(self.inventory, text="Salir", bg="Red", fg="White", command=self.inventory.destroy).place(relx=0.85, rely=0.9, relwidth=0.1, relheight=0.05)
    
    def get_products_in(self):
        list [self.ent_id, self.ent_n, self.ent_b, self.ent_t, self.ent_s]
#<------------------------------------------------------------------------------------------------------------------------>
class update_in:
    
    def __init__(self, Smartfilter_main):
        self.Smartfilter_main = Smartfilter_main
        
        
        self.update_inventory = Toplevel()
        self.update_inventory.title("Actualización de Inventario")
        self.update_inventory.grab_set()
        self.update_inventory.minsize(800, 500)
        self.update_inventory.config(bg="lightblue")
        self.update_inventory.geometry("800x500")
        
        self.btn()
        self.lbl()
        self.ent()
            
    def lbl(self):
        #inf = list("ID producto", "Nombre", "Marca", "Tipo", "Stock") Finish and make a range with this information as a display window
        
        lbl_id = tk.Label(self.update_inventory, text="ID producto", bg="Grey").place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
        lbl_a = tk.Label(self.update_inventory, text="Cantidad", bg="Grey").place(relx=0.17, rely=0.05, relwidth=0.1, relheight=0.05)
        
    def ent(self):
    
        ent_id = tk.Entry(self.update_inventory).place(relx=0.05, rely=0.12, relwidth=0.1, relheight=0.05)
        ent_a =  tk.Entry(self.update_inventory).place(relx=0.17, rely=0.12, relwidth=0.1, relheight=0.05)
        
        
    def btn(self):
        #add buttons to display entered items and filter information
        btn_ex = tk.Button(self.update_inventory, text="Salir", bg="Red", fg="White", command=self.update_inventory.destroy).place(relx=0.85, rely=0.9, relwidth=0.1, relheight=0.05)

#<------------------------------------------------------------------------------------------------------------------------>
def main():
    root = tk.Tk()
    root.geometry("800x500")
    root.title("smart_filter") 
    root.minsize(800, 500)
    root.config(bg="lightblue")
    
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    
    app = smartfilter_main(root)

    root.mainloop()  
       
if __name__ == "__main__":
    main()