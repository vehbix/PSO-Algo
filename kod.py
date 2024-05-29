import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

# Hedef fonksiyon (örnek olarak x^2 + 5)
def target_function(x):
    # Coefficients for x, x^2, x^3, x^4 terms and a constant term
    a = float(coeff_x.get())
    b = float(coeff_x2.get())
    c = float(coeff_x3.get())
    d = float(coeff_x4.get())
    constant = float(constant_term.get())

    return a * x + b * x**2 + c * x**3 + d * x**4 + constant
# PSO Algoritması
class Particle:
    def __init__(self):
        self.position = random.uniform(-10, 10)
        self.pbest_position = self.position
        self.pbest_value = target_function(self.position)
        self.velocity = random.uniform(-1, 1)

def update_velocity(particle, w, c1, c2, gbest_position):
    new_velocity = (w * particle.velocity) + (c1 * random.random()) * (particle.pbest_position - particle.position) + (c2 * random.random()) * (gbest_position - particle.position)
    return new_velocity

def update_position(particle):
    new_position = particle.position + particle.velocity
    return new_position

def run_pso():
    try:
        # Get user inputs
        num_particles = int(num_particles_entry.get())
        num_iterations = int(num_iterations_entry.get())
        max_tekrar = int(max_tekrar_entry.get())
        c1 = float(c1_entry.get())
        c2 = float(c2_entry.get())
        w = float(w_entry.get())
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayısal değerler girin.")
        return

    particles = [Particle() for _ in range(num_particles)]
    gbest_value = float('inf')
    gbest_position = None

    prev_best_values = []

    iterations_listbox.delete(0, tk.END)  # Clear previous iterations

    for i in range(num_iterations):
        for particle in particles:
            fitness_candidate = target_function(particle.position)

            if fitness_candidate < particle.pbest_value:
                particle.pbest_value = fitness_candidate
                particle.pbest_position = particle.position

            if fitness_candidate < gbest_value:
                gbest_value = fitness_candidate
                gbest_position = particle.position

        for particle in particles:
            particle.velocity = update_velocity(particle, w, c1, c2, gbest_position)
            particle.position = update_position(particle)

        # result_label.config(text=f"Iterasyon: {i}, En iyi değer: {gbest_value} at position {gbest_position}")

        prev_best_values.append(gbest_value)

        if len(prev_best_values) > max_tekrar and all(value == prev_best_values[-1] for value in prev_best_values[-max_tekrar:]):
            break

        iterations_listbox.insert(tk.END, f"Iterasyon {i}: En iyi değer {gbest_value} at position {gbest_position}")
        iterations_listbox.yview(tk.END)  # Scroll to the bottom

    # result_label.config(text=f"Son iterasyon tamamlandı. En iyi değer: {gbest_value} at position {gbest_position}")
    messagebox.showinfo("PSO Tamamlandı", "PSO Algoritması başarıyla tamamlandı.")

# Tkinter UI
root = tk.Tk()
root.title("PSO Algoritması Parametre Girişi")

coeff_x_label = ttk.Label(root, text="Katsayı (x):")
coeff_x_label.grid(row=0, column=0, pady=5, padx=10, sticky='E')
coeff_x = ttk.Entry(root, width=10)
coeff_x.insert(0, "1.0")  # Set initial value
coeff_x.grid(row=0, column=1, pady=5, padx=10, sticky='W')

coeff_x2_label = ttk.Label(root, text="Katsayı (x^2):")
coeff_x2_label.grid(row=1, column=0, pady=5, padx=10, sticky='E')
coeff_x2 = ttk.Entry(root, width=10)
coeff_x2.insert(0, "0.0")  # Set initial value
coeff_x2.grid(row=1, column=1, pady=5, padx=10, sticky='W')

coeff_x3_label = ttk.Label(root, text="Katsayı (x^3):")
coeff_x3_label.grid(row=2, column=0, pady=5, padx=10, sticky='E')
coeff_x3 = ttk.Entry(root, width=10)
coeff_x3.insert(0, "0.0")  # Set initial value
coeff_x3.grid(row=2, column=1, pady=5, padx=10, sticky='W')

coeff_x4_label = ttk.Label(root, text="Katsayı (x^4):")
coeff_x4_label.grid(row=3, column=0, pady=5, padx=10, sticky='E')
coeff_x4 = ttk.Entry(root, width=10)
coeff_x4.insert(0, "0.0")  # Set initial value
coeff_x4.grid(row=3, column=1, pady=5, padx=10, sticky='W')

constant_term_label = ttk.Label(root, text="Sabit Değer:")
constant_term_label.grid(row=4, column=0, pady=5, padx=10, sticky='E')
constant_term = ttk.Entry(root, width=10)
constant_term.insert(0, "0.0")  # Set initial value
constant_term.grid(row=4, column=1, pady=5, padx=10, sticky='W')

# Labels and Entry Widgets
num_particles_label = ttk.Label(root, text="Parçacık Sayısı:")
num_particles_label.grid(row=5, column=0, pady=5, padx=10, sticky='E')
num_particles_entry = ttk.Entry(root, width=10)
num_particles_entry.insert(0, "30")  # Set initial value
num_particles_entry.grid(row=5, column=1, pady=5, padx=10, sticky='W')

num_iterations_label = ttk.Label(root, text="İterasyon Sayısı:")
num_iterations_label.grid(row=6, column=0, pady=5, padx=10, sticky='E')
num_iterations_entry = ttk.Entry(root, width=10)
num_iterations_entry.insert(0, "1000")  # Set initial value
num_iterations_entry.grid(row=6, column=1, pady=5, padx=10, sticky='W')

max_tekrar_label = ttk.Label(root, text="Max Tekrar Sayısı:")
max_tekrar_label.grid(row=7, column=0, pady=5, padx=10, sticky='E')
max_tekrar_entry = ttk.Entry(root, width=10)
max_tekrar_entry.insert(0, "50")  # Set initial value
max_tekrar_entry.grid(row=7, column=1, pady=5, padx=10, sticky='W')

c1_label = ttk.Label(root, text="c1 Değeri:")
c1_label.grid(row=8, column=0, pady=5, padx=10, sticky='E')
c1_entry = ttk.Entry(root, width=10)
c1_entry.insert(0, "2.0")  # Set initial value
c1_entry.grid(row=8, column=1, pady=5, padx=10, sticky='W')

c2_label = ttk.Label(root, text="c2 Değeri:")
c2_label.grid(row=9, column=0, pady=5, padx=10, sticky='E')
c2_entry = ttk.Entry(root, width=10)
c2_entry.insert(0, "2.0")  # Set initial value
c2_entry.grid(row=9, column=1, pady=5, padx=10, sticky='W')

w_label = ttk.Label(root, text="w Değeri:")
w_label.grid(row=10, column=0, pady=5, padx=10, sticky='E')
w_entry = ttk.Entry(root, width=10)
w_entry.insert(0, "0.7")  # Set initial value
w_entry.grid(row=10, column=1, pady=5, padx=10, sticky='W')

# Button
run_button = ttk.Button(root, text="PSO Çalıştır", command=run_pso)
run_button.grid(row=11, column=0, columnspan=2, pady=10)

# Iterations Listbox
iterations_listbox = tk.Listbox(root, width=75, height=10)
iterations_listbox.grid(row=12, column=0, columnspan=2, pady=10)

# Result Label
# result_label = ttk.Label(root, text="", font=('Helvetica', 12))
# result_label.grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()
