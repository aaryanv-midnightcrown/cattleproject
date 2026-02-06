import torch
import matplotlib.pyplot as plt
import numpy as np
from model import CattleCNN

def run_inference(patches, model_path, grid_shape):
    device = "cuda" if torch.cuda.is_available() else "cpu"

    model = CattleCNN().to(device)
    model.load_state_dict(torch.load(model_path))
    model.eval()

    with torch.no_grad():
        preds = model(patches.to(device)).cpu().numpy()

    heatmap = preds.reshape(grid_shape)

    plt.figure(figsize=(8,6))
    plt.imshow(heatmap, cmap="YlOrBr")
    plt.colorbar(label="Cattle Probability")
    plt.title("Predicted Cattle Presence")
    plt.show()
