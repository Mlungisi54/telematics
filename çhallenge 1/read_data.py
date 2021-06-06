
import pandas as pd
import seaborn as sns
import numpy as np
path_to_file1 = "4cb82c2383ad.csv"
path_to_file2 = "4cb82c20117b.csv"


def _set_types(data_frame):
    """
    serverTime    datetime64[ns]
    phoneTime     datetime64[ns]
    deviceId              object
    lat                  float32
    lon                  float32
    acc                  float32
    speed                float32
    ts            datetime64[ns]
    dtype: object
    :type data_frame: pd.DataFrame
    """
    data_frame[["lat", "lon", "acc", "speed"]] = data_frame[["lat", "lon", "acc", "speed"]].apply(pd.to_numeric)
    # data_frame[["serverTime", "phoneTime", "ts"]] = pd.to_datetime(data_frame[["serverTime", "phoneTime", "ts"]])
    return data_frame


def _clean_data(data_frame):
    data_frame = data_frame.replace(np.nan, 0)
    return data_frame


def do_heat_map(data_pd):
    data_pd = data_pd[['serverTime', 'phoneTime', 'deviceId', 'lat', 'lon', 'acc', 'speed', 'ts']]
    sns.heatmap(data_pd.corr())


data_file1 = pd.read_csv(path_to_file1)
data_file1 = _set_types(data_file1)
data_file1 = _clean_data(data_file1)
print(data_file1.head())

data_file2 = pd.read_csv(path_to_file2)
data_file2 = _set_types(data_file2)
data_file2 = _clean_data(data_file2)
print(data_file2.head())


