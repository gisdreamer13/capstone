from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)

users = {
    '1': {
        'username': 'eavila',
        'email': 'eavila@gmail.com'
    },
    '2': {
        'username': 'gavila',
        'email': 'gavila@gmail.com'
    },
    '3': {
        'username': 'ravila',
        'email': 'ravila@gmail.com'
    }
}

animes = {
    '1': {
        'body': 'Jujutsu Kaisen',
        'user_id': '1'
    },
    '2': {
        'body': 'Solo Leveling',
        'user_id': '2'
    },
     '3': {
        'body': 'Black Clover',
        'user_id': '3'
    }
}

#user routes

@app.get('/user')
def user():
    return { 'users': list(users.values()) }, 200

@app.post('/user')
def create_user():
    json_body = request.get_json()
    users[uuid4()] = json_body
    return { 'message': f'{json_body["username"]} created'}, 201

@app.put('/user/<user_id>')
def update_user(user_id):
  try:
    user = users[user_id]
    user_data = request.get_json()
    user |= user_data
    return { 'message': f'{user["username"]} updated'}, 202
  except KeyError:
    return {'message': "Invalid User"}, 400

@app.delete('/user/<user_id>')
def delete_user(user_id):
  # user_data = request.get_json()
  # username = user_data['username']
  try:
    del users[user_id]
    return { 'message': f'User Deleted' }, 202
  except:
    return {'message': "Invalid username"}, 400

#anime Routes

@app.get('/anime')
def get_anime():
  return { 'posts': list(animes.values()) }

@app.post('/anime')
def create_anime():
  post_data = request.get_json()
  user_id = post_data['user_id']
  if user_id in users:
    animes[uuid4()] = post_data
    return { 'message': "Anime Created" }, 201
  return { 'message': "Invalid"}, 401

@app.put('/anime/<anime_id>')
def update_anime(anime_id):
  try:
    print(anime_id)
    anime = animes[anime_id]
    anime_data = request.get_json()
    print(anime_data)
    if anime_data['user_id'] == anime['user_id']:
      anime['body'] = anime_data['body']
      return { 'message': 'Anime Updated' }, 202
    return {'message': "Unauthorized"}, 401
  except:
    return {'message': "Invalid Anime Id"}, 400

@app.delete('/anime/<anime_id>')
def delete_anime(anime_id):
  try:
    del animes[anime_id]
    return {"message": "Anime Deleted"}, 202
  except:
    return {'message':"Invalid Anime"}, 400