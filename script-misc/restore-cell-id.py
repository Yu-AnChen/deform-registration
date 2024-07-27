import pathlib
import pandas as pd


mcmicro_paths = r"""
Z:\JL503_JERRY\221-CRC_ORION-2022APR\mcmicro\LSP10532\quantification\LSP10532--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\mcmicro\LSP10543\quantification\LSP10543--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\mcmicro\LSP10554\quantification\LSP10554--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\mcmicro\LSP10566\quantification\LSP10566--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\mcmicro\LSP10576\quantification\LSP10576--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\mcmicro\LSP10587\quantification\LSP10587--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\mcmicro\LSP10598\quantification\LSP10598--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\mcmicro\LSP10609\quantification\LSP10609--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\mcmicro\LSP10621\quantification\LSP10621--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\mcmicro\LSP10631\quantification\LSP10631--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\mcmicro\LSP10642\quantification\LSP10642--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\mcmicro\LSP10653\quantification\LSP10653--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\input2\LSP10664\quantification\LSP10664--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\input2\LSP10675\quantification\LSP10675--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\input2\LSP10687\quantification\LSP10687--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\input2\LSP10697\quantification\LSP10697--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\input2\LSP10708\quantification\LSP10708--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\input2\LSP10719\quantification\LSP10719--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\input2\LSP10730\quantification\LSP10730--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\input2\LSP10741\quantification\LSP10741--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\input2\LSP10752\quantification\LSP10752--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\input2\LSP10763\quantification\LSP10763--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\input2\LSP10774\quantification\LSP10774--unmicst_cellRing.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\input2\LSP10790\quantification\LSP10790--unmicst_cellRing.csv
""".strip().split("\n")

cylinter_paths = r"""
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10532.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10543.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10554.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10566.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10576.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10587.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10598.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10609.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10621.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10631.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10642.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10653.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10664.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10675.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10687.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10697.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10708.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10719.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10730.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10741.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10752.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10763.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10774.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10790.csv
""".strip().split("\n")

case_number = list(range(17, 41))
out_dir = r"C:\Users\yc296\Downloads\test-elastix-img-pair"

out_paths = [
    pathlib.Path(out_dir) / f"C{nn:02}-xy-moving.csv.zip" for nn in case_number
]


def restore_cell_id(p_ori, p_mod, out_path):
    df_ori = pd.read_csv(p_ori, usecols=["CellID", "X_centroid", "Y_centroid"])
    df_mod = pd.read_csv(p_mod, usecols=["X_centroid", "Y_centroid"])

    df_ori[["XX", "YY"]] = df_ori[["X_centroid", "Y_centroid"]].round().astype("int")
    df_mod[["XX", "YY"]] = df_mod[["X_centroid", "Y_centroid"]].round().astype("int")

    df_ori.set_index(["XX", "YY"], inplace=True)
    df_mod.set_index(["XX", "YY"], inplace=True)

    df_out = df_ori.loc[df_mod.index]
    if df_out.shape[0] != df_mod.shape[0]:
        print(
            pathlib.Path(p_mod).name,
            df_mod.shape[0],
            pathlib.Path(p_ori).name,
            df_out.shape[0],
        )
    df_out.to_csv(out_path, compression="zip", index=False)


for p1, p2, oo in zip(mcmicro_paths[:1], cylinter_paths, out_paths):
    restore_cell_id(p1, p2, oo)


from joblib import Parallel, delayed  # noqa: E402


Parallel(n_jobs=3, verbose=1)(
    delayed(restore_cell_id)(p1, p2, oo)
    for p1, p2, oo in zip(mcmicro_paths[1:], cylinter_paths[1:], out_paths[1:])
)


# ---------------------------------------------------------------------------- #
#                       Add the cylinter id (LSPID_index)                      #
#                  because Jerry's matlab code also drop cells                 #
# ---------------------------------------------------------------------------- #
import pathlib
import pandas as pd


cylinter_paths = r"""
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10532.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10543.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10554.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10566.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10576.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10587.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10598.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10609.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10621.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10631.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10642.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output\LSP10653.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10664.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10675.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10687.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10697.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10708.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10719.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10730.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10741.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10752.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10763.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10774.csv
Z:\JL503_JERRY\221-CRC_ORION-2022APR\cylinter_output_2\LSP10790.csv
""".strip().split("\n")


case_number = list(range(17, 41))
out_dir = r"C:\Users\yc296\Downloads\test-elastix-img-pair"

out_paths = [
    pathlib.Path(out_dir) / f"C{nn:02}-cylinter-id-moving.csv.zip" for nn in case_number
]

for pp, oo in zip(cylinter_paths, out_paths):
    df = pd.read_csv(pp, usecols=[0]).rename(columns={"Unnamed: 0": "CylinterID"})
    df.to_csv(oo, compression="zip", index=False)


def wrap(inpath, outpath):
    df = pd.read_csv(inpath, usecols=[0]).rename(columns={"Unnamed: 0": "CylinterID"})
    df.to_csv(outpath, compression="zip", index=False)


from joblib import Parallel, delayed  # noqa: E402


Parallel(n_jobs=4, verbose=1)(
    delayed(wrap)(pp, oo) for pp, oo in zip(cylinter_paths, out_paths)
)




id_paths = """
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C17-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C18-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C19-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C20-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C21-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C22-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C23-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C24-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C25-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C26-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C27-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C28-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C29-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C30-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C31-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C32-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C33-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C34-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C35-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C36-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C37-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C38-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C39-cylinter-id-moving.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C40-cylinter-id-moving.csv.zip
""".strip().split("\n")

topic_paths = """
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C17-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C18-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C19-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C20-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C21-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C22-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C23-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C24-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C25-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C26-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C27-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C28-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C29-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C30-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C31-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C32-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C33-xy-moving-merged-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C34-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C35-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C36-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C37-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C38-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C39-xy-moving-mapped-topic.csv.zip
/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C40-xy-moving-mapped-topic.csv.zip
""".strip().split("\n")


for pt, pi in zip(topic_paths, id_paths):
    df1 = pd.read_csv(pt)
    df2 = pd.read_csv(pi)
    assert len(df1) == len(df2)
    df1["CylinterID"] = df2["CylinterID"]
    df1.to_csv(pt, index=False, compression="zip")