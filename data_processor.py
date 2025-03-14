import pandas as pd
import os
import matplotlib.pyplot as plt
import time
import seaborn as sns
import datetime as datetime

#sum of playtime of songs from each album
def mostPlayedAlbums(df):
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
def mostPlayedSongs(df):
    song = df.groupby(["master_metadata_track_name", "master_metadata_album_album_name", "master_metadata_album_artist_name"])["ms_played"].sum().div(3600000)
    song_df = song.reset_index().rename(columns={"master_metadata_track_name" : "song",
                                                 "master_metadata_album_album_name" : "album",
                                                 "master_metadata_album_artist_name" : "artist",
                                                 "ms_played": "hours_played"})
    song_df = song_df.nlargest(10, "hours_played")
    return song_df

def listeningTimeByYear(df):
    df["year"] = df["ts"].str.split("-").str[0]
    time = df.groupby(["year"])["ms_played"].sum().div(3600000).reset_index(name="hours_played")
    return time

def mostSkippedTracks(df):
    skips = df.groupby(["skipped", "master_metadata_track_name", "master_metadata_album_album_name", "master_metadata_album_artist_name"]).size().reset_index(name="times_skipped")
    skips_df = skips.reset_index().rename(columns={"master_metadata_track_name" : "song",
                                                 "master_metadata_album_album_name" : "album",
                                                 "master_metadata_album_artist_name" : "artist"})
    skips_df = skips_df[skips_df["skipped"] != False]
    skips_df = skips_df.nlargest(10, "times_skipped")
    return skips_df

def listeningByHour(df):
    df["ts"] = df["ts"].str.split("T").str[1].str.split(":").str[0]
    time_df = df.groupby(["ts"])["ms_played"].sum().reset_index(name="time")
    total_playtime = time_df["time"].sum()
    time_df["percent"] = time_df["time"]/total_playtime * 100
    return time_df

def listeningByWeekday(df):
    df["ts"] = pd.to_datetime(df["ts"])  
    df["weekday"] = df["ts"].dt.day_name()
    day = df.groupby(["weekday"])["ms_played"].sum().reset_index(name="time")
    total_playtime = day["time"].sum()
    day["percent"] = day["time"]/total_playtime * 100
    weekdays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    day["weekday"] = pd.Categorical(day["weekday"], categories=weekdays, ordered=True)
    day = day.sort_values("weekday").reset_index(drop=True)
    return day

def listeningHeatmap(df):
    df["ts"] = pd.to_datetime(df["ts"])    
    df["year"] = df["ts"].dt.year
    df["month"] = df["ts"].dt.month
    df["hr"] = df["ts"].dt.hour
    df["weekday"] = df["ts"].dt.day_name()
    heatMap_df = df.groupby(["hr","weekday"])["ms_played"].sum().reset_index()
    total_playtime = heatMap_df["ms_played"].sum()
    heatMap_df["percent"] = heatMap_df["ms_played"]/total_playtime * 100
    
    weekdays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    heatMap_df = heatMap_df.pivot(index="hr", columns="weekday", values="percent")
    heatMap_df = heatMap_df[weekdays]
    return heatMap_df

def top10RecurringSongsByMonth(df, year="2024"):    
    df["year"] = df["ts"].str.split("T").str[0].str.split("-").str[0]
    df["month"] = df["ts"].str.split("T").str[0].str.split("-").str[1]
    month_mapping = {
        "01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr", "05": "May", "06": "Jun",
        "07": "Jul", "08": "Aug", "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"
    }
    df["month"] = df["month"].map(month_mapping)


    month_year_df = df.groupby(["year","month","master_metadata_track_name", "master_metadata_album_album_name", "master_metadata_album_artist_name"])["ms_played"].sum().reset_index(name="play_time")  
    month_year_df = month_year_df.reset_index().rename(columns = { "master_metadata_track_name" : "song",
                                                  "master_metadata_album_album_name" : "album",
                                                  "master_metadata_album_artist_name" : "artist"})
    month_year_df = month_year_df[month_year_df["year"] == year] 
    monthly_dfs = month_year_df.groupby("month").apply(lambda x: x.nlargest(10, "play_time")).reset_index(drop=True)
    monthly_dfs["song_artist"] = monthly_dfs["song"] + " (" + monthly_dfs["artist"] + ")"
    song_counts = monthly_dfs["song_artist"].value_counts()

    #filter songs that appear more than once in the top 10
    filtered_dfs = monthly_dfs[monthly_dfs["song_artist"].isin(song_counts[song_counts > 1].index)]
    filtered_dfs["rank"] = filtered_dfs.groupby("month")["play_time"].rank(ascending=False)
    pivot_df = filtered_dfs.pivot(index="song_artist", columns="month", values="rank")
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    pivot_df = pivot_df.reindex(columns=months, fill_value=None)
    return pivot_df