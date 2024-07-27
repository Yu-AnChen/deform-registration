import pandas as pd

df331 = pd.read_csv(
    "/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C33-xy-moving-mapped.csv.zip",
    index_col="CellID",
)

df332 = pd.read_csv(
    "/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C332-xy-moving-mapped.csv.zip",
    index_col="CellID",
)

df332.loc[df332["tX_centroid"] > 0, "tX_centroid"] += 36923
df331.loc[df332["tX_centroid"] > 0, :] = df332.query("tX_centroid>0")

df331.to_csv('/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C33-xy-moving-merged-mapped.csv.zip')