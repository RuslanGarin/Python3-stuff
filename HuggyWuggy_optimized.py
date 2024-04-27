import matplotlib.pyplot as plt
import numpy as np

def create_circle(radius, center_x, center_y):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta) + center_x
    y = radius * np.sin(theta) + center_y
    return x, y

def create_half_circle(radius, center_y):
    half_circle_x = np.linspace(-radius, radius, 100)
    half_circle_y = -np.sqrt(radius ** 2 - half_circle_x ** 2) + center_y
    return half_circle_x, half_circle_y

fig, ax = plt.subplots()

# Huggy's head
t = np.linspace(0, 2 * np.pi, 100)
x_head = 16 * np.sin(t) * 1
y_head = 15 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
ax.fill(x_head, y_head, color='blue')
ax.plot(x_head, y_head, color='black')

# Eyes and pupils
eye_radius = 2.5
pupil_radius = 2
eye_centers = [(-6, 0), (6, 0)]
for center_x, center_y in eye_centers:
    eye_x, eye_y = create_circle(eye_radius, center_x, center_y)
    pupil_x, pupil_y = create_circle(pupil_radius, center_x, center_y)
    ax.fill(eye_x, eye_y, color='white')
    ax.plot(eye_x, eye_y, color='black')
    ax.fill(pupil_x, pupil_y, color='black')

# Smile (half-circles)
smile_centers = [-5, -4, -5]
smile_radii = [10, 9, 9.5]
colors = ['red', 'blue', 'black']
for center_y, radius, color in zip(smile_centers, smile_radii, colors):
    if color == 'black':
        ax.plot(*create_half_circle(radius, center_y), color=color)
    else:
        ax.fill(*create_half_circle(radius, center_y), color=color)

ax.set_aspect('equal')
plt.show()