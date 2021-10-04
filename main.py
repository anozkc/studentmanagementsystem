from tkinter import *
import time
import random
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import pandas



root = Tk()
root.title('student management system')
root.config(bg="cyan")
root.geometry('1174x700+200+40')
root.iconbitmap("student.ico")
root.resizable(False, False)
