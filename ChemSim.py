import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def create_atom_model(element, atomic_number):
    """
    Creates a simple 3D model of an atom with a nucleus and electron shells.

    Parameters:
        element (str): Symbol of the element.
        atomic_number (int): Atomic number of the element.
    """
    fig = plt.figure(figsize=(16, 8))

    # Subplot 1: Atomic model
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.set_title(f"Atomic Model of {element} (Z = {atomic_number})", fontsize=14)

    # Nucleus representation (a sphere at the center)
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 0.1 * np.outer(np.cos(u), np.sin(v))
    y = 0.1 * np.outer(np.sin(u), np.sin(v))
    z = 0.1 * np.outer(np.ones(np.size(u)), np.cos(v))
    ax1.plot_surface(x, y, z, color='red', alpha=0.6, edgecolor='black', label='Nucleus')

    # Electron shells representation
    for i in range(1, (atomic_number // 2) + 2):
        phi = np.linspace(0, 2 * np.pi, 100)
        theta = np.linspace(0, np.pi, 100)
        x_shell = i * 0.3 * np.outer(np.sin(theta), np.cos(phi))
        y_shell = i * 0.3 * np.outer(np.sin(theta), np.sin(phi))
        z_shell = i * 0.3 * np.outer(np.cos(theta), np.ones_like(phi))
        ax1.plot_wireframe(x_shell, y_shell, z_shell, color='blue', alpha=0.5, linewidth=0.3)

    # Set plot limits
    ax1.set_xlim([-2, 2])
    ax1.set_ylim([-2, 2])
    ax1.set_zlim([-2, 2])

    # Plot labels
    ax1.set_xlabel("X-axis")
    ax1.set_ylabel("Y-axis")
    ax1.set_zlabel("Z-axis")

    # Subplot 2: Particle theory representation
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.set_title(f"Particle Theory of {element} (Z = {atomic_number})", fontsize=14)

    # Protons and neutrons in the nucleus
    num_protons = atomic_number
    num_neutrons = atomic_number  # Simplified assumption for stability
    num_particles = num_protons + num_neutrons

    nucleus_x = np.random.normal(0, 0.1, num_particles)
    nucleus_y = np.random.normal(0, 0.1, num_particles)
    nucleus_z = np.random.normal(0, 0.1, num_particles)

    ax2.scatter(nucleus_x[:num_protons], nucleus_y[:num_protons], nucleus_z[:num_protons], color='red', label='Protons')
    ax2.scatter(nucleus_x[num_protons:], nucleus_y[num_protons:], nucleus_z[num_protons:], color='gray', label='Neutrons')

    # Electrons
    electron_positions = []
    for i in range(1, (atomic_number // 2) + 2):
        num_electrons_in_shell = min(2 * i**2, atomic_number - len(electron_positions))
        phi = np.random.uniform(0, 2 * np.pi, num_electrons_in_shell)
        theta = np.random.uniform(0, np.pi, num_electrons_in_shell)
        r = i * 0.3

        x_electrons = r * np.sin(theta) * np.cos(phi)
        y_electrons = r * np.sin(theta) * np.sin(phi)
        z_electrons = r * np.cos(theta)

        ax2.scatter(x_electrons, y_electrons, z_electrons, color='blue', label='Electrons' if i == 1 else "")
        electron_positions.extend(zip(x_electrons, y_electrons, z_electrons))

    # Set plot limits
    ax2.set_xlim([-2, 2])
    ax2.set_ylim([-2, 2])
    ax2.set_zlim([-2, 2])

    # Plot labels
    ax2.set_xlabel("X-axis")
    ax2.set_ylabel("Y-axis")
    ax2.set_zlabel("Z-axis")

    # Add legend
    ax2.legend()

    plt.show()

def get_element_info():
    """Prompts the user to select an element and returns its symbol and atomic number."""
    periodic_table = {
        "H": 1, "He": 2, "Li": 3, "Be": 4, "B": 5, "C": 6, "N": 7, "O": 8, "F": 9, "Ne": 10,
        "Na": 11, "Mg": 12, "Al": 13, "Si": 14, "P": 15, "S": 16, "Cl": 17, "Ar": 18, "K": 19, "Ca": 20
        # Add more elements as needed.
    }

    print("Available elements:")
    print(", ".join(periodic_table.keys()))
    element = input("Enter the symbol of the element: ").capitalize()

    if element in periodic_table:
        return element, periodic_table[element]
    else:
        print("Element not found in the periodic table. Please try again.")
        return get_element_info()

if __name__ == "__main__":
    element, atomic_number = get_element_info()
    create_atom_model(element, atomic_number)
