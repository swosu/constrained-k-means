import pandas as pd
import sys
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

try:
    # for Python2
    from Tkinter import *   
except ImportError:
    # for Python3
    from tkinter import *   
try:
    # for Python2
    import Tkinter as tk  
except ImportError:
    # for Python3
    import tkinter as tk
try:
    # for Python2
    import Tkinter, Tkconstants, TkFileDialog  
except ImportError:
    #for Python 3
    from tkinter import filedialog   

root= tk.Tk()


canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='k-Means Clustering')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type Number of Clusters:')
label2.config(font=('helvetica', 8))
canvas1.create_window(200, 120, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def getExcel ():
    global df

    root = Tk()
    #root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = ("all   files","*.*")))
    try:
        # for Python2
        root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("excel files","*.xcls"),("all files","*.*")))
    except:
        root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("excel files","*.xcls"),("all   files","*.*"))

    file_path = filedialog.askopenfilename()
    read_file = pd.read_excel (file_path)
    df = DataFrame(read_file,columns=['x','y'])  
    	
browseButtonExcel = tk.Button(text=" Import Excel File ", command=getExcel, bg='green', fg='white', font=('helvetica', 10, 'bold'))
canvas1.create_window(200, 70, window=browseButtonExcel)

def getKMeans ():
    global df
    global numberOfClusters
    numberOfClusters = int(entry1.get())
    
    kmeans = KMeans(n_clusters=numberOfClusters).fit(df)
    centroids = kmeans.cluster_centers_
    
    label3 = tk.Label(root, text= centroids)
    canvas1.create_window(200, 250, window=label3)
    
    figure1 = plt.Figure(figsize=(4,3), dpi=100)
    ax1 = figure1.add_subplot(111)
    ax1.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
    ax1.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
    scatter1 = FigureCanvasTkAgg(figure1, root) 
    scatter1.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
    
processButton = tk.Button(text=' Process k-Means ', command=getKMeans, bg='brown', fg='white', font=('helvetica', 10, 'bold'))
canvas1.create_window(200, 170, window=processButton)

root.mainloop()
