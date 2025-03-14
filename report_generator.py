from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import data_loader as dl
import data_processor as dp
import data_visualizer as dv



def generate_report(df):
    with PdfPages('report.pdf') as pdf:
        df_original = df.copy()

        mpa = dp.mostPlayedAlbums(df_original.copy())
        mps = dp.mostPlayedSongs(df_original.copy())
        lty = dp.listeningTimeByYear(df_original.copy())
        mst = dp.mostSkippedTracks(df_original.copy())
        lbh = dp.listeningByHour(df_original.copy())
        lbw = dp.listeningByWeekday(df_original.copy())
        lh = dp.listeningHeatmap(df_original.copy())
        t10sm = dp.top10SongsByMonth(df_original.copy(), year="2024")  

        figures = [
            dv.plotMostPlayedAlbums(mpa),
            dv.plotMostPlayedSongs(mps),
            dv.plotListeningTimeByYear(lty),
            dv.plotMostSkippedTracks(mst),
            dv.plotListeningByHour(lbh),
            dv.plotListeningByWeekday(lbw),
            dv.plotListeningHeatmap(lh),
            dv.plotTop10SongsByMonth(t10sm)
        ]
        
        for fig in figures:
            pdf.savefig(fig)
            plt.close(fig)  
