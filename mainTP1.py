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

from tabulate import tabulate

ACCURACY = 4

root = tk.Tk()
root.title('SIM 4K1 2020 Trabajo práctico N°1')
root.geometry('450x125')
# root.iconbitmap('favicon.ico')


def generar_otro(actual_method, textarea, random_numbers):
    random_number = actual_method.get_random()
    random_numbers.append([len(random_numbers) + 1, random_number])
    textarea.delete("1.0", "end")
    textarea.insert(tk.END, tabulate(random_numbers, ['Iteración (i)', 'Número aleatorio (RND)'], tablefmt="psql"))
    textarea.see(tk.END)


def generar(method, textarea, btn_otro, xo, k, g, c, a, m, cant_num):
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
    if cant_num == '':
        cant_num = 0

    if method == 1:
        actual_generator = MethodCongrualesMixto(xo, k, g, c, ACCURACY)
    elif method == 2:
        actual_generator = MethodCongrualesMultiplicativo(xo, k, g, ACCURACY)

    # esto por si le queremos imponer algún parámetro
    if a != 0:
        actual_generator.a = int(a)
    if m != 0:
        actual_generator.m = int(m)

    cant_num = int(cant_num)
    random_numbers = []

    for i in range(cant_num):
        random_number = actual_generator.get_random()
        random_numbers.append([i + 1, random_number])

    if btn_otro is not None:
        btn_otro.configure(command=lambda: generar_otro(actual_generator, textarea, random_numbers))

    textarea.insert(tk.END, tabulate(random_numbers, ['Iteración (i)', 'Número aleatorio (RND)'], tablefmt="psql"))

    return random_numbers


def get_random_numbers_congruales_mixto(n, s, x0, k, c, g, textarea):
    if n == '' or s == '':
        popup('Falta cantidad y de subintervalos')
        return

    if k == '':
        popup('Falta parametro k (número entero utilizado para generar constante multiplicativa)')
        return

    if x0 == '':
        popup('Falta parametro x0 (semilla)')
        return

    if g == '':
        popup('Falta parametro g (número entero utilizado para generar el modulo)')
        return

    if c == '':
        popup('Falta parametro c (constante aditiva)')
        return

    n = int(n)
    s = int(s)
    x0 = int(x0)
    k = int(k)
    g = int(g)
    c = int(c)

    xls_name = 'prueba_frecuencia_congruencial_mixto'
    random_numbers = generar(1, textarea, None, x0, k, g, c, '', '', n)

    t = TestChiCuadrado(random_numbers, n, s, ACCURACY)
    t.do_test()

    ToExcel.create_excel(t, xls_name)

    topgraph = tk.Toplevel()
    topgraph.geometry('1024x768')
    topgraph.title('Gráfico')
    show_graph(topgraph, t)

    popup('Finalizado!! Ir a la carpeta exports para observar resultados')


def get_random_numbers_python(n):
    # random.random() es la funcion random de python
    for i in range(n):
        yield i + 1, truncate(random.random(), ACCURACY)


def generar_grafico_y_xls(n, s):
    if n == '' or s == '':
        popup('Falta cantidad y de subintervalos')
        return

    n = int(n)
    s = int(s)

    xls_name = 'prueba_frecuencia_python'
    random_numbers = get_random_numbers_python(n)

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
    top.title('Generador de Números PseudoAleatorios')

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
              command=lambda: generar(r.get(), textarea, btn_otro,
                                      xo.get(), k.get(), g.get(),
                                      c.get(), a.get(), m.get(), 20)
              ).grid(row=2, column=3, padx=5)


def open_b():
    top = tk.Toplevel()
    top.title('Prueba de Frecuencia Números PseudoAleatorios Python')

    tk.Label(top, text='Números a generar:').grid(row=2, column=1)
    n_generar = tk.Entry(top, width=20)
    n_generar.grid(row=2, column=2)

    tk.Label(top, text='Cantidad de Subintervalos:').grid(row=3, column=1, padx=15)
    n_subinterv = tk.Entry(top, width=20)
    n_subinterv.grid(row=3, column=2, padx=15, pady=15)

    tk.Button(top, text='Generar Gráfico y Hoja de Cálculo',
              command=lambda: generar_grafico_y_xls(n_generar.get(), n_subinterv.get())
              ).grid(row=4, column=1, columnspan=2, pady=10)


def open_c():
    top = tk.Toplevel()
    top.title('Prueba de Ji-Cuadrada con Método Congruencial Mixto')

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

    tk.Label(top, text='Números a generar:').grid(row=6, column=1)
    n_generar = tk.Entry(top, width=20)
    n_generar.grid(row=6, column=2)

    tk.Label(top, text='Cantidad de Subintervalos:').grid(row=7, column=1)  # , padx=15
    n_subinterv = tk.Entry(top, width=20)
    n_subinterv.grid(row=7, column=2)  # , padx=15, pady=15

    textarea = tk.Text(top, height=15, width=65)
    # Read only
    textarea.bind('<Key>', lambda e: 'break')
    textarea.grid(row=8, column=1, columnspan=3)

    tk.Button(top, text='Generar Gráfico y Hoja de Cálculo',
              command=lambda: get_random_numbers_congruales_mixto(n_generar.get(), n_subinterv.get(),
                                                                  xo.get(), k.get(), c.get(), g.get(), textarea)
              ).grid(row=6, column=3, padx=5)


def popup(message):
    # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    messagebox.showinfo('Title', message)


lbl = tk.Label(root, text='Hello World!')
lbl2 = tk.Label(root, text='Gasti')

btn = tk.Button(root, text='Generador Números Pseudos Aleatorios', padx=20, command=open_a).pack(pady=3)
btn2 = tk.Button(root, text='Prueba en Frecuencia Números Pseudos Aleatorios', padx=20, command=open_b).pack(pady=3)
btn3 = tk.Button(root, text='Prueba de Ji-Cuadrada con Método Congruencial Mixto', padx=20, command=open_c).pack(pady=3)

root.mainloop()
