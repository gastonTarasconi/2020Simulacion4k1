import tkinter as tk
from tkinter import messagebox
from tp1.MethodCongruencialesMixto import MethodCongrualesMixto
from tp1.MethodCongruencialesMultiplicativo import MethodCongrualesMultiplicativo

ACCURACY = 4

root = tk.Tk()
root.title('SIM 4K1 2020 Trabajo práctico N°1')
root.geometry('320x125')
# root.iconbitmap('favicon.ico')


def generar_otro(actual_method, textarea):
    textarea.insert(tk.END, str(actual_method.get_random()) + '\n')
    textarea.see(tk.END)


def generar20(method, textarea, btn_otro, xo, k, g, c, a, m):
    actual_generator = None
    textarea.delete(1.0, tk.END)

    if xo == '':
        xo = 0
    if k == '':
        k = 0
    if g == '':
        g = 0
    if c == '':
        c = 0
    if a == '':
        a = 0
    if m == '':
        m = 0

    if method == 1:
        actual_generator = MethodCongrualesMixto(xo, k, g, c, ACCURACY)
    elif method == 2:
        actual_generator = MethodCongrualesMultiplicativo(xo, k, g, ACCURACY)

    # esto por si le queremos imponer algún parámetro
    if a != 0:
        actual_generator.a = int(a)
    if m != 0:
        actual_generator.m = int(m)

    for i in range(20):
        textarea.insert(tk.END, str(actual_generator.get_random()) + '\n')

    btn_otro.configure(command=lambda: generar_otro(actual_generator, textarea))


def open_a():
    top = tk.Toplevel()
    # top.geometry('840x620')
    top.title('Generador de Números PseudoAleatorios')
    # tk.Button(top, text='Cerrar Ventana', command=top.destroy).grid(row=0, column=9)

    r = tk.IntVar()
    r.set(1)

    tk.Radiobutton(top, text='Método Congruales Mixto', variable=r, value=1).grid(row=1, column=1)
    tk.Radiobutton(top, text='Método Congruales Multiplicativo', variable=r, value=2).grid(row=1, column=2)

    tk.Label(top, text='Número Semilla:').grid(row=2, column=1)
    xo = tk.Entry(top, width=20)
    xo.grid(row=2, column=2)

    tk.Label(top, text='Parámetro K:').grid(row=3, column=1)
    k = tk.Entry(top, width=20)
    k.grid(row=3, column=2)

    tk.Label(top, text='Parámetro G:').grid(row=4, column=1)
    g = tk.Entry(top, width=20)
    g.grid(row=4, column=2)

    tk.Label(top, text='Parámetro C: (Congruales Mixto)').grid(row=5, column=1)
    c = tk.Entry(top, width=20)
    c.grid(row=5, column=2)

    tk.Label(top, text='Parámetro A:').grid(row=6, column=1)
    a = tk.Entry(top, width=20)
    a.grid(row=6, column=2)

    tk.Label(top, text='Parámetro M:').grid(row=7, column=1)
    m = tk.Entry(top, width=20)
    m.grid(row=7, column=2)

    textarea = tk.Text(top, height=15, width=65)
    # Read only
    textarea.bind('<Key>', lambda e: 'break')
    textarea.grid(row=9, column=1, columnspan=3)

    btn_otro = tk.Button(top, text='Generar Otro?')
    btn_otro.grid(row=10, column=3, pady=5)

    tk.Button(top, text='Generar 20',
              command=lambda: generar20(r.get(), textarea, btn_otro,
                                        xo.get(), k.get(), g.get(),
                                        c.get(), a.get(), m.get())
              ).grid(row=2, column=3, padx=5)


def open_b():
    top = tk.Toplevel()
    top.geometry('840x620')
    top.title('Prueba de Frecuencia Números PseudoAleatorios Python')
    tk.Button(top, text='Cerrar Ventana', command=top.destroy).grid(row=0, column=9)


def open_c():
    top = tk.Toplevel()
    top.geometry('840x620')
    top.title('Prueba de Frecuencia Números PseudoAleatorios Método Congruales Mixto')
    tk.Button(top, text='Cerrar Ventana', command=top.destroy).grid(row=0, column=9)


def popup():
    # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    messagebox.showinfo('Title', 'Message')


lbl = tk.Label(root, text='Hello World!')
lbl2 = tk.Label(root, text='Gasti')

btn = tk.Button(root, text='Números Pseudos aleatorios', padx=20, command=open_a).pack(pady=3)
btn2 = tk.Button(root, text='Prueba en Frecuencia Python', padx=20, command=open_b).pack(pady=3)
btn3 = tk.Button(root, text='Prueba Frecuencia Congruales Mixto', padx=20, command=open_c).pack(pady=3)


# lbl.grid(row=0, column=0)
# lbl2.grid(row=1, column=0)
# btn.grid(row=0, column=1)
# btn2.grid(row=1, column=1, pady=3, sticky=W+E)
#
# btn.grid(pady=3)
# btn2.grid(pady=3)
# btn3.pack(pady=3)

# popup()

root.mainloop()
