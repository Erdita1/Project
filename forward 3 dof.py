import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def forward_kinematics():
    try:
        # Mendapatkan panjang link dari input pengguna
        L1 = float(entry_L1.get())
        L2 = float(entry_L2.get())
        L3 = float(entry_L3.get())

        # Mendapatkan sudut joint dari input pengguna dalam derajat
        theta1 = np.radians(float(entry_theta1.get()))
        theta2 = np.radians(float(entry_theta2.get()))
        theta3 = np.radians(float(entry_theta3.get()))

        # Menghitung koordinat X dan Y menggunakan forward kinematik
        x = L1 * np.cos(theta1) + L2 * np.cos(theta1 + theta2) + L3 * np.cos(theta1 + theta2 + theta3)
        y = L1 * np.sin(theta1) + L2 * np.sin(theta1 + theta2) + L3 * np.sin(theta1 + theta2 + theta3)

        # Menampilkan koordinat X dan Y
        result_label.config(text=f"X: {x:.2f}, Y: {y:.2f}")

        # Menggambar lengan manipulator
        ax.clear()
        ax.plot([0, L1 * np.cos(theta1), L1 * np.cos(theta1) + L2 * np.cos(theta1 + theta2), x],
                [0, L1 * np.sin(theta1), L1 * np.sin(theta1) + L2 * np.sin(theta1 + theta2), y], 'bo-')
        ax.set_xlim(-L1 - L2 - L3, L1 + L2 + L3)
        ax.set_ylim(-L1 - L2 - L3, L1 + L2 + L3)
        canvas.draw()
    except ValueError:
        result_label.config(text="Masukkan tidak valid. Pastikan semua input adalah angka.")

# Membuat jendela GUI
root = tk.Tk()
root.title("Simulasi Forward Kinematik Manipulator 3-Link")

# Membuat label dan input untuk panjang link
label_L1 = ttk.Label(root, text="Panjang Link 1:")
label_L1.grid(row=0, column=0)
entry_L1 = ttk.Entry(root)
entry_L1.grid(row=0, column=1)

label_L2 = ttk.Label(root, text="Panjang Link 2:")
label_L2.grid(row=1, column=0)
entry_L2 = ttk.Entry(root)
entry_L2.grid(row=1, column=1)

label_L3 = ttk.Label(root, text="Panjang Link 3:")
label_L3.grid(row=2, column=0)
entry_L3 = ttk.Entry(root)
entry_L3.grid(row=2, column=1)

# Membuat label dan input untuk sudut joint
label_theta1 = ttk.Label(root, text="Sudut Joint θ1 (derajat):")
label_theta1.grid(row=3, column=0)
entry_theta1 = ttk.Entry(root)
entry_theta1.grid(row=3, column=1)

label_theta2 = ttk.Label(root, text="Sudut Joint θ2 (derajat):")
label_theta2.grid(row=4, column=0)
entry_theta2 = ttk.Entry(root)
entry_theta2.grid(row=4, column=1)

label_theta3 = ttk.Label(root, text="Sudut Joint θ3 (derajat):")
label_theta3.grid(row=5, column=0)
entry_theta3 = ttk.Entry(root)
entry_theta3.grid(row=5, column=1)

# Tombol untuk menghitung hasil
calculate_button = ttk.Button(root, text="Hitung", command=forward_kinematics)
calculate_button.grid(row=6, columnspan=2)

# Label untuk menampilkan hasil
result_label = ttk.Label(root, text="")
result_label.grid(row=7, columnspan=2)

# Membuat plot untuk menggambar lengan manipulator
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=2, rowspan=8)

# Menjalankan aplikasi GUI
root.mainloop()