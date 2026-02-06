import torch
import numpy as np
from src.data_loader import load_features, extract_patches
from src.train import train_model
from src.infer import run_inference

DATA_DIR = "data/sentinel"
MODEL_PATH = "model/cattle_cnn.pt"

features = load_features(DATA_DIR)
patches = extract_patches(features)
patches_tensor = torch.tensor(patches, dtype=torch.float32)

# --- Dummy labels (placeholder until SkyFi / GEE labeling)
labels = torch.rand((patches_tensor.shape[0], 1))

# --- TRAIN
train_model(patches_tensor, labels, MODEL_PATH)

# --- INFER
grid_h = int(features.shape[1] / 32) - 1
grid_w = int(features.shape[2] / 32) - 1

run_inference(patches_tensor, MODEL_PATH, (grid_h, grid_w))
