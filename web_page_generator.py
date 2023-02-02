import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.entry = Entry(width=30)
        self.entry.grid(padx=(10, 10), pady=(10, 10))
        self.btn = Button(self.master, text="Add Your Text", width=30, height=2, command=self.customHTML)
        self.btn.grid(padx=(10, 10), pady=(10, 10))

    
    def customHTML(self):
        customText = self.entry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + customText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
