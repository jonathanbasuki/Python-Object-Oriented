import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text = "Name")
label2 = tkinter.Label(main_window, text = "Email")

button1 = tkinter.Button(main_window, text = "Submit")
button2 = tkinter.Button(main_window, text = "Cancel")

label1.pack()
label2.pack()
button1.pack()
button2.pack()

main_window.mainloop()
