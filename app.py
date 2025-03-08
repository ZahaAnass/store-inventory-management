from tkinter import *
from view import GestionInventaire
import database

# Initialisation de la base de données
database.create_table()

# Start the app
if __name__ == "__main__":
    window = Tk()
    my_app = GestionInventaire(window)
    window.mainloop()
