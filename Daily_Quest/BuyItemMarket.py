import pyautogui
import cv2
import numpy as np
import os
import time

# Fonction pour cliquer à une position spécifique
def click(x, y):
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.click()

# Fonction pour vérifier si une image est visible à l'écran
def find_image(image_path, confidence=0.8):
    # Capture de l'écran et conversion en format compatible OpenCV
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Charger l'image modèle
    template = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if template is None:
        raise FileNotFoundError(f"Image modèle introuvable : {image_path}")

    # Appliquer cv2.matchTemplate
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # Vérifier si la correspondance dépasse le seuil
    if max_val >= confidence:
        # Retourne les coordonnées du centre de l'image trouvée
        h, w = template.shape[:2]
        return (max_loc[0] + w // 2, max_loc[1] + h // 2)
    return None

# Fonction principale
def run():
    # Configuration des chemins
    base_dir = "Daily_Quest\images"
    eclat_vert_image = os.path.join(base_dir, "EclatVertPrixMarche.png")
    buy_item_image = os.path.join(base_dir, "BuyItemMarket.png")

    print("Ouverture du marché...")
    # Clique sur 650, 700 : ouverture du marché
    click(650, 700)
    time.sleep(2)

    # Cherche l'image de l'éclat vert
    try:
        image_location = find_image(eclat_vert_image)
    except FileNotFoundError as e:
        print(e)
        return
    
    # Si l'image est trouvée, clique sur l'image puis achète
    if image_location:
        print(f"Image éclat vert trouvée à : {image_location}")
        click(*image_location)
        time.sleep(1)

        # Cherche l'image pour acheter
        try:
            image_location = find_image(buy_item_image)
        except FileNotFoundError as e:
            print(e)
            return

        if image_location:
            print(f"Achat en cours à : {image_location}")
            click(*image_location)
            
    # Sinon, clique sur 600, 200 puis cherche à acheter
    else:
        print("Eclat vert non trouvé, clic de secours...")
        click(600, 200)
        time.sleep(1)

        # Cherche l'image pour acheter
        try:
            image_location = find_image(buy_item_image)
        except FileNotFoundError as e:
            print(e)
            return

        if image_location:
            print(f"Achat en cours à : {image_location}")
            click(*image_location)
            
            

    # Clique sur 1850, 50 : Quitter le marché
    print("Fermeture du marché...")
    click(1850, 50)
