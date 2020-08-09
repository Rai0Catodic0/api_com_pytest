from requests import  get,post
import  json

url = 'http://localhost:5000'

def test_get_todos():
    assert get(url)

def test_post_todo():
    content = json.dumps({'name':'teste','done':False})
    assert post('http://localhost:5000/',json=content).text ==  f'sucesso! task teste'

def test_delete_todo():
    id = 1
    assert post(url+f'/delete?id={id}').text == f'task{id} deleted'

def test_update_todo():
    content = json.dumps({'id':1,'name':'teste','done':False})
    assert post(url+'/update',json=content).text == "task does not exist"
    content = json.dumps({'id':2,'name':'teste','done':False})
    assert post(url+'/update',json=content).text == "task teste, done = False"

def teste_json():
    content = json.dumps({'name':'teste','age':14})
    assert  post(url+'/teste',json=content).text == 'sucesso'