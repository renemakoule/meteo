import tkinter as tk
from time import strftime

class Horloge(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Horloge")

        self.label_heure = tk.Label(self, font=('calibri', 40, 'bold'), background='black', foreground='white')
        self.label_heure.pack(anchor='center')

        # Appeler la fonction pour mettre à jour l'heure en temps réel
        self.actualiser_heure()

    def actualiser_heure(self):
        heure_actuelle = strftime('%H:%M:%S %p')  # Format de l'heure
        self.label_heure['text'] = heure_actuelle
        self.after(1000, self.actualiser_heure)  # Actualiser toutes les secondes

if __name__ == "__main__":
    app = Horloge()
    app.mainloop()
