import cv2 as cv
import numpy as np

def apply_b_w_filter(img_path=None, use_camera=False):
    window_name = "Ajuste de Preto e Branco"

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

    blend_factor = [0.0]

    def update_black_and_white(scale):
        blend_factor[0] = scale / 100.0

    cv.namedWindow(window_name)
    cv.createTrackbar("Preto e Branco", window_name, 0, 100, update_black_and_white)

    while True:
        if use_camera:
            ret, frame = capture.read()
            if not ret:
                print("Falha ao capturar frame da câmera.")
                break

        gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray_img = cv.cvtColor(gray_img, cv.COLOR_GRAY2BGR) 
        img_adjusted = cv.addWeighted(frame, 1 - blend_factor[0], gray_img, blend_factor[0], 0)

        cv.imshow(window_name, img_adjusted)

        key = cv.waitKey(1) & 0xFF
        if key == ord('s'):  
            save_path = input("Digite como salvar a imagem, nao esqueca o tipo no final (ex: foto.png): ").strip()
            cv.imwrite(save_path, img_adjusted)
            print(f"Imagem salva em {save_path}")
        elif key == ord('q'):  
            break

    if use_camera:
        capture.release()
    cv.destroyAllWindows()