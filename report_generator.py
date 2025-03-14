from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import data_loader as dl
import data_processor as dp
import data_visualizer as dv



def generate_report(df, year):
    with PdfPages('report.pdf') as pdf:
        df_original = df.copy()

        figures = []
        
        mpa = dp.mostPlayedAlbums(df_original.copy())
        if not mpa.index.empty: 
            figures.append(dv.plotMostPlayedAlbums(mpa))

        mps = dp.mostPlayedSongs(df_original.copy())
        if not mps.index.empty: 
            figures.append(dv.plotMostPlayedSongs(mps))
        if year == "":
            lty = dp.listeningTimeByYear(df_original.copy())
            if not lty.index.empty: 
                figures.append(dv.plotListeningTimeByYear(lty))

        mst = dp.mostSkippedTracks(df_original.copy())
        if not mst.index.empty: 
            figures.append(dv.plotMostSkippedTracks(mst))

        lbh = dp.listeningByHour(df_original.copy())
        if not lbh.index.empty: 
            figures.append(dv.plotListeningByHour(lbh))

        lbw = dp.listeningByWeekday(df_original.copy())
        if not lbw.index.empty: 
            figures.append(dv.plotListeningByWeekday(lbw))

        lh = dp.listeningHeatmap(df_original.copy())
        if not lh.index.empty: 
            figures.append(dv.plotListeningHeatmap(lh))

        if year != "":
            t10sm = dp.top10RecurringSongsByMonth(df_original.copy(), year)  
        else :
            t10sm = dp.top10RecurringSongsByMonth(df_original.copy())
            
        if not t10sm.index.empty:
             figures.append(dv.plotTop10RecurringSongsByMonth(t10sm))

        for fig in figures:
            pdf.savefig(fig)
            plt.close(fig)  
