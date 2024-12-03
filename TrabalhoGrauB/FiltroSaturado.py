import cv2 as cv
import numpy as np

def atualizar_saturacao(escala, img_hsv):
    escala_saturacao = escala / 100.0
    H, S, V = cv.split(img_hsv)
    S = np.clip(S * escala_saturacao, 0, 255).astype(np.uint8)
    return cv.cvtColor(cv.merge([H, S, V]), cv.COLOR_HSV2BGR)

def apply_saturation_filter(img_path=None, use_camera=False):
    window_name = "Ajuste de Saturação"

    if use_camera:
        capture = cv.VideoCapture(0)
        if not capture.isOpened():
            raise RuntimeError("Não foi possível acessar a câmera.")
    else:
        if img_path is None:
            raise ValueError("Nenhuma imagem foi fornecida.")
        img = cv.imread(img_path)
        if img is None:
            raise ValueError("Imagem inválida ou caminho incorreto.")
        img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    cv.namedWindow(window_name)
    cv.createTrackbar("Saturação", window_name, 100, 200, lambda x: None)

    while True:
        if use_camera:
            ret, frame = capture.read()
            if not ret:
                print("Falha ao capturar frame da câmera.")
                break
            img_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        escala = cv.getTrackbarPos("Saturação", window_name)
        imagem_ajustada = atualizar_saturacao(escala, img_hsv)  
        cv.imshow(window_name, imagem_ajustada)

        key = cv.waitKey(1) & 0xFF
        if key == ord('s'):  
            save_path = input("Digite como salvar a imagem, nao esqueca o tipo no final (ex: foto.png):").strip()
            cv.imwrite(save_path, imagem_ajustada)  
            print(f"Imagem salva em {save_path}")
        elif key == ord('q'):  
            break

    if use_camera:
        capture.release()
    cv.destroyAllWindows()