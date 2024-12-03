import tkinter as tk
from tkinter import filedialog, messagebox
import cv2 as cv
import numpy as np

sticker_positions = []

def overlay_sticker(base_image, sticker, x, y):
    if sticker is None:
        print("Error: Unable to load sticker image.")
        return base_image

    sticker = cv.resize(sticker, (100, 100), interpolation=cv.INTER_AREA)

    sticker_h, sticker_w = sticker.shape[:2]
    
    # Cabe na imagem
    if y + sticker_h > base_image.shape[0] or x + sticker_w > base_image.shape[1]:
        print("Erro: Sticker fora da imagem.")
        return base_image 
    
    sticker_bgr = sticker[:, :, :3]  
    alpha_mask = sticker[:, :, 3]  

    roi = base_image[y:y+sticker_h, x:x+sticker_w]

    for c in range(3):
        roi[:, :, c] = (alpha_mask / 255.0) * sticker_bgr[:, :, c] + \
                       (1 - alpha_mask / 255.0) * roi[:, :, c]

    base_image[y:y+sticker_h, x:x+sticker_w] = roi
    return base_image

def mouse_click(event, x, y, flags, param):
    global sticker_positions  
    if event == cv.EVENT_LBUTTONDOWN:
        sticker_positions.append((x, y))

def choose_and_overlay_sticker():
    global sticker_positions  
    
    stickers = {
        'cat': 'Stickers/catsticker.png',
        'dog': 'Stickers/dogsticker.png',
        'star': 'Stickers/starsticker.png',
        'flower': 'Stickers/flowersticker.png',
        'mushroom': 'Stickers/mushroomsticker.png'
    }

    sticker_choice = tk.simpledialog.askstring(
        "Sticker Options", 
        "Escolha um sticker: cat, dog, star, flower, mushroom"
    )

    if sticker_choice not in stickers:
        print("Escolha de Sticker invalido.")
        return

    sticker_path = stickers[sticker_choice]
    sticker = cv.imread(sticker_path, cv.IMREAD_UNCHANGED)
    if sticker is None:
        print(f"Erro ao carregar Sticker: {sticker_path}")
        return

    use_camera = messagebox.askyesno("Input Option", "Você gostaria de usar a camera?")

    if use_camera:
        capture = cv.VideoCapture(0)
        if not capture.isOpened():
            print('Não foi possível abrir a camera')
            return

        sticker_positions = []

        while True:
            ret, img = capture.read()
            if not ret:
                break

            for (x, y) in sticker_positions:
                img = overlay_sticker(img, sticker, x, y)

            cv.imshow('image', img)
            cv.setMouseCallback('image', mouse_click)

            key = cv.waitKey(1) & 0xFF
            if key == ord('s'): 
                save_path = input("Salvar imagem como: ").strip()
                cv.imwrite(save_path, img)
                print(f"Imagem salva em {save_path}")
            elif key == ord('q'): 
                break

        capture.release()
        cv.destroyAllWindows()

    else:
        img_path = filedialog.askopenfilename(
            title="Selecione a imagem",
            filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*"))
        )
        if not img_path:
            print("Sem seleção de imagem.")
            return

        img = cv.imread(img_path)
        if img is None:
            print(f"Erro ao carregar imagem: {img_path}")
            return

        sticker_positions = []

        while True:
            for (x, y) in sticker_positions:
                img = overlay_sticker(img, sticker, x, y)

            cv.imshow('image', img)
            cv.setMouseCallback('image', mouse_click)

            key = cv.waitKey(1) & 0xFF
            if key == ord('s'): 
                save_path = input("Salvar imagem como: ").strip()
                cv.imwrite(save_path, img)
                print(f"Imagem salva em {save_path}")
            elif key == ord('q'): 
                break

        cv.destroyAllWindows()