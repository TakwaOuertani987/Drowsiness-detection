📂Drowsiness-detection.py # Script principal du projet


/best.pt # Modèle YOLOv8 entraîné pour détecter la somnolence


/istockphoto-2193889646-640_adpp_is.mp4 # Vidéo d’entrée (exemple)


/ALRMBuzr_Buzzer 5 (ID 1587)_LS.wav # Fichier audio de l’alarme



##⚙️ Installation et Configuration

 ###1️⃣ Installer les dépendances nécessaires

Avant d’exécuter le script, installe les bibliothèques Python suivantes :

```bash
pip install ultralytics opencv-python pygame
###2️⃣ Vérifier les chemins des fichiers

Dans le code, assure-toi que les chemins vers :

la vidéo (video_path)

le modèle YOLO (model_path)

le son d’alarme (alarm_path)

sont bien corrects et correspondent à ton environnement local.

Exemple :

video_path = r"C:\Users\USER\Desktop\detection de somnolence\video.mp4"
model_path = r"C:\Users\USER\Desktop\detection de somnolence\best.pt"
alarm_path = r"C:\Users\USER\Desktop\detection de somnolence\alarm.wav"
Exécution du Programme

Pour exécuter le projet :

python détection_de_somnolence.py
Le programme ouvrira la vidéo et affichera les détections YOLOv8 en temps réel.
Si une détection de somnolence ("drawsy") est observée pendant plus de 2 secondes, une alarme sonore se déclenche automatiquement.Fonctionnement du Code

Chargement du modèle YOLOv8
Le modèle pré-entraîné (best.pt) est chargé pour détecter la classe “drawsy”.

Lecture de la vidéo
Le programme lit la vidéo image par image avec OpenCV.

Détection de la somnolence
YOLOv8 analyse chaque image pour déterminer si un état de somnolence est présent.

Temporisation et déclenchement de l’alarme

Si la somnolence est détectée pendant au moins 2 secondes, une alarme est jouée via Pygame.

Si la somnolence disparaît, l’alarme est arrêtée.

Affichage en temps réel
La vidéo est affichée avec les annotations YOLOv8 pour visualiser les détections.

Sortie du programme
Appuie sur la touche ‘q’ pour fermer la fenêtre vidéo et arrêter le programme.
