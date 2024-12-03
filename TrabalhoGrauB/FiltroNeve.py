import cv2 as cv
import numpy as np

def aplicar_neve(img_path=None, use_camera=False):
    """Applies a snow effect to an image or video feed."""
    window_name = "Snow Effect"

    def nevar(frame, floco_de_neve, qnt_neve=100):
        h, w, _ = frame.shape
        snow = frame.copy()

        for i in range(qnt_neve):
            x, y, tamanho, intensidade, velocidade = floco_de_neve[i]
            y += velocidade
            if y > h:
                y = 0  #volta topo
            cor_floco_neve = (intensidade, intensidade, intensidade)
            cv.circle(snow, (x, y), tamanho, cor_floco_neve, -1)
            floco_de_neve[i] = (x, y, tamanho, intensidade, velocidade)

        frame_com_neve = cv.addWeighted(frame, 0.9, snow, 0.3, 0)
        return frame_com_neve, floco_de_neve

    def generate_floco_de_neve(qnt_neve, width, height):
        floco_de_neve = []
        for _ in range(qnt_neve):
            x = np.random.randint(0, width)
            y = np.random.randint(0, height)
            tamanho = np.random.randint(2, 7)
            intensidade = np.random.randint(150, 255)
            velocidade = np.random.randint(2, 5)
            floco_de_neve.append((x, y, tamanho, intensidade, velocidade))
        return floco_de_neve

    if use_camera:
        capture = cv.VideoCapture(0)
        if not capture.isOpened():
            raise RuntimeError("Não foi possível acessar a câmera.")
        
        ret, frame = capture.read()
        if not ret:
            raise RuntimeError("Falha ao capturar frame da câmera.")
        
        height, width, _ = frame.shape
    else:
        if img_path is None:
            raise ValueError("Nenhuma imagem foi fornecida.")
        frame = cv.imread(img_path)
        if frame is None:
            raise ValueError("Imagem inválida ou caminho incorreto.")
        height, width, _ = frame.shape

    floco_de_neve = generate_floco_de_neve(150, width, height)

    while True:
        if use_camera:
            ret, frame = capture.read()
            if not ret:
                print("Falha ao capturar frame da câmera.")
                break

        frame_com_neve, floco_de_neve = nevar(frame, floco_de_neve, qnt_neve=150)

        cv.imshow(window_name, frame_com_neve)

        key = cv.waitKey(1) & 0xFF
        if key == ord('s'):  
            save_path = input("Digite como salvar a imagem, nao esqueca o tipo no final (ex: foto.png): ").strip()
            cv.imwrite(save_path, frame_com_neve)
            print(f"Imagem salva em {save_path}")
        elif key == ord('q'): 
            break

    if use_camera:
        capture.release()
    cv.destroyAllWindows()