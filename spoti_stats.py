import pandas as pd
import os
import matplotlib.pyplot as plt
import time

def main():
    start = time.time()
    df = setUp()
    ta = topAlbums(df)
    ts = topSongs(df)
    tpy = timePerYear(df)
    end = time.time()
    topAlbumsPlot(ta)
    topSongsPlot(ts)
    timePerYearPlot(tpy)
    print(f"Data calculated in: {end - start}")

def setUp():
    file_location_prefix = "my_spotify_data/Spotify Extended Streaming History/Streaming_History_Audio_"
    files = ["2018-2019_0","2019-2020_1","2020_2","2020_3","2020_4","2020-2021_5","2021_6","2021-2022_7",
             "2022_8","2022_9","2022-2023_10","2023_11","2023-2024_12","2024_13","2024-2025_14"]
    dataframes = []
    for file in files:
        df = pd.read_json(file_location_prefix + file + ".json")
        dataframes.append(df)
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df

#sum of playtime of songs from each album
def topAlbums(df):
    albums = df.groupby(["master_metadata_album_album_name", "master_metadata_album_artist_name"])["ms_played"].sum().div(3600000)
    album_df = albums.reset_index().rename(columns={"master_metadata_album_album_name": "album", 
                                                "master_metadata_album_artist_name": "artist", 
                                                "ms_played": "hours_played"})
    album_df = album_df.sort_values(by="hours_played", ascending=False).head(10)
    return album_df

"""
sum of the most played songs, distinguishing by artist and album to account for different songs with the same name. 
however, it still differentiates between EP and LP versions.
"""
def topSongs(df):
    song = df.groupby(["master_metadata_track_name", "master_metadata_album_album_name", "master_metadata_album_artist_name"]).size().reset_index(name="times_played")
    song_df = song.reset_index().rename(columns={"master_metadata_track_name" : "song",
                                                 "master_metadata_album_album_name" : "album",
                                                 "master_metadata_album_artist_name" : "artist"})
    song_df = song_df.nlargest(10, "times_played")
    return song_df

def timePerYear(df):
    df["year"] = df["ts"].str.split("-").str[0]
    time = df.groupby(["year"])["ms_played"].sum().div(3600000).reset_index(name="hours_played")
    return time

def topAlbumsPlot(df):
    df["album_artist"] = df["album"] + " (" + df["artist"] + ")"
    plt.plot(df["album_artist"], df["hours_played"], marker="o", linestyle="-")
    plt.xlabel("Album")
    plt.ylabel("Hours Played")
    plt.title("Top Albums by Hours Played")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    plt.show()

def topSongsPlot(df):
    df["song_artist"] = df["song"] + " (" + df["artist"] + ")"
    plt.plot(df["song_artist"], df["times_played"], marker="o", linestyle="-")
    plt.xlabel("Song")
    plt.ylabel("Times Played")
    plt.title("Top Songs by Time Played")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    plt.show()

def timePerYearPlot(df):
    plt.plot(df["year"], df["hours_played"], marker="o", linestyle="-")
    plt.xlabel("Year")
    plt.ylabel("Hours Played")
    plt.title("Hours Played Per Year")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       