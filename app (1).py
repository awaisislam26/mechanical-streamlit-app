import gradio as gr

# ------------------------------
# Pump Power Calculation Function
# ------------------------------
def calculate_pump_power(flow_rate, head, density, efficiency):
    # Input validation
    if efficiency <= 0 or efficiency > 1:
        return "Error: Efficiency must be between 0 and 1.", ""
    if flow_rate < 0 or head < 0 or density <= 0:
        return "Error: Flow rate, head, and density must be positive values.", ""

    g = 9.81  # gravitational acceleration (m/s^2)

    # Hydraulic power (Watts)
    hydraulic_power = density * g * flow_rate * head  # W

    # Brake power (including efficiency)
    brake_power = hydraulic_power / efficiency  # W

    # Convert to kW
    hydraulic_kw = hydraulic_power / 1000
    brake_kw = brake_power / 1000

    return (f"{hydraulic_kw:.3f} kW", f"{brake_kw:.3f} kW")


# ------------------------------
# Gradio Interface
# ------------------------------
with gr.Blocks(title="Pump Power Calculator") as demo:
    gr.Markdown(
        """
        # 💧 Pump Power Calculator
        Calculate **Hydraulic Power** and **Brake Power** of a pump using input parameters.
        
        **Formulas Used:**
        - Hydraulic Power: ρ × 9.81 × Q × H  
        - Brake Power: Hydraulic Power / η  
        
        Enter the values below:
        """
    )

    with gr.Row():
        flow_rate = gr.Number(label="Flow Rate Q (m³/s)", value=0.01)
        head = gr.Number(label="Head H (m)", value=20)

    with gr.Row():
        density = gr.Number(label="Fluid Density ρ (kg/m³)", value=1000)
        efficiency = gr.Number(label="Pump Efficiency η (0–1)", value=0.70)

    calc_button = gr.Button("Calculate Power")

    with gr.Row():
        hydraulic_output = gr.Textbox(label="Hydraulic Power (kW)", interactive=False)
        brake_output = gr.Textbox(label="Brake Power (kW)", interactive=False)

    calc_button.click(
        calculate_pump_power,
        inputs=[flow_rate, head, density, efficiency],
        outputs=[hydraulic_output, brake_output]
    )

# Run the app
demo.launch()
