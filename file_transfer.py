import datetime
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #set window title
        self.master.title("File Transfer")
        
        #create button to select files from source dir
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #position button in tk grid
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #create entry for source dir
        self.source_dir = Entry(width=75)
        #position entry field, match padding with buttons
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #create button to select destination from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #position destination button under source button
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #create tranfer button
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #position transfer button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #create exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #position exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

        #create entry for destination dir
        self.destination_dir = Entry(width = 75)
        #position and match entry as above
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #.delete(0, END) clears Entry widget content,
        #allowing the source dir path to be inserted
        self.source_dir.delete(0, END)
        #insert user selection into source_dir Entry
        self.source_dir.insert(0, selectSourceDir)
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)
    #transfers files from one directory to another
    def transferFiles(self):
        #get source dir
        source = self.source_dir.get()
        #get destination dir
        destination = self.destination_dir.get()
        #gets files from source dir
        source_files = os.listdir(source)
        #enumerates files in source dir
        for i in source_files:
            path = (source + '/' + i)
            #get current time
            today = datetime.datetime.now()
            hours = (today.timestamp()//3600)
            #get file mod time
            file_mod_time = (os.path.getmtime(path)//3600)
            #compare times
            age = hours - file_mod_time
            if age < 24.0:
                #moves files from source to destination
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred.')
            else:
                print(i + ' has not been recently updated.\n')

    #create exit function
    def exit_program(self):
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
