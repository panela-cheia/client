import PySimpleGUI as sg

def change_page(layout, page_name):
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

# Definir o layout da barra lateral
sidebar_layout = [
    [sg.Image(filename='assets/icons/icon.png')],
    [sg.Button('', image_filename='assets/icons/inicio.png', key='inicio')],
    [sg.Button('', image_filename='assets/icons/explorar.png', key='explorar')],
    [sg.Button('', image_filename='assets/icons/notificacoes.png', key='notificacoes')],
    [sg.Button('', image_filename='assets/icons/perfil.png', key='perfil')],
    [sg.Image(filename='assets/icons/profile.png'), sg.Text('Meu Perfil')]
]

# Definir o layout do conteúdo
content_layout = [
    [sg.Text('Conteúdo da página')],
    # Adicione aqui os elementos do conteúdo da página
]

# Definir o layout principal
layout = [
    [sg.Column(sidebar_layout, background_color='#EEEEEE', pad=(0, 0), element_justification='center', k='-SIDEBAR-'), 
     sg.Column(content_layout, k='-CONTENT-')]
]

window = sg.Window('Instagram', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event.startswith('inicio'):
        change_page(content_layout, 'inicio')
    elif event.startswith('explorar'):
        change_page(content_layout, 'explorar')
    elif event.startswith('notificacoes'):
        change_page(content_layout, 'notificacoes')
    elif event.startswith('perfil'):
        change_page(content_layout, 'perfil')

window.close()
