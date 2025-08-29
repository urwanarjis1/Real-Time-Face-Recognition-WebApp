
import os
import sys
import numpy as np
import cv2
import json
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout


# Parent path add
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

def load_data():
    images, labels = [], []
    label_map = {}
    current_label = 0

    for person in os.listdir(config.DATASET_DIR):
        person_path = os.path.join(config.DATASET_DIR, person)
        if not os.path.isdir(person_path):
            continue

        label_map[person] = current_label
        for img_name in os.listdir(person_path):
            img_path = os.path.join(person_path, img_name)
            img = cv2.imread(img_path)
            if img is None:
                continue
            img = cv2.resize(img, (config.IMG_SIZE, config.IMG_SIZE))
            img = img.astype("float32") / 255.0
            images.append(img)
            labels.append(current_label)

        current_label += 1

    X = np.array(images)
    y = to_categorical(labels, num_classes=len(label_map))

    # Save label map
    with open(config.LABELS_PATH, "w") as f:
        json.dump(label_map, f)

    return X, y, label_map

def build_transfer_model(num_classes):
    base_model = MobileNetV2(weights="imagenet", include_top=False, input_shape=(config.IMG_SIZE, config.IMG_SIZE, 3))
    base_model.trainable = False  # Freeze base model- we dont train pre trained layers

    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dropout(0.3)(x)
    x = Dense(128, activation="relu")(x)
    x = Dropout(0.3)(x)
    predictions = Dense(num_classes, activation="softmax")(x)

    model = Model(inputs=base_model.input, outputs=predictions)
    model.compile(optimizer=tf.keras.optimizers.Adam(1e-4),
                  loss="categorical_crossentropy",
                  metrics=["accuracy"])
    return model

def train():
    X, y, label_map = load_data()
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=config.VAL_SPLIT, stratify=y)

    model = build_transfer_model(num_classes=len(label_map))

    callbacks = [
        EarlyStopping(monitor="val_loss", patience=config.EARLY_STOP_PATIENCE, restore_best_weights=True), #if val_loss isnt improving, then we stop training
        ModelCheckpoint(config.MODEL_PATH, save_best_only=True) # saves best model (prevent overfitting)
    ]

    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=config.EPOCHS,
        batch_size=config.BATCH_SIZE,
        callbacks=callbacks
    )

    model.save(config.MODEL_PATH)
    print("✅ Transfer Learning Model trained and saved at", config.MODEL_PATH)

if __name__ == "__main__":
    train()

