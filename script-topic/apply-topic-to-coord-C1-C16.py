import tifffile
import numpy as np
import pandas as pd


case_number = range(1, 17)
old_case_number = list(range(1, 18))
old_case_number.pop(6)

for nn, nno in zip(case_number, old_case_number):
    print(nn)
    _topic = tifffile.imread(
        rf"/Users/yuanchen/HMS Dropbox/Yu-An Chen/000 local remote sharing/20240714-deform-registration-crc/topic-img/C{nn:02}-topics.ome.tif"
    )
    assert (_topic > 0).sum(axis=0).max() == 1
    topic = (_topic > 0) * np.arange(len(_topic)).reshape(-1, 1, 1)
    topic = topic.sum(axis=0)

    # FIXME pad topic image
    topic = np.pad(topic, [(0, 100), (0, 100)], constant_values=-1)

    df = pd.read_csv(
        rf"/Users/yuanchen/HMS Dropbox/Yu-An Chen/000 local remote sharing/20240714-deform-registration-crc/img-data/TNPCRC_{nno:02}_cellRing-mapped.csv.zip",
        index_col="CellID",
    )

    coord = df[["tY_centroid", "tX_centroid"]].values
    coord *= 0.325
    coord /= 100

    coord = np.floor(coord).astype("int")

    df["tTopic"] = topic[coord[:, 0], coord[:, 1]]
    df.to_csv(
        rf"/Users/yuanchen/HMS Dropbox/Yu-An Chen/000 local remote sharing/20240714-deform-registration-crc/img-data/TNPCRC_{nno:02}_cellRing-mapped-topic.csv.zip",
        compression="zip",
    )
