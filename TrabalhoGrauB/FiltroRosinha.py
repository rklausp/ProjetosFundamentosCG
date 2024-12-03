import cv2 as cv
import numpy as np

def apply_pinkness(frame, blend_factor):
    pink_layer = np.full_like(frame, [255, 128, 255]) 
    return cv.addWeighted(frame, 1 - blend_factor, pink_layer, blend_factor, 0)

def apply_pink_filter(img_path=None, use_camera=False):
    window_name = "Efeito Rosa"

    if use_camera:
        capture = cv.VideoCapture(0)
        if not capture.isOpened():
            raise RuntimeError("Não foi possível acessar a câmera.")
    else:
        if img_path is None:
            raise ValueError("Nenhuma imagem foi fornecida.")
        frame = cv.imread(img_path)
        if frame is None:
            raise ValueError("Imagem inválida ou caminho incorreto.")

    pinkness_factor = [0.0]

    def update_pinkness(scale):
        pinkness_factor[0] = scale / 100.0

    cv.namedWindow(window_name)
    cv.createTrackbar("Pinkness", window_name, 0, 100, update_pinkness)

    while True:
        if use_camera:
            ret, frame = capture.read()
            if not ret:
                print("Falha ao capturar frame da câmera.")
                break

        pink_frame = apply_pinkness(frame, pinkness_factor[0])
        cv.imshow(window_name, pink_frame)

        key = cv.waitKey(1) & 0xFF
        if key == ord('s'): 
            save_path = input("Caminho para salvar a imagem (ex.: 'pink_effect.jpg'): ").strip()
            cv.imwrite(save_path, pink_frame)
            print(f"Imagem salva em {save_path}")
        elif key == ord('q'): 
            break

    if use_camera:
        capture.release()
    cv.destroyAllWindows()