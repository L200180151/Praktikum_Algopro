from tkinter import *

my_app = Tk(className='Program Data Diri')

L1 = Label(my_app, text="Data Diri", font=("Arial", 24))
L1.grid(row=0, column=0)
L2 = Label(my_app, text="Nama")
L2.grid(row=1, column=0)
L3 = Label(my_app, text="Arya Mukti A'raafi Zha Putra")
L3.grid(row=1, column=1)
L4 = Label(my_app, text="NIM")
L4.grid(row=2, column=0)
L5 = Label(my_app, text="L200180151")
L5.grid(row=2, column=1)
L6 = Label(my_app, text="Buku Favorit")
L6.grid(row=3, column=0)
L7 = Label(my_app, text="The Count of Monte Cristo")
L7.grid(row=3, column=1)
L8 = Label(my_app, text="Idola")
L8.grid(row=4, column=0)
L9 = Label(my_app, text="Nabi Muhammad SAW")
L9.grid(row=4, column=1)
L10 = Label(my_app, text="Motto")
L10.grid(row=5, column=0)
L11 = Label(my_app, text="Apalah")
L11.grid(row=5, column=1)


def tutup():
    my_app.destroy()

B1 = Button(my_app, text="Tutup", command=tutup)
B1.grid(row=6, column=1)

my_app.mainloop()
