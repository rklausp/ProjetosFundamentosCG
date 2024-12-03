import numpy as np
import cv2 as cv
from common import clock, draw_str

def aplica_olho(background, foreground, pos_x=None, pos_y=None):
    olho = cv.cvtColor(foreground, cv.COLOR_RGBA2BGR)
    b, g, r, a = cv.split(foreground)
    
    f_rows, f_cols, _ = foreground.shape
    b_rows, b_cols, _ = background.shape

    if pos_x is None:
        pos_x = b_cols // 2
    if pos_y is None:
        pos_y = b_rows // 2

    x_start = pos_x - f_cols // 2
    y_start = pos_y - f_rows // 2

    bg_x_start = max(0, x_start)
    bg_y_start = max(0, y_start)
    bg_x_end = min(b_cols, x_start + f_cols)
    bg_y_end = min(b_rows, y_start + f_rows)

    fg_x_start = max(0, -x_start)
    fg_y_start = max(0, -y_start)
    fg_x_end = fg_x_start + (bg_x_end - bg_x_start)
    fg_y_end = fg_y_start + (bg_y_end - bg_y_start)

    olho = olho[fg_y_start:fg_y_end, fg_x_start:fg_x_end]
    mask = a[fg_y_start:fg_y_end, fg_x_start:fg_x_end]
    mask_inv = cv.bitwise_not(mask)
    roi = background[bg_y_start:bg_y_end, bg_x_start:bg_x_end]

    img_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
    img_fg = cv.bitwise_and(olho, olho, mask=mask)
    res = cv.add(img_bg, img_fg)

    background[bg_y_start:bg_y_end, bg_x_start:bg_x_end] = res

    return background

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv.rectangle(img, (x1, y1), (x2, y2), color, 2)

def aplicar_olhos():
    face_classifier = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
    eye_classifier = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")   

    foreground = cv.imread('Stickers/singleeye.png', cv.IMREAD_UNCHANGED)

    create_capture = cv.VideoCapture(0)

    while True:
        _ret, img = create_capture.read()
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray = cv.equalizeHist(gray)

        t = clock()
        rects = detect(gray, face_classifier)  
        vis = img.copy()

        if not eye_classifier.empty():
            for x1, y1, x2, y2 in rects:
                roi = gray[y1:y2, x1:x2]  # parte rosto
                vis_roi = vis[y1:y2, x1:x2]
                subrects = detect(roi.copy(), eye_classifier)  # olhos
                
                for ex1, ey1, ex2, ey2 in subrects:
                    eye_center_x = x1 + (ex1 + ex2) // 2
                    eye_center_y = y1 + (ey1 + ey2) // 2
                    
                    eye_width = ex2 - ex1
                    resized_olho = cv.resize(foreground, (eye_width, eye_width), interpolation=cv.INTER_AREA)
                    
                    vis = aplica_olho(vis, resized_olho, eye_center_x, eye_center_y)

        cv.imshow('facedetect', vis)

        key = cv.waitKey(1) & 0xFF
        if key == ord('s'):  
            save_path = input("Digite como salvar a imagem, nao esqueca o tipo no final (ex: foto.png): ").strip()
            cv.imwrite(save_path, vis)
            print(f"Imagem salva em {save_path}")
        elif key == ord('q'):  
            break
        
    cv.destroyAllWindows()
    create_capture.release()