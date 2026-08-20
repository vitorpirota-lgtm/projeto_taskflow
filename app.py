# importe de biblioteca
from flask import Flask, render_template, request

# criar objeto flask "apelido - app"
app = Flask(__name__)

# Base fake
base_fake = []

# Rotas:
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pessoa')
def pessoa():
    return render_template('pessoa.html')


@app.route('/atividade/criar', methods=['GET', 'POST'])
def criar_atividade():
    if request.method == 'POST':
        # Aqui recebe dados do formulario
        nome_atividade = request.form.get('form_atividade')
        descricao_atividade = request.form.get('form_descricao')
        data_atividade = request.form.get('form_data_atividade')
        categoria_atividade = request.form.getlist('form_categoria')
        importancia_atividade = request.form.get('form_importancia')

        dados = {
            'nome_atividade': nome_atividade,
            'descricao_atividade': descricao_atividade,
            'data_atividade': data_atividade,
            'categoria_atividade': categoria_atividade,
            'importancia_atividade': importancia_atividade
        }


        print(f"dados cadastrados: {dados}")
        base_fake.append(dados)
        print(f'base_fake: {base_fake}')
        return render_template('listar_atividades.html', dados_atividade=base_fake)

    return render_template('criar_atividade.html')

@app.route('/atividades/Listar')

def listar_atividades():
    return render_template('listar_atividades.html', dados_atividade=base_fake)


# Iniciar aplicação web
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
    # Nada deve ser colocado abaixo
