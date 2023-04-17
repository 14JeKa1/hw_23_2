from flask import Flask

from app_2 import create_app

app: Flask = create_app()

if __name__ == '__main__':
    app.run(port=25000)

