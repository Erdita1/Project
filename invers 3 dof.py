import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def inverse_kinematics():
    try:
        # Mendapatkan panjang link dari input pengguna
        L1 = float(entry_L1.get())
        L2 = float(entry_L2.get())
        L3 = float(entry_L3.get())

        # Mendapatkan posisi X dan Y yang diinginkan dari input pengguna
        x_target = float(entry_x.get())
        y_target = float(entry_y.get())

        # Menghitung sudut joint menggunakan inverse kinematik
        # Hitung theta3 terlebih dahulu
        D = (x_target*x_target + y_target*y_target - L1*L1 - L2*L2 - L3*L3) / (2 * L2 * L3)
        theta3 = np.arctan2(-np.sqrt(1 - D**2), D)

        # Hitung theta1 dan theta2
        k1 = L1 + L2 * np.cos(theta3)
        k2 = L2 * np.sin(theta3)
        theta1 = np.arctan2(y_target, x_target) - np.arctan2(k2, k1)
        theta2 = np.arctan2(y_target - k2, x_target - k1) - theta1

        # Mengonversi sudut ke derajat
        theta1_deg = np.degrees(theta1)
        theta2_deg = np.degrees(theta2)
        theta3_deg = np.degrees(theta3)

        # Menampilkan sudut joint
        result_label.config(text=f"θ1: {theta1_deg:.2f}°, θ2: {theta2_deg:.2f}°, θ3: {theta3_deg:.2f}°")

        # Menggambar lengan manipulator
        ax.clear()
        ax.plot([0, L1 * np.cos(theta1), L1 * np.cos(theta1) + L2 * np.cos(theta1 + theta2), x_target],
                [0, L1 * np.sin(theta1), L1 * np.sin(theta1) + L2 * np.sin(theta1 + theta2), y_target], 'bo-')
        ax.set_xlim(-L1 - L2 - L3, L1 + L2 + L3)
        ax.set_ylim(-L1 - L2 - L3, L1 + L2 + L3)
        canvas.draw()
    except ValueError:
        result_label.config(text="Masukkan tidak valid. Pastikan semua input adalah angka.")

# Membuat jendela GUI
root = tk.Tk()
root.title("Simulasi Inverse Kinematik Manipulator 3-Link")

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

# Membuat label dan input untuk posisi akhir yang diinginkan
label_x = ttk.Label(root, text="Posisi X:")
label_x.grid(row=3, column=0)
entry_x = ttk.Entry(root)
entry_x.grid(row=3, column=1)

label_y = ttk.Label(root, text="Posisi Y:")
label_y.grid(row=4, column=0)
entry_y = ttk.Entry(root)
entry_y.grid(row=4, column=1)

# Tombol untuk menghitung hasil
calculate_button = ttk.Button(root, text="Hitung", command=inverse_kinematics)
calculate_button.grid(row=5, columnspan=2)

# Label untuk menampilkan hasil
result_label = ttk.Label(root, text="")
result_label.grid(row=6, columnspan=2)

# Membuat plot untuk menggambar lengan manipulator
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=2, rowspan=7)

# Menjalankan aplikasi GUI
root.mainloop()