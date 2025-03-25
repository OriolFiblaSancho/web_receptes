from app.main import main  # Importa la instancia de Flask
from waitress import serve

if __name__ == "__main__":
    serve(main, host="0.0.0.0", port=5000)

