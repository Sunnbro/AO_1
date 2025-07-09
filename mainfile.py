import os
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

# Lire les données Google stock
file_path = "C:/Users/Yanis.Belharrat/Downloads/archive/Google_stock_data.csv"
df = pd.read_csv(file_path)

# Convertir 'Date' en datetime
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])
else:
    raise ValueError("La colonne 'Date' est introuvable.")

# Paramètres
WINDOW_SIZE = 30
PREDICT_HORIZON = 30
IMG_SAVE_PATH = "stock_images"
LABELS_CSV_PATH = "stock_labels.csv"

# Créer le dossier s'il n'existe pas
os.makedirs(IMG_SAVE_PATH, exist_ok=True)

# Trier les données
df = df.sort_values("Date").reset_index(drop=True)

# Si le CSV existe déjà, inutile de tout refaire
if os.path.exists(LABELS_CSV_PATH):
    print(f"✅ {LABELS_CSV_PATH} déjà présent, PNG déjà générés.")
else:
    print("📊 Génération des labels et du fichier CSV...")
    X_paths = []
    y_labels = []

    for i in tqdm(range(len(df) - WINDOW_SIZE - PREDICT_HORIZON)):
        window_df = df.iloc[i:i+WINDOW_SIZE]
        future_df = df.iloc[i+WINDOW_SIZE:i+WINDOW_SIZE+PREDICT_HORIZON]
        
        current_price = window_df['Close'].iloc[-1]
        future_price = future_df['Close'].iloc[-1]
        
        label = int(future_price > current_price)

        img_name = f"window_{i}_label_{label}.png"
        img_path = os.path.join(IMG_SAVE_PATH, img_name)

        # Vérifier si l’image existe déjà
        if not os.path.exists(img_path):
            # (Ce bloc ne s'exécutera pas si les PNG sont déjà là)
            plt.figure(figsize=(3, 3))
            plt.plot(window_df['Close'].values, color='blue')
            plt.axis('off')
            plt.tight_layout()
            plt.savefig(img_path, bbox_inches='tight', pad_inches=0)
            plt.close()

        X_paths.append(img_path)
        y_labels.append(label)

    # Sauvegarde des labels
    label_df = pd.DataFrame({
        "path": X_paths,
        "label": y_labels
    })
    label_df.to_csv(LABELS_CSV_PATH, index=False)
    print(f"✅ Labels sauvegardés dans {LABELS_CSV_PATH}")
print("📊 Génération terminée.")