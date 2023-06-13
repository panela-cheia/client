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
    [sg.Image(filename='src/assets/images/logo.png',background_color=("#FFFFFF"))],
    [sg.Button('', image_filename='src/assets/icons/home.png', key='inicio',button_color=("#FFFFFF","#FFFFFF"),size=(184,44),border_width=0)],
    [sg.Button('', image_filename='src/assets/icons/buteco.png', key='explorar',button_color=("#FFFFFF","#FFFFFF"),size=(184,44),border_width=0)],
    [sg.Button('', image_filename='src/assets/icons/search.png', key='notificacoes',button_color=("#FFFFFF","#FFFFFF"),size=(184,44),border_width=0)],
    [sg.Button('', image_filename='src/assets/icons/armazem.png', key='perfil',button_color=("#FFFFFF","#FFFFFF"),size=(184,44),border_width=0)],
    [sg.Image(filename='src/assets/images/user.png'), sg.Text('Meu Perfil')]
]

# Definir o layout do conteúdo
content_layout = [
    [sg.Text('Conteúdo da página')],
    # Adicione aqui os elementos do conteúdo da página
]

# Definir o layout principal
layout = [
    [
        sg.Column(sidebar_layout, background_color='#FFF', pad=(0, 0), element_justification='center',vertical_alignment='center',justification='space-between' ,k='-SIDEBAR-',size=(288,1080)), 
        sg.Column(content_layout, k='-CONTENT-')
    ]
]

window = sg.Window('Panela Cheia', layout,resizable=True)

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
