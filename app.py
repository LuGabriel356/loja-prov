from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/produtos')
def produtos():
    return render_template('usuarios/produtos.html')

@app.route('/carrinho')
def carrinho():
    return render_template('usuarios/carrinho.html')

@app.route('/novidades')
def novidades():
    return render_template('usuarios/novidades.html')






if __name__ == '__main__':
    # debug=True ativa o recarregamento automático ao salvar o arquivo
    # NUNCA use debug=True em produção (servidor público)
    app.run(debug=True)