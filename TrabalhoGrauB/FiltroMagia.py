import numpy as np
import cv2 as cv

def apply_magic_filter(frame):

    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    hsv_frame[..., 0] = (hsv_frame[..., 0] + 100) % 180  #matiz
    hsv_frame[..., 1] = np.minimum(hsv_frame[..., 1] * 1.5, 255)  #saturacao

    frame = cv.cvtColor(hsv_frame, cv.COLOR_HSV2BGR)

    blurred_frame = cv.GaussianBlur(frame, (21, 21), 0)
    frame_with_aura = cv.addWeighted(frame, 0.6, blurred_frame, 0.4, 0)

    return frame_with_aura

def aplicar_filtro_genio(use_camera=False, img_path=None):
    if use_camera:
        capture = cv.VideoCapture(0)
        if not capture.isOpened():
            print('Unable to open camera.')
            return
    else:
        if img_path is None:
            print("No image provided.")
            return
        img = cv.imread(img_path)
        if img is None:
            print("Invalid image path.")
            return

    while True:
        if use_camera:
            ret, frame = capture.read()
            if not ret:
                print("Failed to grab frame.")
                break
        else:
            frame = img  

        magic_frame = apply_magic_filter(frame)


        cv.imshow('Magic Filter', magic_frame)

        if cv.waitKey(1) & 0xFF == ord('s'):
            save_path = input("Digite como salvar a imagem, nao esqueca o tipo no final (ex: foto.png): ").strip()
            cv.imwrite(save_path, magic_frame)
            print(f"Imagem salva em {save_path}")
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    if use_camera:
        capture.release()
    cv.destroyAllWindows()