# import streamlit as st
# import numpy as np
# from scipy.integrate import solve_ivp
# import matplotlib.pyplot as plt

# st.set_page_config(page_title="PK Model Dashboard", layout="wide")

# st.title("🧪 Pharmacokinetic 2-Compartment Model")
# st.write("Simulate drug distribution dynamics between central and peripheral compartments.")

# # Sidebar Configuration for Interactivity
# st.sidebar.header("Model Parameters")

# # Initial concentration control
# init_x1 = st.sidebar.number_input("Initial Central Conc. (X1)", min_value=0.0, value=793.0, step=10.0)

# # Allow users to tweak the baseline parameters dynamically
# k12 = st.sidebar.slider("Transfer Rate k12 (Central -> Peripheral)", 100.0, 1000.0, 793.33)
# k21 = st.sidebar.slider("Transfer Rate k21 (Peripheral -> Central)", 10.0, 200.0, 79.33)
# k10 = st.sidebar.slider("Elimination Rate k10", 1.0, 50.0, 8.16)

# # Differential Equation Solver Logic
# def two_compartment_model(t, y, k12, k21, k10):
#     x1, x2 = y
#     dX1_dt = -(k12 + k10) * x1 + k21 * x2
#     dX2_dt = k12 * x1 - k21 * x2
#     return [dX1_dt, dX2_dt]

# t_span = (0, 24)
# t_eval = np.linspace(0, 24, 500)
# initial_conc = [init_x1, 0.0]
# parameters = (k12, k21, k10)

# solve = solve_ivp(two_compartment_model, t_span, initial_conc, args=parameters, t_eval=t_eval)

# # Layout: Split page into Metrics and the Matplotlib chart
# col1, col2 = st.columns([1, 3])

# with col1:
#     st.metric(label="Peak Central Concentration", value=f"{np.max(solve.y[0]):.2f}")
#     st.metric(label="Peak Peripheral Concentration", value=f"{np.max(solve.y[1]):.2f}")

# with col2:
#     # Build and clean up plot
#     fig, ax = plt.subplots(figsize=(10, 4.5))
#     ax.plot(solve.t, solve.y[0], label='Central ($X_1$)', color='#1f77b4', lw=2.5)
#     ax.plot(solve.t, solve.y[1], label='Peripheral ($X_2$)', color='#ff7f0e', lw=2.5)
    
#     ax.set_title('Concentration Curves Over Time', fontsize=12, fontweight='bold')
#     ax.set_xlabel('Time (Hours)')
#     ax.set_ylabel('Concentration')
#     ax.legend()
#     ax.grid(True, linestyle='--', alpha=0.5)
    
#     # Pipe the matplotlib figure directly to Streamlit
#     st.pyplot(fig)



import streamlit as st
import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp, simpson

# Set page structure to wide layout
st.set_page_config(page_title="Advanced PK Engine", layout="wide", page_icon="🧬")

st.title("🧬 Advanced PK Simulation & Patient Analysis Dashboard")
st.write("Compute dynamic Drug Exposure metrics, map clearance timelines, and validate theoretical curves against clinical telemetry.")

# ----------------------------------------------------
# SIDEBAR CONTROL CONTROLS
# ----------------------------------------------------
st.sidebar.header("🕹️ Simulation Settings")

# 1. Timeline Extension Slider
max_hours = st.sidebar.slider("Simulation Window (Hours)", min_value=12, max_value=168, value=48, step=12)

st.sidebar.markdown("---")
st.sidebar.header("💊 Pharmacokinetic Rates")
init_x1 = st.sidebar.number_input("Initial Central Loading Dose (X1)", min_value=0.0, value=793.0, step=50.0)

# Theoretical parameter configurations
k12 = st.sidebar.slider("Transfer Rate k12 (Central -> Peripheral)", 100.0, 1000.0, 793.33)
k21 = st.sidebar.slider("Transfer Rate k21 (Peripheral -> Central)", 10.0, 200.0, 79.33)
k10 = st.sidebar.slider("Elimination Rate k10", 0.1, 50.0, 8.16)

# ----------------------------------------------------
# MATHEMATICAL PK SOLVER ENGINE
# ----------------------------------------------------
def two_compartment_model(t, y, k12, k21, k10):
    x1, x2 = y
    dX1_dt = -(k12 + k10) * x1 + k21 * x2
    dX2_dt = k12 * x1 - k21 * x2
    return [dX1_dt, dX2_dt]

# Use user-selected timeline window dynamically
t_span = (0, max_hours)
t_eval = np.linspace(0, max_hours, max_hours * 10)  # 10 data points per hour
initial_conc = [init_x1, 0.0]
parameters = (k12, k21, k10)

solve = solve_ivp(two_compartment_model, t_span, initial_conc, args=parameters, t_eval=t_eval)

# Generate a clean dataframe for the native Streamlit charting engine
sim_df = pd.DataFrame({
    'Time (Hours)': solve.t,
    'Central Compartment (Theoretical)': solve.y[0],
    'Peripheral Compartment (Theoretical)': solve.y[1]
})

# ----------------------------------------------------
# METRIC ENGINEERING & AUC INTEGRATION
# ----------------------------------------------------
# Compute mathematical Area Under Curve using Simpson's Rule approximation
auc_central = simpson(y=solve.y[0], x=solve.t)
auc_peripheral = simpson(y=solve.y[1], x=solve.t)

st.subheader("📊 Primary Pharmacokinetic Vectors")
m_col1, m_col2, m_col3, m_col4 = st.columns(4)

with m_col1:
    st.metric(label="Peak Central Conc. ($C_{max}$)", value=f"{np.max(solve.y[0]):.2f} mg/L")
with m_col2:
    st.metric(label="Peak Peripheral Conc.", value=f"{np.max(solve.y[1]):.2f} mg/L")
with m_col3:
    st.metric(label="AUC (Central Exposure)", value=f"{auc_central:.1f} mg·h/L")
with m_col4:
    st.metric(label="AUC (Peripheral Exposure)", value=f"{auc_peripheral:.1f} mg·h/L")

st.markdown("---")

# ----------------------------------------------------
# PATIENT CLINICAL DATA UPLOADER
# ----------------------------------------------------
st.subheader("📂 Patient Observation Matching")
uploaded_file = st.file_uploader(
    "Upload actual clinical monitoring data (.csv). Expected fields: 'Time' and 'Observed_Conc'", 
    type=["csv"]
)

# Provide fallback sample data generator button to let users preview the feature
if uploaded_file is None:
    if st.button("💡 Load Mock Patient Dataset"):
        # Generate simulated observations matching the current mathematical framework with random noise
        mock_times = np.sort(np.random.choice(t_eval[t_eval <= 24], size=8, replace=False))
        # Fetch theoretical values at those times
        interp_central = np.interp(mock_times, solve.t, solve.y[0])
        # Inject standard variance noise 
        mock_obs = np.maximum(0, interp_central + np.random.normal(0, 45, size=len(mock_times)))
        
        uploaded_file = pd.DataFrame({
            'Time': mock_times,
            'Observed_Conc': mock_obs
        })
        st.info("Loaded synthetic validation profile: Continuous tracking active.")

# Bind dataset if provided or generated
if uploaded_file is not None:
    if isinstance(uploaded_file, pd.DataFrame):
        patient_df = uploaded_file
    else:
        patient_df = pd.read_csv(uploaded_file)
    
    # Clean check to confirm table properties match UI demands
    if 'Time' in patient_df.columns and 'Observed_Conc' in patient_df.columns:
        # Standardize matching index fields to overlay nicely with simulation arrays
        patient_df = patient_df.rename(columns={'Time': 'Time (Hours)'})
        
        # Merge datasets cleanly using a rolling/outer connection framework
        chart_data = pd.merge_ordered(sim_df, patient_df, on='Time (Hours)')
    else:
        st.error("Uploaded format mismatch. Please supply a CSV with exactly 'Time' and 'Observed_Conc' headers.")
        chart_data = sim_df
else:
    chart_data = sim_df

# ----------------------------------------------------
# INTERACTIVE DATA VISUALIZATION
# ----------------------------------------------------
# Pivot names to give a clean multi-line plot legend
chart_data = chart_data.set_index('Time (Hours)')

st.write("### Interactive Curve Overlay")
st.line_chart(
    chart_data[['Central Compartment (Theoretical)', 'Peripheral Compartment (Theoretical)']], 
    height=400,
    use_container_width=True
)

if 'Observed_Conc' in chart_data.columns:
    st.write("### Patient Scatter Plot (Real vs Target)")
    # Filter valid non-null telemetry coordinates
    scatter_pts = chart_data['Observed_Conc'].dropna()
    st.scatter_chart(scatter_pts, height=250, use_container_width=True)
