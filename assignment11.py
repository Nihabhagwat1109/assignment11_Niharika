#Niharika
import tkinter as tk
import webbrowser as w

def faq_details():
    name = e1.get()
    email = e2.get()
    course = course_var.get()
    source = source_var.get()

    if name and email and course != "Select a course" and source != "Select a source":
        if source == "Instagram ads":
            w.open("https://www.instagram.com/faq/")
        elif source == "YouTube ads":
            w.open("https://www.youtube.com/faq/")
        elif source == "Google ads":
            w.open("https://ads.google.com/faq/")
        elif source == "Facebook ads":
            w.open("https://www.facebook.com/faq/")
        else:
            tk.messagebox.showerror("Error", "Please fill in all the fields.")

root = tk.Tk(className='Course Enquiry Form')


title_ = tk.Label(root, text="Course Enquiry Form", font=("Times New Roman", 16))
title_.grid()

name = tk.Label(root, text="Name:").grid()
e1 = tk.Entry(root,font=('Times New Roman',16))
e1.grid()

email = tk.Label(root, text="Email:").grid()
e2 = tk.Entry(root,font=('Times New Roman',16))
e2.grid()

course = tk.Label(root, text="Course:").grid()
course_var = tk.StringVar()
course_var.set("Select a course")
course_options = ["Python", "Java", "C++", "Web Development", "Javascript"]
course_menu = tk.OptionMenu(root, course_var, *course_options).grid()

source = tk.Label(root, text="Source:")
source.grid()
source_var = tk.StringVar()
source_var.set("Select a source")
source_options = ["Instagram ads", "YouTube ads", "Google ads", "Facebook ads", "Other"]
source_menu = tk.OptionMenu(root, source_var, *source_options).grid()

sbt = tk.Button(root,text='Submit',command=faq_details) 
sbt.grid()
root.mainloop()
#Niharika