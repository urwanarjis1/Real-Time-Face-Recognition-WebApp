# config.py
"""
Central project configuration.
This file provides many alias names so the other scripts (that expect
slightly different variable names) work without editing.
"""

import os
from pathlib import Path
import cv2

# ---------- Base dirs ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Dataset (where data_collection will save per-person folders)
DATASET_DIR = os.path.join(BASE_DIR, "dataset")
DATASET_PATH = DATASET_DIR   # alias

# Models / saved artifacts
SAVED_MODELS_DIR = os.path.join(BASE_DIR, "saved_models")
MODEL_DIR = SAVED_MODELS_DIR    # alias for scripts that use MODEL_DIR
MODELS_DIR = SAVED_MODELS_DIR   # another alias

# Primary model & label paths (used by training / recognition scripts)
MODEL_PATH = os.path.join(SAVED_MODELS_DIR, "face_recognition_mobilenet.h5")
# Some scripts use labels.json, some labels.pkl — we include both aliases
LABELS_PATH = os.path.join(SAVED_MODELS_DIR, "labels.json")
LABELS_PKL_PATH = os.path.join(SAVED_MODELS_DIR, "labels.pkl")

# Ensure directories exist
os.makedirs(DATASET_DIR, exist_ok=True)
os.makedirs(SAVED_MODELS_DIR, exist_ok=True)

# ---------- Image settings ----------
# Use a single integer IMG_SIZE in most scripts; we also provide tuple aliases.
IMG_SIZE = 224 #96             # scalar (width=height)
IMG_WIDTH = IMG_SIZE
IMG_HEIGHT = IMG_SIZE
IMG_SHAPE = (IMG_SIZE, IMG_SIZE)    # alias expected by some code
IMG_SIZE_TUPLE = IMG_SHAPE

# Channels: set 3 for color (RGB) or 1 for grayscale pipelines
CHANNELS = 3

# ---------- Haar Cascade ----------
# Prefer project haarcascade/ file if present, otherwise fall back to OpenCV built-in.
_HAAR_LOCAL = os.path.join(BASE_DIR, "haarcascade", "haarcascade_frontalface_default.xml")
if os.path.exists(_HAAR_LOCAL):
    HAAR_PATH = _HAAR_LOCAL
else:
    # fallback to OpenCV default data path
    HAAR_PATH = os.path.join(cv2.data.haarcascades, "haarcascade_frontalface_default.xml")

# also provide older/alternate name
HAAR_CASCADE_PATH = HAAR_PATH

# ---------- Face detection / prediction ----------
# Minimum face window size passed to detectMultiScale
MIN_FACE_SIZE = (80, 80)   # (width, height)

# Confidence threshold to label a prediction as known vs "Unknown" (softmax prob)
PRED_THRESH = 0.80

# ---------- Training hyperparams ----------
BATCH_SIZE = 16
EPOCHS = 20
VAL_SPLIT = 0.2
AUGMENT = True
EARLY_STOP_PATIENCE = 5
SEED = 42

# ---------- Misc / notes ----------
# Use these helper aliases if any script expects different names:
# - DATASET_PATH  <-> DATASET_DIR
# - MODEL_DIR / MODELS_DIR  <-> SAVED_MODELS_DIR
# - LABELS_PATH (json) and LABELS_PKL_PATH (pickle)
#
# If you want grayscale pipeline, set CHANNELS = 1 and adjust preprocessing in scripts.
