# from Tkinter import *
# import Tkinter, Tkconstants, tkFileDialog
 
# root = Tk()
# root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
# print (root.filename)

import xlrd
book = xlrd.open_workbook('trial.xlsx')
sheet = book.sheet_by_name('Sheet1')
data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
# Profit !
print(data)