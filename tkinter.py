import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text = "Name")
label2 = tkinter.Label(main_window, text = "Email")

tombol1 = tkinter.Button(main_window, text = "Submit")
tombol2 = tkinter.Button(main_window, text = "Cancel")

label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

main_window.mainloop()