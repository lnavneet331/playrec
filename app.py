import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pickle
loaded_model = pickle.load(open('rf_model.sav', 'rb'))
import pandas as pd
import os

# Set up Spotify API credentials
client_id = os.getenv("client_id")
client_secret = os.getenv('client_secret')
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to search for a song and get its Spotify ID and audio features
def get_song_details(song_name):
    results = sp.search(q=song_name, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        spotify_id = track['id']
        st.write("Spotify ID: ", spotify_id)
        audio_features = sp.audio_features([spotify_id])[0]
        return spotify_id, audio_features
    else:
        return None, None

# Streamlit app
st.title("Song Details")

# User input
song_name = st.text_input("Enter a song name")

if song_name:
    # Get Spotify ID and audio features
    spotify_id, audio_features = get_song_details(song_name)

    if spotify_id and audio_features:
        # Display song details
        # st.write(f"Spotify ID for '{song_name}': {spotify_id}")
        # st.write("Audio Features:")
        # st.write(audio_features)
        # convert audio features to dataframe
        audio_features = pd.DataFrame(audio_features, index=[0])
        audio_features = audio_features.drop(['key', 'mode', 'speechiness', 'type', 'id', "uri", "track_href", "analysis_url", "time_signature"], axis=1)
        result = loaded_model.predict(audio_features)
        for i in result:
            if i == -1:
                st.write("You probably won't like this song 🚫")
            elif i == 1:
                st.write("You probably will like this song 💖")
            else:
                st.write("Not enough data to predict 🤷")
    else:
        st.write(f"No song found for '{song_name}'.")
