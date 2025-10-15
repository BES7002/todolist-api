from flask import jsonify

def buscar_tarefas():
    tarefas = [
        {
            'id':1,
            'nome':'Aprender digitação',
            'descricao': 'Vamos aumentar o zoom para não errar',
            'default': 'Pendente'
        },
        {
            'id':2,
            'nome':'Caminhar',
            'descricao': '120Km durante o periodo matutino',
            'default': 'Pendente'
        },
    ]
    return jsonify(tarefas)

def buscar_tarefa():
    tarefa = {
        'id':3,
        'nome':'Aprender natação',
        'descricao': 'Vamos nadar',
        'default': 'Pendente'
    }
    return jsonify(tarefa)
