import pandas as pd
import os
import matplotlib.pyplot as plt
import time
import seaborn as sns
# my files
import data_processor as dp
import data_visualizer as dv
import report_generator as rg
import data_loader as dl

def main():
    df = dl.load_spotify_data()
    start = time.time()
    rg.generate_report(df)
    end = time.time()
    print(f"Data processed and visualized in: {end - start}")

if __name__ == "__main__":
    main()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
