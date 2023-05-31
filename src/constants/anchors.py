from screens.main.widgets.home import HomeWidget
from screens.main.widgets.dive import DiveWidget
from screens.main.widgets.search import SearchWidget
from screens.main.widgets.barn import BarnWidget

anchors = [
    {
        "label": "Home",
        "icon": "icons/home.png",
        "widget": HomeWidget
    },
    {
        "label": "Butecos",
        "icon": "icons/dive.png",
        "widget": DiveWidget
    },
    {
        "label": "Pesquisar",
        "icon": "icons/search.png",
        "widget": SearchWidget
    },
    {
        "label": "Armazém",
        "icon": "icons/barn.png",
        "widget": BarnWidget
    }
]