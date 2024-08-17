from fer import FER
import cv2

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Crear el detector de emociones
emotion_detector = FER()

while True:
    ret, frame = cap.read()
    
    # Detectar emociones en la imagen
    emotion_results = emotion_detector.detect_emotions(frame)
    
    # Mostrar resultados en la imagen
    for result in emotion_results:
        bounding_box = result['box']
        emotions = result['emotions']
        
        # Dibujar el rectángulo alrededor de la cara
        cv2.rectangle(frame, 
                      (bounding_box[0], bounding_box[1]), 
                      (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]), 
                      (0, 255, 0), 2)
        
        # Mostrar la emoción más probable
        dominant_emotion = max(emotions, key=emotions.get)
        cv2.putText(frame, dominant_emotion, 
                    (bounding_box[0], bounding_box[1] - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    0.9, (36, 255, 12), 2)
    
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
