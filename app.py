import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Pump Power Calculator",
    layout="centered"
)

# --------------------------------------------------
# Title & description
# --------------------------------------------------
st.title("🔧 Pump Power Calculator")
st.markdown("### For Mechanical Engineering Students")

st.markdown("""
This web app calculates the **required pump power** based on flow rate,
pump head, and efficiency.
""")

# --------------------------------------------------
# Sidebar inputs
# --------------------------------------------------
st.sidebar.header("Input Parameters")

Q = st.sidebar.number_input(
    "Flow Rate (m³/s)",
    min_value=0.0,
    value=0.05,
    step=0.01
)

H = st.sidebar.number_input(
    "Pump Head (m)",
    min_value=0.0,
    value=20.0,
    step=1.0
)

eta = st.sidebar.slider(
    "Pump Efficiency (η)",
    min_value=0.1,
    max_value=1.0,
    value=0.7
)

# --------------------------------------------------
# Pump power calculation
# --------------------------------------------------
def pump_power(flow_rate, head, efficiency):
    rho = 1000      # kg/m³
    g = 9.81        # m/s²
    power_kw = (rho * g * flow_rate * head) / efficiency / 1000
    return power_kw

# --------------------------------------------------
# Button action
# --------------------------------------------------
if st.sidebar.button("Calculate Pump Power"):
    power = pump_power(Q, H, eta)

    st.success(f"✅ Required Pump Power: **{power:.2f} kW**")

    # --------------------------------------------------
    # Plot: Pump Power vs Flow Rate
    # --------------------------------------------------
    flow_range = np.linspace(0.01, max(Q * 1.5, 0.02), 20)
    power_curve = [
        pump_power(q, H, eta) for q in flow_range
    ]

    fig, ax = plt.subplots()
    ax.plot(flow_range, power_curve)
    ax.set_xlabel("Flow Rate (m³/s)")
    ax.set_ylabel("Pump Power (kW)")
    ax.set_title("Pump Power vs Flow Rate")
    ax.grid(True)

    st.pyplot(fig)

# --------------------------------------------------
# Theory section
# --------------------------------------------------
st.markdown("---")
st.markdown("""
### 📘 Pump Power Formula

\\[
P = \\frac{\\rho g Q H}{\\eta}
\\]

**Where:**
- ρ = 1000 kg/m³ (water density)
- g = 9.81 m/s²
- Q = Flow rate (m³/s)
- H = Pump head (m)
- η = Pump efficiency

### ⚠ Assumptions
- Incompressible fluid (water)
- Steady flow
- Constant efficiency
""")

