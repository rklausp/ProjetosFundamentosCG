import cv2 as cv
import numpy as np

def aplicar_orelhas(fundo, orelhinhas, x, y, largura):
    escala = largura / orelhinhas.shape[1]
    orelinhas_mudanca_tamanho = cv.resize(orelhinhas, None, fx=escala, fy=escala, interpolation=cv.INTER_AREA)
    h, w, _ = orelinhas_mudanca_tamanho.shape

    orelhinhas_rgb = orelinhas_mudanca_tamanho[:, :, :3]
    alpha = orelinhas_mudanca_tamanho[:, :, 3]

    x_end = min(x + w, fundo.shape[1])
    y_end = min(y + h, fundo.shape[0])
    w = x_end - x
    h = y_end - y

    if x < 0 or y < 0 or w <= 0 or h <= 0:
        return fundo

    roi = fundo[y:y + h, x:x + w]
    mask = cv.resize(alpha[:h, :w], (w, h), interpolation=cv.INTER_AREA)
    mask_inv = cv.bitwise_not(mask)

    fundo_roi = cv.bitwise_and(roi, roi, mask=mask_inv)
    orelhinhas_fg = cv.bitwise_and(orelhinhas_rgb[:h, :w], orelhinhas_rgb[:h, :w], mask=mask)
    combined = cv.add(fundo_roi, orelhinhas_fg)

    fundo[y:y + h, x:x + w] = combined

    return fundo

def aplicar_orelha_gatinho():
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
    cat_ears = cv.imread("Stickers/catears.png", cv.IMREAD_UNCHANGED)
    if cat_ears is None:
        print("Erro: imagem de orelha de gato nao encontrada")
        return

    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Erro: Sem acesso a webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro: Nao foi possivel ler webecam.")
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

        for (x, y, w, h) in faces:
            ear_largura = int(w * 1.5)
            ear_x = x - (ear_largura - w) // 2
            ear_y = y - int(h * 0.6)
            frame = aplicar_orelhas(frame, cat_ears, ear_x, ear_y, ear_largura)

        cv.imshow("Detector de orelha de gatinho", frame)

        key = cv.waitKey(5) & 0xFF
        if key == ord('s'):
            save_path = input("Digite como salvar a imagem, nao esqueca o tipo no final (ex: foto.png): ").strip()
            cv.imwrite(save_path, frame)
            print(f"Imagem salva em {save_path}")
        elif key == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()