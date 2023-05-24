import tkinter as tk
from PIL import ImageTk, Image

def change_page(page_name):
    # Função para mudar o conteúdo com base na página selecionada
    if page_name == 'inicio':
        # Lógica para exibir o conteúdo da página inicial
        pass
    elif page_name == 'explorar':
        # Lógica para exibir o conteúdo da página explorar
        pass
    elif page_name == 'notificacoes':
        # Lógica para exibir o conteúdo da página de notificações
        pass
    elif page_name == 'perfil':
        # Lógica para exibir o conteúdo da página de perfil
        pass

root = tk.Tk()

# Configuração da barra lateral
sidebar = tk.Frame(root, width=100, bg='#EEEEEE')
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# Ícone no topo da barra lateral
icon = ImageTk.PhotoImage(Image.open('assets/icons/icon.png'))
icon_label = tk.Label(sidebar, image=icon)
icon_label.pack()

# Botões de página na barra lateral
pages = ['inicio', 'explorar', 'notificacoes', 'perfil']
for page in pages:
    # Carregar a imagem do ícone da pasta assets/icons
    image = ImageTk.PhotoImage(Image.open(f'assets/icons/{page}.png'))

    # Criar o botão da página
    button = tk.Button(sidebar, image=image, command=lambda page=page: change_page(page))
    button.pack()

# Conteúdo central que muda de acordo com a página selecionada
content = tk.Frame(root, bg='white')
content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Foto de perfil e texto "meu perfil" na barra lateral
profile_image = ImageTk.PhotoImage(Image.open('assets/icons/profile.png'))
profile_label = tk.Label(sidebar, image=profile_image)
profile_label.pack()
profile_text = tk.Label(sidebar, text='Meu Perfil')
profile_text.pack()

root.mainloop()
