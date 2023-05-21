import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up Spotify API credentials
client_id = '77e238f16d4c4ad696c0c13ebf18d6ba'
client_secret = '2192639a6a8f477aa1fe31e915922386'
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
