#Arquivo Main para iniciar todo o processo de automação

from CancelamentoFuncao.src.gui.app import app

if(__name__ == "__main__"):
    app.run(debug=True, port=5000)