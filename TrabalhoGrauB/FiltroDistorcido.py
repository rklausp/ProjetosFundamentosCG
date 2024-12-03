import numpy as np
import cv2 as cv

def aplicar_filtro_distorcido(img_path=None, use_camera=False):
    def apply_distortion(frame, distortion_scale=0.001):
        h, w = frame.shape[:2]
        map_x, map_y = np.meshgrid(np.arange(w), np.arange(h))
        map_x = map_x.astype(np.float32)
        map_y = map_y.astype(np.float32)

        map_x += distortion_scale * w * np.sin(2 * np.pi * map_y / 180)
        map_y += distortion_scale * h * np.sin(2 * np.pi * map_x / 180)

        distorted_frame = cv.remap(frame, map_x, map_y, interpolation=cv.INTER_LINEAR)
        return distorted_frame

    if use_camera:
        capture = cv.VideoCapture(0)
        if not capture.isOpened():
            print('Unable to open camera')
            return
    else:
        if img_path is None:
            print("Image path is required")
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

        distorted_frame = apply_distortion(frame, distortion_scale=0.02)
        
        cv.imshow('Distorted Frame', distorted_frame)

        if cv.waitKey(1) & 0xFF == ord('s'):
            save_path = input("Digite como salvar a imagem, nao esqueca o tipo no final (ex: foto.png): ").strip()
            cv.imwrite(save_path, distorted_frame)
            print(f"Imagem salva em {save_path}")
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    if use_camera:
        capture.release()

    cv.destroyAllWindows()