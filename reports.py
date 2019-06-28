#import module from tkinter for UI
from tkinter import *
from datetime import datetime;
import os

#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("600x600")

def function1():
    
    os.system("py face_datasets.py")
    
def function2():
    
    os.system("py training.py")

def function3():

    os.system("py face_recognition.py")

def function4():

    root.destroy()



def attend():
    os.startfile(os.getcwd()+"/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xls')


#stting title for the window
root.title("Automatic Attendence Using Face Recognition")

#creating a text label
Label(root, text="Face Recognition ",font=("times new roman",20),fg="white",bg="red",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#lbl = Label(root, text="Enter ID",width=20  ,height=2  ,font=('times', 15, ' bold ') )
#lbl.grid(row=2, column =0)

#creating a button
Button(root,text="Record Images",font=("times new roman",20),bg="#3F51B5",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Train Data",font=("times new roman",20),bg="#3F51B5",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Recognize",font=('times new roman',20),bg="#3F51B5",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating the attendance button

Button(root,text="Attendance Sheet",font=('times new roman',20),bg="#3F51B5",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating five button
Button(root,text="Exit",font=('times new roman',20),bg="red",fg="white",command=function4).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
