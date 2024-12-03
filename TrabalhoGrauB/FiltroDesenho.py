import numpy as np
import cv2 as cv

def aplicar_filtro_desenho(img_path=None, use_camera=False):
    def apply_edge_detection(frame):
        frame_canny = cv.Canny(frame, 50, 100)
        
        inverted_canny = cv.bitwise_not(frame_canny)
        
        return inverted_canny

    if use_camera:
        capture = cv.VideoCapture(0)
        if not capture.isOpened():
            print('Falha ao abrir camera')
            return
    else:
        if img_path is None:
            print("É necessário caminho da imagem.")
            return
        img = cv.imread(img_path)
        if img is None:
            print("Imagem inválida.")
            return

    while True:
        if use_camera:
            ret, frame = capture.read()
            if not ret:
                print("Erro ao captar frame")
                break
        else:
            frame = img  

        inverted_frame = apply_edge_detection(frame)
        
        cv.imshow('Edge Detection', inverted_frame)
        
        if cv.waitKey(1) & 0xFF == ord('s'):
            save_path = input("Digite como salvar a imagem, nao esqueca o tipo no final (ex: foto.png): ").strip()
            cv.imwrite(save_path, inverted_frame)
            print(f"Imagem salva em {save_path}")

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    if use_camera:
        capture.release()


    cv.destroyAllWindows()