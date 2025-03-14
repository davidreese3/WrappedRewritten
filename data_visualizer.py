import pandas as pd
import os
import matplotlib.pyplot as plt
import time
import seaborn as sns

def plotMostPlayedAlbums(df):
    df["album_artist"] = df["album"] + " (" + df["artist"] + ")"
    fig, ax = plt.subplots() 
    ax.plot(df["album_artist"], df["hours_played"], marker="o", linestyle="-")
    ax.set_xlabel("Album")
    ax.set_ylabel("Hours Played")
    ax.set_title("Top Albums by Hours Played")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    return fig  

def plotMostPlayedSongs(df):
    df["song_artist"] = df["song"] + " (" + df["artist"] + ")"
    
    fig, ax = plt.subplots()
    ax.plot(df["song_artist"], df["hours_played"], marker="o", linestyle="-")
    
    ax.set_xlabel("Song")
    ax.set_ylabel("Hours Played")
    ax.set_title("Top Songs by Hours Played")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    
    return fig

def plotMostPlayedArtist(df):   
    fig, ax = plt.subplots()
    ax.plot(df["artist"], df["hours_played"], marker="o", linestyle="-")
    
    ax.set_xlabel("Artist")
    ax.set_ylabel("Hours Played")
    ax.set_title("Top Artist by Hours Played")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    
    return fig

def plotListeningTimeByYear(df):
    fig, ax = plt.subplots()
    ax.plot(df["year"], df["hours_played"], marker="o", linestyle="-")
    
    ax.set_xlabel("Year")
    ax.set_ylabel("Hours Played")
    ax.set_title("Hours Played Per Year")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    
    return fig

def plotMostSkippedTracks(df):
    df["song_artist"] = df["song"] + " (" + df["artist"] + ")"
    
    fig, ax = plt.subplots()
    ax.plot(df["song_artist"], df["times_skipped"], marker="o", linestyle="-")
    
    ax.set_xlabel("Song")
    ax.set_ylabel("Times Skipped")
    ax.set_title("Times Skipped Per Song")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    
    return fig

def plotListeningByHour(df):
    fig, ax = plt.subplots()
    ax.plot(df["ts"], df["percent"], marker="o", linestyle="-")
    
    ax.set_xlabel("Time of Day")
    ax.set_ylabel("Percentage of Listening")
    ax.set_title("Percentage of Listening at Time of Day")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    
    return fig

def plotListeningByWeekday(df):
    fig, ax = plt.subplots()
    ax.plot(df["weekday"], df["percent"], marker="o", linestyle="-")
    
    ax.set_xlabel("Day of Week")
    ax.set_ylabel("Percentage of Listening")
    ax.set_title("Percentage of Listening at Day of Week")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    
    return fig

def plotListeningHeatmap(df):
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(df, cmap="viridis", ax=ax)
    
    ax.set_xlabel("Day of Week")
    ax.set_ylabel("Time of Day")
    ax.set_title("Heatmap of Streaming")
    plt.xticks(rotation=0)  
    plt.tight_layout()
    
    return fig

def plotTop10RecurringSongsByMonth (df):    
    fig, ax = plt.subplots(figsize=(10, 10)) 
    sns.heatmap(df, cmap="viridis", ax=ax, annot=True)
    
    ax.set_xlabel("Month")
    ax.set_ylabel("Song")
    ax.set_title("Heatmap of Recurring Top 10 Songs")
    plt.xticks(rotation=0)  
    plt.tight_layout()
    
    return fig
