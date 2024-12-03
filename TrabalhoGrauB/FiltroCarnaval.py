import numpy as np
import cv2 as cv
import random

def aplicar_filtro_carnaval(img_path=None, use_camera=False):
    def adicionar_confetes(frame):
        num_confetes = 50
        for _ in range(num_confetes):
            x = random.randint(0, frame.shape[1])
            y = random.randint(0, frame.shape[0])
            radius = random.randint(2, 5)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            cv.circle(frame, (x, y), radius, color, -1)
        return frame

    def process_frame(frame):
        return adicionar_confetes(frame)

    if use_camera:
        capture = cv.VideoCapture(0)
        if not capture.isOpened():
            print('Falha ao abrir câmera')
            return
    else:
        if img_path is None:
            print("É necessário o caminho da imagem.")
            return
        img = cv.imread(img_path)
        if img is None:
            print("Imagem inválida.")
            return

    while True:
        if use_camera:
            ret, frame = capture.read()
            if not ret:
                print("Erro ao captar frame.")
                break
            frame_com_confetes = process_frame(frame)
        else:
            frame_com_confetes = process_frame(img.copy())

        cv.imshow('Confetes', frame_com_confetes)

        if cv.waitKey(1) & 0xFF == ord('s'):
            save_path = input("Digite como salvar a imagem, não esqueça o tipo no final (ex: foto.png):").strip()
            cv.imwrite(save_path, frame_com_confetes)
            print(f"Imagem salva em {save_path}")

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    if use_camera:
        capture.release()

    cv.destroyAllWindows()