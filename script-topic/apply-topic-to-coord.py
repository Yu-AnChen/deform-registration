import tifffile
import numpy as np
import pandas as pd


case_number = range(34, 41)

for nn in case_number:
    print(nn)
    _topic = tifffile.imread(
        rf"/Users/yuanchen/Dropbox (HMS)/000 local remote sharing/20240714-deform-registration-crc/topic-img/C{nn:02}-topics.ome.tif"
    )
    assert (_topic > 0).sum(axis=0).max() == 1
    topic = (_topic > 0) * np.arange(len(_topic)).reshape(-1, 1, 1)
    topic = topic.sum(axis=0)

    # FIXME pad topic image
    topic = np.pad(topic, [(0, 1), (0, 1)])

    df = pd.read_csv(
        rf"/Users/yuanchen/Dropbox (HMS)/000 local remote sharing/20240714-deform-registration-crc/img-data/C{nn:02}-xy-moving-mapped.csv.zip",
        index_col="CellID",
    )

    coord = df[["tY_centroid", "tX_centroid"]].values
    coord *= 0.325
    coord /= 100

    coord = np.floor(coord).astype("int")

    df["tTopic"] = topic[coord[:, 0], coord[:, 1]]
    df.to_csv(
        rf"/Users/yuanchen/Dropbox (HMS)/000 local remote sharing/20240714-deform-registration-crc/img-data/C{nn:02}-xy-moving-mapped-topic.csv.zip",
        compression="zip",
    )


# ---------------------------------------------------------------------------- #
#                           special treatment for C33                          #
# ---------------------------------------------------------------------------- #

def run33():
    nn = 33
    print(nn)
    _topic = tifffile.imread(
        rf"/Users/yuanchen/Dropbox (HMS)/000 local remote sharing/20240714-deform-registration-crc/topic-img/C{nn:02}-topics.ome.tif"
    )
    assert (_topic > 0).sum(axis=0).max() == 1
    topic = (_topic > 0) * np.arange(len(_topic)).reshape(-1, 1, 1)
    topic = topic.sum(axis=0)

    # FIXME pad topic image
    topic = np.pad(topic, [(0, 1), (0, 1)])

    df = pd.read_csv(
        r"/Users/yuanchen/Dropbox (HMS)/000 local remote sharing/20240714-deform-registration-crc/img-data/C33-xy-moving-merged-mapped.csv.zip",
        index_col="CellID",
    )

    coord = df[["tY_centroid", "tX_centroid"]].values
    coord *= 0.325
    coord /= 100

    coord = np.floor(coord).astype("int")

    df["tTopic"] = topic[coord[:, 0], coord[:, 1]]
    df.to_csv(
        r"/Users/yuanchen/Dropbox (HMS)/000 local remote sharing/20240714-deform-registration-crc/img-data/C33-xy-moving-merged-mapped-topic.csv.zip",
        compression="zip",
    )


