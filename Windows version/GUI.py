from tkinter import *
from tkinter import messagebox
import resultdownloader


window = Tk()
window.title("RTMNU Result Leecher  =-ElmnTrix-=")
title_label = Label(window, text="***___ELMNTRIX___***", bg="black", fg="Red")
title_label.configure(font=("Times New roman", 16, "bold"))
title_label.place(x=90, y=40)

title2_label = Label(window, text="***RTMNU  BCA Results Extractor ***", bg="black", fg="orange")
title2_label.configure(font=("Monotype Corsiva", 12, "italic"))
title2_label.place(x=90, y=95)

roll_label = Label(window,text="\nEnter Your Roll Number of \n BCA FOURTH SEMESTER \n( e.g. 470240 )", fg="purple", bg ="black")
roll_label.place(x=130, y=120)

roll_entry = Entry(window, fg="saddle brown", bg="azure")
roll_entry.configure(width = 40)
roll_entry.place(x=90, y=200)

def result(event):
	global roll_entry
	roll_no = ""
	roll_no = roll_entry.get()

	if roll_no == "":
		messagebox.showerror("Error", "Please Enter Roll Number before you proceed")
		return
	else:
		fun_object = resultdownloader.result(roll_no)



#### PROCEED BUTTON
proceed_Label = Label(window, text ="STEP 2:\nSmash the Button" ,fg="purple", bg ="black" )
proceed_Label.place(x=145, y=250)

proceed_button = Button(window, text="Save Result", bg="light goldenrod", fg="black")
proceed_button.bind("<Button-1>", result)
proceed_button.place(x=147, y=290)


window.configure(background="black")
window.configure(height=500, width =400)
window.resizable(0,0)
window.mainloop()
