import tkinter as tk

class MainApp(tk.Tk):
    def __init__(self):
      super().__init__()
      self.geometry("200x300")
      self.title("Primera ventanita")

if __name__=="__main__":
    app=MainApp()
    app.mainloop()
