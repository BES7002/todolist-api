from flask import Flask, redirect, request
from tarefa import buscar_tarefas, buscar_tarefa, criar_tarefa

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    return{
        'message': 'Api rodando'   
    }

@app.route('/api/tarefas', methods=['GET'])
def get_tarefas():
    tarefas = buscar_tarefas()
    # link = 'https://www.google.com'
    # return redirect("https://www.gogle.com")
    return tarefas

@app.route('/api/tarefa/<int:todo_id>', methods=['GET'])
def get_tarefa(todo_id):
    tarefa = buscar_tarefa(todo_id)
    return tarefa

# padrao rest
@app.route('/api/tarefas', methods=['POST'])
def create_tarefa():
    # pega o corpo da requisição
    corpo = request.get_json()

    # guarda as informações em variaveis
    tarefa_name = corpo.get('name')
    tarefa_description = corpo.get('description')

    # chama a função e massa as variaveis como argumento
    criar_tarefa(tarefa_name, tarefa_description)
    
    # retorna algo
    return {
        'message': 'Tarefa cadastrada'
    }

# Se for o modulo principal roda o projeto em debug(atualiza o projeto simultaneamente)
if __name__ == '__main__':
    app.run(debug = True)