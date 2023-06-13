import sys
from app import App
from infra.client.client import Client

if __name__ == "__main__":
    app = App(sys.argv)
    app.Boostrap(client=Client())
    sys.exit(app.exec_())