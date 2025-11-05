import cv2
import time
import pygame
from ultralytics import YOLO

# Configuration des chemins
video_path = r"C:\Users\USER\Desktop\detection de somnolence\istockphoto-2193889646-640_adpp_is.mp4"
model_path = r"C:\Users\USER\Desktop\detection de somnolence\best.pt"
alarm_path = r"C:\Users\USER\Desktop\detection de somnolence\ALRMBuzr_Buzzer 5 (ID 1587)_LS.wav"

# Charger le modèle YOLOv8
model = YOLO(model_path)

# Initialiser Pygame pour l'alarme sonore
pygame.mixer.init()
alarm_sound = pygame.mixer.Sound(alarm_path)

# Ouvrir la vidéo
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Erreur: Impossible d'ouvrir la vidéo.")
    exit()

# Variables pour gérer la détection et l'alarme
detection_active = False
detection_start_time = None
alarm_interval = 2  # Temps en secondes avant de jouer l'alarme
alarm_playing = False  # Flag pour éviter de répéter l'alarme

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Détection avec YOLOv8
    results = model(frame)

    drawsy_detected = False  # Flag pour vérifier si "drawsy" est détecté

    # Vérifier si "drawsy" est détecté
    for result in results:
        names = result.names  # Liste des noms des classes
        boxes = result.boxes  # Boîtes de détection
        
        for box in boxes:
            class_id = int(box.cls[0].item())  # ID de la classe détectée
            label = names[class_id]  # Nom de la classe détectée
            
            if label == "drawsy":
                drawsy_detected = True
                break  # Pas besoin de vérifier d'autres boxes

    # Gestion de l'alarme
    current_time = time.time()
    
    if drawsy_detected:
        if not detection_active:
            detection_active = True
            detection_start_time = current_time
            alarm_playing = False  # Réinitialisation de l'alarme
            print("Détection 'drawsy' détectée, attente confirmation...")

        # Vérifier si la détection dure plus longtemps que l'intervalle avant de jouer l'alarme
        if current_time - detection_start_time >= alarm_interval and not alarm_playing:
            print("Alerte : Détection confirmée de 'drawsy' !")
            alarm_sound.play()
            alarm_playing = True  # Marquer l'alarme comme jouée

    else:
        # Réinitialisation si plus aucune détection
        detection_active = False
        detection_start_time = None
        alarm_playing = False  # Réinitialisation de l'alarme

    # Afficher la vidéo avec les annotations YOLOv8
    annotated_frame = results[0].plot()  # Affichage avec les annotations
    cv2.imshow("Détection de somnolence", annotated_frame)

    # Quitter la boucle si la touche 'q' est pressée
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()