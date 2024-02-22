import tkinter as tk
import requests

class PrevisionsMeteoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Prévisions Météo")

        self.label_ville = tk.Label(root, text="Ville:")
        self.label_ville.pack()

        self.entry_ville = tk.Entry(root)
        self.entry_ville.pack()

        self.button_obtenir_previsions = tk.Button(root, text="Obtenir Prévisions", command=self.obtenir_previsions)
        self.button_obtenir_previsions.pack()

        self.resultats_frame = tk.Frame(root)
        self.resultats_frame.pack()

    def obtenir_previsions(self):
        ville = self.entry_ville.get()

        # Remplacez "YOUR_API_KEY" par votre clé API OpenWeatherMap
        api_key = "8f22b840c4bfbd4902cb0e8637241236"
        api_url = f"http://api.openweathermap.org/data/2.5/forecast?q={ville}&appid={api_key}&units=metric"

        try:
            response = requests.get(api_url)
            data = response.json()

            if response.status_code == 200:
                previsions = data["list"]

                for prevision in previsions:
                    date_heure = prevision["dt_txt"]
                    temperature = prevision["main"]["temp"]
                    description = prevision["weather"][0]["description"]

                    resultat_texte = f"{date_heure}: Température {temperature}°C, {description}"
                    label_resultat = tk.Label(self.resultats_frame, text=resultat_texte)
                    label_resultat.pack()

            else:
                tk.messagebox.showerror("Erreur", f"Erreur lors de la requête : {data['message']}")

        except Exception as e:
            tk.messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PrevisionsMeteoApp(root)
    root.mainloop()
