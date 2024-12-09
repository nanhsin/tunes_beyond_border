from datetime import datetime
import json
import requests
import os
from dotenv import load_dotenv


def init():
    '''Initialize the environment.'''
    load_dotenv()

    global spotify_cid
    global spotify_secret

    spotify_cid = os.getenv("SPOTIFY_CID")
    spotify_secret = os.getenv("SPOTIFY_SECRET")


def getSpotifyToken():
    '''
    Get the Spotify access token.
    
    Returns:
        str: The Spotify access token.
    '''
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        data={
        "grant_type": "client_credentials",
        "client_id": spotify_cid,
        "client_secret": spotify_secret,
    }).json()

    return response["access_token"]


def getSpotifyPlaylist(token, playlist_id):
    '''
    Get the songs in a Spotify playlist.
    
    Parameters:
        token (str): The Spotify access token.
        playlist_id (str): The Spotify ID of the playlist.
        
    Returns:
        list: The list of songs in the playlist.
    '''
    headers = {"Authorization": "Bearer " + token}
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?fields=items(added_at,track(id,name,album(id,name),artists(id,name)))"
    response = requests.get(url, headers=headers).json()
    return response["items"]


def getSpotifyTrack(token, track_id):
    '''
    Get the Spotify track information.
    
    Parameters:
        token (str): The Spotify access token.
        track_id (str): The Spotify ID of the track.
        
    Returns:
        dict: The Spotify track information.
    '''
    headers = {"Authorization": "Bearer " + token}
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    response = requests.get(url, headers=headers)
    return response.json()


def getSpotifyFeatures(token, track_id):
    '''
    Get the Spotify features of a song.
    
    Parameters:
        token (str): The Spotify access token.
        track_id (str): The Spotify ID of the song.
        
    Returns:
        dict: The Spotify features of the song.
    '''
    headers = {"Authorization": "Bearer " + token}
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    response = requests.get(url, headers=headers)
    return response.json()


def getSpotifyAlbumTracks(token, album_id):
    '''
    Get the tracks in a Spotify album.
    
    Parameters:
        token (str): The Spotify access token.
        album_id (str): The Spotify ID of the album.
        
    Returns:
        list: The list of tracks' ID in the album.
    '''
    headers = {"Authorization": "Bearer " + token}
    url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
    response = requests.get(url, headers=headers).json()

    track_ids = []
    for track in response["items"]:
        track_ids.append(track["id"])
    return track_ids


def getSpotifyCharts():
    '''Get the Spotify charts.'''
    playlist_id = {
        "Global": "37i9dQZEVXbMDoHDwVN2tF",
        'Argentina': '37i9dQZEVXbMMy2roB9myp',
        'Australia': '37i9dQZEVXbJPcfkRz0wJ0',
        'Austria': '37i9dQZEVXbKNHh6NIXu36',
        'Baltics': '37i9dQZEVXbMx56Rdq5lwc',
        'Belarus': '37i9dQZEVXbIYfjSLbWr4V',
        'Belgium': '37i9dQZEVXbJNSeeHswcKB',
        'Bolivia': '37i9dQZEVXbJqfMFK4d691',
        'Brazil': '37i9dQZEVXbMXbN3EUUhlg',
        'Bulgaria': '37i9dQZEVXbNfM2w2mq1B8',
        'Canada': '37i9dQZEVXbKj23U1GF4IR',
        'Chile': '37i9dQZEVXbL0GavIqMTeb',
        'Colombia': '37i9dQZEVXbOa2lmxNORXQ',
        'Costa Rica': '37i9dQZEVXbMZAjGMynsQX',
        'Czech Republic': '37i9dQZEVXbIP3c3fqVrJY',
        'Denmark': '37i9dQZEVXbL3J0k32lWnN',
        'Dominican Republic': '37i9dQZEVXbKAbrMR8uuf7',
        'Ecuador': '37i9dQZEVXbJlM6nvL1nD1',
        'Egypt': '37i9dQZEVXbLn7RQmT5Xv2',
        'El Salvador': '37i9dQZEVXbLxoIml4MYkT',
        'Estonia': '37i9dQZEVXbLesry2Qw2xS',
        'Finland': '37i9dQZEVXbMxcczTSoGwZ',
        'France': '37i9dQZEVXbIPWwFssbupI',
        'Germany': '37i9dQZEVXbJiZcmkrIHGU',
        'Global': '37i9dQZEVXbMDoHDwVN2tF',
        'Greece': '37i9dQZEVXbJqdarpmTJDL',
        'Guatemala': '37i9dQZEVXbLy5tBFyQvd4',
        'Honduras': '37i9dQZEVXbJp9wcIM9Eo5',
        'Hong Kong': '37i9dQZEVXbLwpL8TjsxOG',
        'Hungary': '37i9dQZEVXbNHwMxAkvmF8',
        'Iceland': '37i9dQZEVXbKMzVsSGQ49S',
        'India': '37i9dQZEVXbLZ52XmnySJg',
        'Indonesia': '37i9dQZEVXbObFQZ3JLcXt',
        'Ireland': '37i9dQZEVXbKM896FDX8L1',
        'Israel': '37i9dQZEVXbJ6IpvItkve3',
        'Italy': '37i9dQZEVXbIQnj7RRhdSX',
        'Japan': '37i9dQZEVXbKXQ4mDTEBXq',
        'Kazakhstan': '37i9dQZEVXbM472oKPNKzS',
        'Latvia': '37i9dQZEVXbJWuzDrTxbKS',
        'Lithuania': '37i9dQZEVXbMx56Rdq5lwc',
        'Luxembourg': '37i9dQZEVXbKGcyg6TFGx6',
        'Malaysia': '37i9dQZEVXbJlfUljuZExa',
        'Mexico': '37i9dQZEVXbO3qyFxbkOE1',
        'Morocco': '37i9dQZEVXbJU9eQpX8gPT',
        'Netherlands': '37i9dQZEVXbKCF6dqVpDkS',
        'New Zealand': '37i9dQZEVXbM8SIrkERIYl',
        'Nicaragua': '37i9dQZEVXbISk8kxnzfCq',
        'Nigeria': '37i9dQZEVXbKY7jLzlJ11V',
        'Norway': '37i9dQZEVXbJvfa0Yxg7E7',
        'Pakistan': '37i9dQZEVXbJkgIdfsJyTw',
        'Panama': '37i9dQZEVXbKypXHVwk1f0',
        'Paraguay': '37i9dQZEVXbNOUPGj7tW6T',
        'Peru': '37i9dQZEVXbJfdy5b0KP7W',
        'Philippines': '37i9dQZEVXbNBz9cRCSFkY',
        'Poland': '37i9dQZEVXbN6itCcaL3Tt',
        'Portugal': '37i9dQZEVXbKyJS56d1pgi',
        'Romania': '37i9dQZEVXbNZbJ6TZelCq',
        'Saudi Arabia': '37i9dQZEVXbLrQBcXqUtaC',
        'Singapore': '37i9dQZEVXbK4gjvS1FjPY',
        'Slovakia': '37i9dQZEVXbKIVTPX9a2Sb',
        'South Africa': '37i9dQZEVXbMH2jvi6jvjk',
        'South Korea': '37i9dQZEVXbNxXF4SkHj9F',
        'Spain': '37i9dQZEVXbNFJfN1Vw8d9',
        'Sweden': '37i9dQZEVXbLoATJ81JYXz',
        'Switzerland': '37i9dQZEVXbJiyhoAPEfMK',
        'Taiwan': '37i9dQZEVXbMnZEatlMSiu',
        'Thailand': '37i9dQZEVXbMnz8KIWsvf9',
        'Turkey': '37i9dQZEVXbIVYVBNw9D5K',
        'UAE': '37i9dQZEVXbM4UZuIrvHvA',
        'US': '37i9dQZEVXbLRQDuF5jeBp',
        'Ukraine': '37i9dQZEVXbKkidEfWYRuD',
        'United Kingdom': '37i9dQZEVXbLnolsZ8PSNw',
        'Uruguay': '37i9dQZEVXbMJJi3wgRbAy',
        'Venenzuela': '37i9dQZEVXbNLrliB10ZnX',
        'Vietnam': '37i9dQZEVXbLdGSmz6xilI'
    }
    spotify_token = getSpotifyToken()
    full_playlist = {}
    for country in playlist_id:
        print(f"Getting Spotify chart for {country}...")
        playlist = getSpotifyPlaylist(spotify_token, playlist_id[country])
        full_playlist[country] = playlist
    return full_playlist


def exportData():
    '''Export the dataset to a JSON file.'''
    data = getSpotifyCharts()
    date = datetime.today().strftime("%Y%m%d")
    filename = f"project/data/spotify_chart_{date}.json"
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Exported data to {filename}")


if __name__ == "__main__":
    exportData()
