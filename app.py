import gradio as gr
import numpy as np
import pickle

with open("solar_flare_rf.pkl", "rb") as f:
    rf = pickle.load(f)

with open("solar_flare_scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("solar_flare_encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

def predict_flare(
    active_region,
    linked_events,
    duration,
    rise_time,
    month,
    hour
):
    sample = np.array([[
        active_region,
        linked_events,
        duration,
        rise_time,
        month,
        hour
    ]])

    sample_scaled = scaler.transform(sample)

    pred = rf.predict(sample_scaled)

    return encoder.inverse_transform(pred)[0]

app = gr.Interface(
    fn=predict_flare,
    inputs=[
        gr.Number(label="Active Region"),
        gr.Number(label="Linked Events"),
        gr.Number(label="Duration"),
        gr.Number(label="Rise Time"),
        gr.Number(label="Month"),
        gr.Number(label="Hour")
    ],
    outputs="text",
    title="NASA Solar Flare Predictor"
)

app.launch()