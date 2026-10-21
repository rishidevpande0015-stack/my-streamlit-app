import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# --- 1-Compartment Model ODE ---
def one_compartment_model(t, y, k10):
    X1, = y
    dX1_dt = -k10 * X1
    return [dX1_dt]

# --- 2-Compartment Model ODEs ---
def two_compartment_model(t, y, k12, k21, k10):
    X1, X2 = y
    dX1_dt = -(k12 + k10) * X1 + k21 * X2
    dX2_dt = k12 * X1 - k21 * X2
    return [dX1_dt, dX2_dt]

# --- 3-Compartment Model ODEs ---
def three_compartment_model(t, y, k12, k21, k13, k31, k10):
    X1, X2, X3 = y
    dX1_dt = -(k12 + k13 + k10) * X1 + k21 * X2 + k31 * X3
    dX2_dt = k12 * X1 - k21 * X2
    dX3_dt = k13 * X1 - k31 * X3
    return [dX1_dt, dX2_dt, dX3_dt]

# Simulation time settings (e.g., 24 hours)
t_span = (0, 24)
t_eval = np.linspace(0, 24, 500)

# Initial conditions: 100 mg administered directly into the central compartment
y0_1c = [100.0]
y0_2c = [100.0, 0.0]
y0_3c = [100.0, 0.0, 0.0]

# Rate constants (1/hour)
params_1c = (0.1,)
params_2c = (0.5, 0.2, 0.1)            # (k12, k21, k10)
params_3c = (0.6, 0.3, 0.2, 0.1, 0.1)  # (k12, k21, k13, k31, k10)

# Solve the differential equations
sol_1c = solve_ivp(one_compartment_model, t_span, y0_1c, args=params_1c, t_eval=t_eval)
sol_2c = solve_ivp(two_compartment_model, t_span, y0_2c, args=params_2c, t_eval=t_eval)
sol_3c = solve_ivp(three_compartment_model, t_span, y0_3c, args=params_3c, t_eval=t_eval)

# --- Plotting the Results ---
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 1-Compartment Plot
axes[0].plot(sol_1c.t, sol_1c.y[0], label='Central ($X_1$)', color='blue', lw=2)
axes[0].set_title('1-Compartment Model')
axes[0].set_xlabel('Time (hours)')
axes[0].set_ylabel('Amount (mg)')
axes[0].legend()
axes[0].grid(True, linestyle='--', alpha=0.6)

# 2-Compartment Plot
axes[1].plot(sol_2c.t, sol_2c.y[0], label='Central ($X_1$)', color='blue', lw=2)
axes[1].plot(sol_2c.t, sol_2c.y[1], label='Peripheral ($X_2$)', color='orange', lw=2)
axes[1].set_title('2-Compartment Model')
axes[1].set_xlabel('Time (hours)')
axes[1].set_ylabel('Amount (mg)')
axes[1].legend()
axes[1].grid(True, linestyle='--', alpha=0.6)

# 3-Compartment Plot
axes[2].plot(sol_3c.t, sol_3c.y[0], label='Central ($X_1$)', color='blue', lw=2)
axes[2].plot(sol_3c.t, sol_3c.y[1], label='Peripheral 1 ($X_2$)', color='orange', lw=2)
axes[2].plot(sol_3c.t, sol_3c.y[2], label='Peripheral 2 ($X_3$)', color='green', lw=2)
axes[2].set_title('3-Compartment Model')
axes[2].set_xlabel('Time (hours)')
axes[2].set_ylabel('Amount (mg)')
axes[2].legend()
axes[2].grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
