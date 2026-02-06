import rasterio
import numpy as np
import os

PATCH_SIZE = 32

def load_band(path):
    with rasterio.open(path) as src:
        return src.read(1).astype(np.float32)

def compute_indices(red, nir, green):
    ndvi = (nir - red) / (nir + red + 1e-6)
    ndwi = (green - nir) / (green + nir + 1e-6)
    return ndvi, ndwi

def load_features(data_dir):
    red = load_band(os.path.join(data_dir, "B04.tif"))
    nir = load_band(os.path.join(data_dir, "B08.tif"))
    green = load_band(os.path.join(data_dir, "B03.tif"))

    ndvi, ndwi = compute_indices(red, nir, green)
    return np.stack([red, nir, green, ndvi, ndwi], axis=0)

def extract_patches(arr):
    patches = []
    h, w = arr.shape[1:]

    for i in range(0, h - PATCH_SIZE, PATCH_SIZE):
        for j in range(0, w - PATCH_SIZE, PATCH_SIZE):
            patch = arr[:, i:i+PATCH_SIZE, j:j+PATCH_SIZE]
            patches.append(patch)

    return np.array(patches)
