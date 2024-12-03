import tkinter as tk
from tkinter import filedialog, messagebox
import FiltroSaturado
import FiltroRosinha
import FiltroPretoBranco
import FiltroNeve
import FiltroDistorcido  
import FiltroDesenho
import FiltroCarnaval  
import FiltroOrelhaGatinho  
import FiltroOlhos  
import Stickers   

def apply_filter(filter_type):
    if filter_type == "Saturação":
        use_camera = messagebox.askyesno("Opção de Entrada", "Deseja usar a câmera?")
        img_path = None

        if not use_camera:
            img_path = filedialog.askopenfilename(
                title="Selecione uma imagem",
                filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"))
            )
            if not img_path:
                return  

        try:
            FiltroSaturado.apply_saturation_filter(img_path=img_path, use_camera=use_camera)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao aplicar o filtro: {e}")

    elif filter_type == "Rosa":
        use_camera = messagebox.askyesno("Opção de Entrada", "Deseja usar a câmera?")
        img_path = None

        if not use_camera:
            img_path = filedialog.askopenfilename(
                title="Selecione uma imagem",
                filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"))
            )
            if not img_path:
                return  

        try:
            FiltroRosinha.apply_pink_filter(img_path=img_path, use_camera=use_camera)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao aplicar o filtro: {e}")

    elif filter_type == "Preto e Branco":
        use_camera = messagebox.askyesno("Opção de Entrada", "Deseja usar a câmera?")
        img_path = None

        if not use_camera:
            img_path = filedialog.askopenfilename(
                title="Selecione uma imagem",
                filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"))
            )
            if not img_path:
                return  

        try:
            FiltroPretoBranco.apply_b_w_filter(img_path=img_path, use_camera=use_camera)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao aplicar o filtro: {e}")

    elif filter_type == "Neve":
        use_camera = messagebox.askyesno("Opção de Entrada", "Deseja usar a câmera?")
        img_path = None

        if not use_camera:
            img_path = filedialog.askopenfilename(
                title="Selecione uma imagem",
                filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"))
            )
            if not img_path:
                return  

        try:
            FiltroNeve.aplicar_neve(img_path=img_path, use_camera=use_camera)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao aplicar o filtro: {e}")

    elif filter_type == "Distorção":
        use_camera = messagebox.askyesno("Opção de Entrada", "Deseja usar a câmera?")
        img_path = None

        if not use_camera:
            img_path = filedialog.askopenfilename(
                title="Selecione uma imagem",
                filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"))
            )
            if not img_path:
                return  

        try:
            FiltroDistorcido.aplicar_filtro_distorcido(img_path=img_path, use_camera=use_camera)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao aplicar o filtro: {e}")

    elif filter_type == "Desenho":
        use_camera = messagebox.askyesno("Opção de Entrada", "Deseja usar a câmera?")
        img_path = None

        if not use_camera:
            img_path = filedialog.askopenfilename(
                title="Selecione uma imagem",
                filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"))
            )
            if not img_path:
                return 

        try:
            FiltroDesenho.aplicar_filtro_desenho(img_path=img_path, use_camera=use_camera)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao aplicar o filtro: {e}")

    elif filter_type == "Carnaval":
        use_camera = messagebox.askyesno("Opção de Entrada", "Deseja usar a câmera?")
        img_path = None

        if not use_camera:
            img_path = filedialog.askopenfilename(
                title="Selecione uma imagem",
                filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"))
            )
            if not img_path:
                return 

        try:
            FiltroCarnaval.aplicar_filtro_carnaval(img_path=img_path, use_camera=use_camera)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao aplicar o filtro: {e}")

    elif filter_type == "Orelha de Gatinho":
        try:
            FiltroOrelhaGatinho.aplicar_orelha_gatinho()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao aplicar o filtro de orelha de gatinho: {e}")

    elif filter_type == "Olhos":
        try:
            FiltroOlhos.aplicar_olhos()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao aplicar o filtro de olhos: {e}")

    elif filter_type == "Sticker":
        try:
            Stickers.choose_and_overlay_sticker() 
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao aplicar o filtro de stickers: {e}")

    else:
        messagebox.showerror("Erro", "Filtro inválido.")
        
def main():
    root = tk.Tk()
    root.title("Aplicador de Filtros")
    root.geometry("400x300") 

    tk.Label(root, text="Selecione um filtro para aplicar:", font=("Arial", 14)).pack(pady=10)

    filters = [
        "Saturação", "Rosa", "Preto e Branco", 
        "Neve", "Distorção", "Desenho", "Carnaval", 
        "Orelha de Gatinho", "Olhos", "Sticker" 
    ]

    selected_filter = tk.StringVar(value="Selecione um filtro")
    dropdown = tk.OptionMenu(root, selected_filter, *filters)
    dropdown.pack(pady=10)

    tk.Button(root, text="Aplicar Filtro", command=lambda: apply_filter(selected_filter.get())).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()