import numpy as np


def get_circumference(center, radius):
    theta = np.linspace(0, 2 * np.pi, 100)
    return [center[0] + radius * np.cos(theta), center[1] + radius * np.sin(theta)]


def generate_vector(base, direction, scale=1):
    first_point = [base[0] - direction[0], base[1] - direction[1]]
    final_point = [base[0] + direction[0], base[1] + direction[1]]

    line_x = np.empty(2)
    line_y = np.empty(2)

    line_x[0] = scale * first_point[0]
    line_x[1] = scale * final_point[0]

    line_y[0] = scale * first_point[1]
    line_y[1] = scale * final_point[1]

    return [line_x, line_y]


def generate_main_draw(base, angles, plt):
    circumference = get_circumference([0, 0], 1)
    plt.plot(circumference[0], circumference[1])
    for i in range(4):
        values = generate_vector([0, 0], [np.cos(angles[i]), np.sin(angles[i])], 1 / (i + 2))
        plt.plot(values[0], values[1], linestyle='-')
    plt.gca().set_aspect('equal', adjustable='box')
    return plt
