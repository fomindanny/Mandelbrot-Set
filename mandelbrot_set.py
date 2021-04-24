import numpy as np
import matplotlib.pyplot as plt


def iterations_until_diverge(complex_number: complex, threshold: int) -> int:
    """Returns an amount of iterations until function diverges.
    Function is z(n + 1) = z ^ 2 + c.
    Function diverges when |z| > 4.
    """
    z = complex(0, 0)
    for iteration in range(threshold):
        z = z ** 2 + complex_number
        if abs(z) > 4:
            break

    return iteration


def mandelbrot_set(threshold: int, density: int):
    """Mandelbrot Set realisation.
    Saves an image to the program directory.
    """
    real_axis = np.linspace(-2, 1, density)
    imaginary_axis = np.linspace(-1.5, 1.5, density)
    matrix = np.empty((density, density))

    for row in range(density):
        for col in range(density):
            complex_number = complex(real_axis[row], imaginary_axis[col])
            matrix[row, col] = iterations_until_diverge(complex_number, threshold)

    file_name = "mandelbrot_set.png"
    plt.imsave(file_name, matrix)
