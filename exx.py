import tkinter as tk
import requests

class MeteoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Météo App")

        self.label_ville = tk.Label(root, text="Ville:")
        self.label_ville.pack()

        self.entry_ville = tk.Entry(root)
        self.entry_ville.pack()

        self.button_obtenir_meteo = tk.Button(root, text="Obtenir Météo", command=self.obtenir_meteo)
        self.button_obtenir_meteo.pack()

        self.resultats_frame = tk.Frame(root)
        self.resultats_frame.pack()

    def obtenir_meteo(self):
        ville = self.entry_ville.get()

        # Remplacez "YOUR_API_KEY" par votre clé API OpenWeatherMap
        api_key = "8f22b840c4bfbd4902cb0e8637241236"
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&units=metric"

        try:
            response = requests.get(api_url)
            data = response.json()

            if response.status_code == 200:
                temperature = data["main"]["temp"]
                humidite = data["main"]["humidity"]
                pression = data["main"]["pressure"]
                vitesse_vent = data["wind"]["speed"]
                description = data["weather"][0]["description"]

                resultat_texte = f"Température : {temperature} °C\nHumidité : {humidite}%\nPression : {pression} hPa\nVitesse du vent : {vitesse_vent} m/s\nDescription : {description}"
                label_resultat = tk.Label(self.resultats_frame, text=resultat_texte)
                label_resultat.pack()

            else:
                tk.messagebox.showerror("Erreur", f"Erreur lors de la requête : {data['message']}")

        except Exception as e:
            tk.messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MeteoApp(root)
    root.mainloop()
