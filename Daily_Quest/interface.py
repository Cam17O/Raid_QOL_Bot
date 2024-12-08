import tkinter as tk
from threading import Thread
import BuyItemMarket

def start_bot():
    print("Bot démarré...")
    print("\nDébut achat item au marche\n")
    thread = Thread(target=BuyItemMarket.run)  # Appelle la fonction run() dans BuyItemMarket.py
    thread.daemon = True  # Le thread se termine si l'application principale se ferme
    thread.start()
    print("\nachat item au marche fini\n")

def stop_bot():
    print("Bot arrêté.")

def start_interface():    
    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("Raid Shadow Legends Bot")
    
    # Définir une taille fixe pour la fenêtre
    width = 800
    height = 800
    root.geometry(f"{width}x{height}")
    root.resizable(False, False)


    # Ajout des boutons Démarrer et Arrêter côte à côte
    start_button = tk.Button(
        root,
        text="Démarrer",
        command=start_bot,
        width=15,
        height=2,
        bg="green",
        fg="white"
    )

    stop_button = tk.Button(
        root,
        text="Arrêter",
        command=stop_bot,
        width=15,
        height=2,
        bg="red",
        fg="white"
    )


    # Placement des boutons
    start_button.place(x=10, y=10)
    stop_button.place(x=150, y=10)

    # Lancer la boucle principale
    root.mainloop()
