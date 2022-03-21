import pandas as pd
import fitparse

def fit2pd(fname):
    cols = []
    rows = []
    
    fitfile = fitparse.FitFile(fname)
    # Load the FIT file
    for record in fitfile.get_messages("record"):
        # Records can contain multiple pieces of data (ex: timestamp, latitude, longitude, etc)
        cols = [d.name for d in record]
        data = [d.value for d in record]
        sub_df = pd.DataFrame([data], columns=cols)
        rows.append(sub_df)
    df = pd.concat(rows)
    # treat file
    df.timestamp = pd.to_datetime(df.timestamp)
    df.distance = df.distance / 1000 # m to km
    df.speed = df.speed * 3.6 # m/s to km/h
    return df

