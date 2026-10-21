
# import numpy as np
# import matplotlib.pyplot as plt

# # 1. Simulation Parameters
# L = 1.0          # Total length of the domain
# N = 100          # Number of spatial grid points
# dx = L / (N - 1) # Space step size
# D = 0.01         # Diffusion coefficient

# # Time-stepping parameters (ensuring stability: r <= 0.5)
# r = 0.4          # Stability parameter (D * dt / dx^2)
# dt = r * (dx**2) / D
# total_time = 0.5
# Nt = int(total_time / dt)

# # 2. Grid and Initial Conditions
# x = np.linspace(0, L, N)
# u = np.zeros(N)

# # Initial condition: A sharp concentration spike right in the middle
# u[int(N * 0.4):int(N * 0.6)] = 1.0

# # 3. Time-Stepping Loop (Finite Difference)
# # We save snapshots at specific intervals to visualize the progress
# plot_intervals = [0, int(Nt * 0.1), int(Nt * 0.3), int(Nt * 1.0)]
# snapshot_data = {}

# for n in range(Nt + 1):
#     if n in plot_intervals:
#         snapshot_data[n] = u.copy()
        
#     # Compute the next time step using vectorization
#     # u[1:-1] represents all interior points
#     u_new = u.copy()
#     u_new[1:-1] = u[1:-1] + r * (u[2:] - 2 * u[1:-1] + u[:-2])
    
#     # Boundary conditions: Fixed at 0 (Dirichlet) implicitly handled 
#     # since the ends remain at 0.
#     u = u_new

# # 4. Visualization
# plt.figure(figsize=(8, 5))
# for n, profile in snapshot_data.items():
#     time_val = n * dt
#     plt.plot(x, profile, label=f"t = {time_val:.3f} s")

# plt.title("1D Diffusion Simulation (FTCS Scheme)")
# plt.xlabel("Position ($x$)")
# plt.ylabel("Concentration ($u$)")
# plt.legend()
# plt.grid(True, linestyle="--", alpha=0.6)
# plt.show()