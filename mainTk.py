import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from tp1.MethodCongruencialesMixto import MethodCongrualesMixto
from tp1.MethodCongruencialesMultiplicativo import MethodCongrualesMultiplicativo
from tp1.TestChiCuadrado import TestChiCuadrado

import random
from utils.tools import truncate
from tp1.exports.ToExcel import ToExcel
from tp1.exports.ToGraph import ToGraph

ACCURACY = 4

root = tk.Tk()
root.title('SIM 4K1 2020 Trabajo práctico N°1')
# root.geometry('320x125')
root.geometry('450x100')
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


def get_random_numbers_congruales_mixto(n):
    # TODO: desde un n y un s, obtener xo k c g para congruales mixto
    # example
    # random_numbers = [0.15, 0.22, 0.41, 0.65, 0.84,
    #                   0.81, 0.62, 0.45, 0.32, 0.07,
    #                   0.11, 0.29, 0.58, 0.73, 0.93,
    #                   0.97, 0.79, 0.55, 0.35, 0.09,
    #                   0.99, 0.51, 0.35, 0.02, 0.19,
    #                   0.24, 0.98, 0.10, 0.31, 0.17]
    # subintervals = int(math.sqrt(len(random_numbers)))

    # for i in range(n):
    pass


def get_random_numbers_python(n):
    for i in range(n):
        yield truncate(random.random(), ACCURACY)


def generar_grafico_y_xls(method, n, s):
    xls_name = None
    random_numbers = None

    if n == '' or s == '':
        popup('Falta cantidad y de subintervalos')
        return

    n = int(n)
    s = int(s)

    if method == 1:
        xls_name = 'prueba_frecuencia_python'
        random_numbers = get_random_numbers_python(n)
    elif method == 2:
        xls_name = 'prueba_frecuencia_congrual_mixto'

    t = TestChiCuadrado(random_numbers, n, s, ACCURACY)
    t.do_test()

    ToExcel.create_excel(t, xls_name)

    topgraph = tk.Toplevel()
    topgraph.geometry('1024x768')
    topgraph.title('Gráfico')
    show_graph(topgraph, t)


def show_graph(top, t):
    intervalos = []
    freq_observadas = []
    freq_esperadas = []

    for key in t.freq_esperadas:
        freq_observadas.append(t.freq_observ[key])
        freq_esperadas.append(t.freq_esperadas[key])

    for i in range(len(t.labels)):
        intervalos.append(t.labels[i][1])

    # generar graph
    fig = ToGraph.get_graph(intervalos, freq_observadas, freq_esperadas)
    bar = FigureCanvasTkAgg(fig, master=top)
    bar.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    # matplotlib toolbar
    toolbar = NavigationToolbar2Tk(bar, top)
    toolbar.update()
    bar.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


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
    # top.geometry('840x620')
    top.title('Prueba de Frecuencia Números PseudoAleatorios Python')
    # tk.Button(top, text='Cerrar Ventana', command=top.destroy).grid(row=0, column=9)

    tk.Label(top, text='Números a generar:').grid(row=2, column=1)
    n_generar = tk.Entry(top, width=20)
    n_generar.grid(row=2, column=2)

    tk.Label(top, text='Cantidad de Subintervalos:').grid(row=3, column=1, padx=15)
    n_subinterv = tk.Entry(top, width=20)
    n_subinterv.grid(row=3, column=2, padx=15, pady=15)

    tk.Button(top, text='Generar Gráfico y Hoja de Cálculo Python',
              command=lambda: generar_grafico_y_xls(1, n_generar.get(), n_subinterv.get())
              ).grid(row=4, column=1, columnspan=2, pady=10)
    tk.Button(top, text='Generar Gráfico y Hoja de Cálculo Método Congrual Mixto',
              command=lambda: generar_grafico_y_xls(2, n_generar.get(), n_subinterv.get())
              ).grid(row=5, column=1, columnspan=2, pady=(0, 10))


# def open_c():
#     top = tk.Toplevel()
#     top.geometry('840x620')
#     top.title('Prueba de Frecuencia Números PseudoAleatorios Método Congruales Mixto')
#     tk.Button(top, text='Cerrar Ventana', command=top.destroy).grid(row=0, column=9)


def popup(message):
    # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    messagebox.showinfo('Title', message)


lbl = tk.Label(root, text='Hello World!')
lbl2 = tk.Label(root, text='Gasti')

# btn = tk.Button(root, text='Números Pseudos aleatorios', padx=20, command=open_a).pack(pady=3)
# btn2 = tk.Button(root, text='Prueba en Frecuencia Python', padx=20, command=open_b).pack(pady=3)
# btn3 = tk.Button(root, text='Prueba Frecuencia Congruales Mixto', padx=20, command=open_c).pack(pady=3)

btn = tk.Button(root, text='Generador Números Pseudos Aleatorios', padx=20, command=open_a).pack(pady=3)
btn2 = tk.Button(root, text='Prueba en Frecuencia Números Pseudos Aleatorios', padx=20, command=open_b).pack(pady=3)


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
