# # import numpy as np
# # import matplotlib.pyplot as plt
# # from scipy.integrate import solve_ivp

# # # ODE
# # def two_compart_model(t, y, k12, k21, k10):
# #     bcp, t = y
# #     dX1_dt = -(k12 + k10) * bcp + k21 * t
# #     dX2_dt = k12 * bcp - k21 * t
# #     return [dX1_dt, dX2_dt]

# # Bevacizumab (B)	
# # Carboplatin (C)	
# # Paclitaxel (P)

# import numpy as np
# from scipy.integrate import solve_ivp
# import matplotlib.pyplot as plt

# # take the mean of these values that will be k12
# # def bevacizumab(w):
# #     return 15 * w
# # def carboplatin(gfr):
# #     auc = 6
# #     return auc * (gfr + 25)
# # def paclitaxel(h, w):
# #     one = (h * w) / 3600
# #     bsa = one ** 1/2
#     # return bsa

# # THEESE VALUES ARE AFTER ROUNDING OFF
# # w = 88
# # bevacizumab = 15 * w
# bevacizumab = 1300
# # gfr = 88
# # auc = 6
# # carboplatin = auc * (gfr + 25)
# carboplatin = 650
# # h = 177
# # one = (h * w) / 3600
# # bsa = one ** 1/2
# # paclitaxel = bsa * 200
# paclitaxel = 430
# # k12 is considered the mean of all 3
# k12 = (bevacizumab + carboplatin + paclitaxel) / 3

# # now for k21 10% of mean
# k21 = k12 * 0.1

# # now for k10 take the mean elimination time of the 3
# k10 = (20 + 4 + (1/2)) / 3

# # ODE





# # Plotting
# fig, axes = plt.subplots(1, 3, figsize=(18, 5))
# axes[1].plot(solve.t, solve.y[0], label='Central ($X_1$)', color='blue', lw=2)
# axes[1].plot(solve.t, solve.y[1], label='Peripheral ($X_2$)', color='orange', lw=2)
# axes[1].set_title('2-Compartment Model')
# axes[1].set_xlabel('BCP')
# axes[1].set_ylabel('Size')
# axes[1].legend()
# axes[1].grid(True, linestyle='--', alpha=0.6)
# plt.tight_layout()
# plt.show()
# SOME CHANGES ARE REQD IN THE PLOTS BUT IT IS OK NOW AS WITH THE INC IN CONC OF "BCP" THE "SIZE" OF THE TUMOR DECREASES




import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# 1. Define Drug Properties & Automatically Compute Rates
bevacizumab = 1300
carboplatin = 650
paclitaxel = 430

# Rate Constants derived from means
k12_calc = (bevacizumab + carboplatin + paclitaxel) / 3
k21_calc = k12_calc * 0.1
k10_calc = (20 + 4 + (1/2)) / 3

# 2. System of Differential Equations (Fixed the `k21 * t` typo to `k21 * x2`)
def two_compartment_model(t, y, k12, k21, k10):
    x1, x2 = y
    dX1_dt = -(k12 + k10) * x1 + k21 * x2
    dX2_dt = k12 * x1 - k21 * x2
    return [dX1_dt, dX2_dt]

# 3. Solver Setup
t_span = (0, 24)
t_eval = np.linspace(0, 24, 500)
initial_conc = [793.0, 0.0]
parameters = (k12_calc, k21_calc, k10_calc)

# Solving the system
solve = solve_ivp(two_compartment_model, t_span, initial_conc, args=parameters, t_eval=t_eval)

# 4. Improved Visualization Function
def plot_pharmacokinetics(solve_data):
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Custom styling
    ax.plot(solve_data.t, solve_data.y[0], label='Central Compartment (\(X_1\))', color='#1f77b4', lw=2.5)
    ax.plot(solve_data.t, solve_data.y[1], label='Peripheral Compartment (\(X_2\))', color='#ff7f0e', lw=2.5)
    
    # Enhanced Metadata labels
    ax.set_title('2-Compartment Pharmacokinetic Model (BCP Regimen)', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Time (Hours)', fontsize=12)
    ax.set_ylabel('Drug Amount / Concentration', fontsize=12)
    
    ax.legend(frameon=True, facecolor='white', edgecolor='none', fontsize=11)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    return fig

# Display locally if running standalone
if __name__ == "__main__":
    fig = plot_pharmacokinetics(solve)
    plt.show()
