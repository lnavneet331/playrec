import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up Spotify API credentials
client_id = "client_id"
client_secret = 'client_secret'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to get the song name from a Spotify URI
def get_song_name(spotify_uri):
    track = sp.track(spotify_uri)
    if track:
        return track['name']
    else:
        return None

# Example usage
spotify_uri = input("Enter a Spotify URI: ")
song_name = get_song_name(spotify_uri)

if song_name:
    print(f"Song name for '{spotify_uri}': {song_name}")
else:
    print(f"No song name found for '{spotify_uri}'.")
