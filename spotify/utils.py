from datetime import timedelta
from .models import SpotifyToken
from django.utils import timezone
from dotenv import load_dotenv
from requests import post,put,get
import os
load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
BASE_URL = "https://api.spotify.com/v1/me/"

def get_user_tokens(session_key):
    user_tokens = SpotifyToken.objects.filter(user=session_key)
    if user_tokens.exists():
        return user_tokens[0]
    else:
        return None

def update_or_create_user_tokens(session_key, access_token, token_type, expires_in, refresh_token):
    tokens = get_user_tokens(session_key) # will return a queryset object or none 
    expires_in = timezone.now() + timedelta(seconds=expires_in) #expires_in is originally a numeric values which represents seconds,I convert it to the exact time, it will expire

    if tokens:
        tokens.access_token = access_token 
        tokens.refresh_token = refresh_token
        tokens.expires_in = expires_in
        tokens.token_type = token_type
        tokens.save(update_fields=['access_token', 'refresh_token', 'expires_in', 'token_type'])# thats we can directly acees the save methos
    else:
        tokens = SpotifyToken(user= session_key, access_token=access_token, refresh_token=refresh_token, token_type=token_type,expires_in=expires_in)
        tokens.save()

    
def is_spotify_authenticated(session_key):
    tokens = get_user_tokens(session_key)
    if tokens:
        expiry = tokens.expires_in
        if expiry <= timezone.now():
            refresh_spotify_token(session_key)
        return True

    return False

#refresh-token stays the same

def refresh_spotify_token(session_key):
    refresh_token = get_user_tokens(session_key).refresh_token

    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type' : 'refresh_token',
        'refresh_token' : refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    expires_in = response.get('expires_in')

    update_or_create_user_tokens(session_key,access_token,token_type,expires_in,refresh_token)


def execute_spotify_api_request(session_key, endpoint, post_=False, put_=False):
    tokens = get_user_tokens(session_key)
    
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : "Bearer " + tokens.access_token
    }

    if post_:
        x = post(BASE_URL + endpoint , headers=headers) 
        print("post diya", x)

    if put_:
        x = put(BASE_URL + endpoint, headers=headers)
        print("put diya",x)

    response = get(BASE_URL+endpoint, {}, headers=headers)
    
    try :
        return response.json()
    except :
        return {
            'Error' : 'Issue with request'
        }


def play_song(session_key):
    return execute_spotify_api_request(session_key, "player/play", put_=True)

def pause_song(session_key):
    return execute_spotify_api_request(session_key, "player/pause", put_=True)

def skip_song(session_key):
    return execute_spotify_api_request(session_key, "player/next",post_=True)
    