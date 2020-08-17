from flask import Flask, request, render_template
import core
from json import  loads
app = Flask(__name__)

@app.route('/alo')
def alo():
    return render_template('index.html')


@app.route('/',methods=['GET','POST'])
def add_todo():
    if request.method == 'POST':
        content = request.get_json()
        content = loads(content)
        x = core.Task(name=content['name'],done=content['done'])
        x.save()
        return f'sucesso! task {content["name"]}'
    else:
        return str(core.get_task())
    
@app.route('/delete',methods=['POST'])
def delete_todo():
    id = request.args.get('id',default=1,type=int)
    core.delete(id)
    return f'task{id} deletada'

@app.route('/update',methods=['POST'])
def update_todo():
    content =   request.get_json()
    content = loads(content)
    result = core.update(content['id'],content)
    return str(result)