import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()

# Huggy's head
t = np.linspace(0, 2*np.pi, 100)
x_head = 16 * np.sin(t)**1
y_head = 15 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Rendering the head here
ax.fill(x_head, y_head, color='blue')
ax.plot(x_head, y_head, color='black')

# Setting up his eyes

theta = np.linspace(0, 2*np.pi, 100)

# Huggy's right eye
r_eye_x = 2.5 * np.cos(theta) - 6
r_eye_y = 2.5 * np.sin(theta)

# Huggy's right pupil
rp_eye_x = 2 * np.cos(theta) - 6
rp_eye_y = 2 * np.sin(theta)

# Reflection in right eye
rr_eye_x = np.cos(theta) - 7
rr_eye_y = np.sin(theta) + 1

# Reflection in left eye
lr_eye_x = np.cos(theta) + 5
lr_eye_y = np.sin(theta) + 1

# Huggy's left eye
l_eye_x = 2.5 * np.cos(theta) + 6
l_eye_y = 2.5 * np.sin(theta)

# Huggy's left pupil
lp_eye_x = 2 * np.cos(theta) + 6
lp_eye_y = 2 * np.sin(theta)

# Rendering the eyes

# Right
ax.fill(r_eye_x, r_eye_y, color='white')
ax.plot(r_eye_x, r_eye_y, color='black')

# Left
ax.fill(l_eye_x, l_eye_y, color='white')
ax.plot(l_eye_x, l_eye_y, color='black')

# Rendering pupils both at once

ax.fill(rp_eye_x, rp_eye_y, color='black')
ax.fill(lp_eye_x, lp_eye_y, color='black')

# Rendering reflections in the eyes

ax.fill(rr_eye_x, rr_eye_y, color='white')
ax.fill(lr_eye_x, lr_eye_y, color ='white')

# Smile, you're being recorded! The smile is consisted of 3 (three) half-circles

radius = 10
low_half_circle_x = np.linspace(-radius, radius, 100)
low_half_circle_y = np.sqrt(radius**2 - low_half_circle_x**2) + 5

radius = 9
high_half_circle_x = np.linspace(-radius, radius, 100)
high_half_circle_y = np.sqrt(radius**2 - high_half_circle_x**2) + 4

radius = 9.5
mid_half_circle_x = np.linspace(-radius, radius, 100)
mid_half_circle_y = np.sqrt(radius**2 - mid_half_circle_x**2) + 5

# Plot the half circles from the smile!
ax.fill(low_half_circle_x, -low_half_circle_y, color='red')
ax.fill(high_half_circle_x, -high_half_circle_y, color='blue')
ax.plot(mid_half_circle_x, -mid_half_circle_y, color='black')

# Remove the axis ticks
#ax.set_xticks([])
#ax.set_yticks([])

# Aspect ratio to be equal
ax.set_aspect('equal')

# Show the plot
plt.show()