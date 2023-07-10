import sys

from app import App

from config.app_url import API_URL

from infra.middleware.rmi import RMI
from infra.web.web_client import WebClient

if __name__ == "__main__":
    app = App(sys.argv)
    app.Boostrap(client=RMI(),webClient=WebClient(base_url=API_URL))
    sys.exit(app.exec_())