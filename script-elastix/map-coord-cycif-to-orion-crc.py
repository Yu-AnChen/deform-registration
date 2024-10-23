import skimage.transform
import itk
import numpy as np
import pathlib
import pandas as pd


def map_moving_points(points_xy, param_obj):
    return _map_points(points_xy, param_obj, is_from_moving=True)


def map_fixed_points(points_xy, param_obj):
    return _map_points(points_xy, param_obj, is_from_moving=False)


def _map_points(points_xy, param_obj, is_from_moving=True):
    import scipy.ndimage as ndi

    points = np.asarray(points_xy)
    assert points.shape[1] == 2
    assert points.ndim == 2

    shape = param_obj.GetParameterMap(0).get("Size")[::-1]
    shape = np.array(shape, dtype="int")

    deformation_field = itk.transformix_deformation_field(
        itk.GetImageFromArray(np.zeros(shape, dtype="uint8")), param_obj
    )
    dx, dy = np.moveaxis(deformation_field, 2, 0)

    if is_from_moving:
        inverted_fixed_point = itk.FixedPointInverseDisplacementFieldImageFilter(
            deformation_field,
            NumberOfIterations=10,
            Size=deformation_field.shape[:2][::-1],
        )
        dx, dy = np.moveaxis(inverted_fixed_point, 2, 0)

    my, mx = np.mgrid[: shape[0], : shape[1]].astype("float32")

    mapped_points_xy = np.vstack(
        [
            ndi.map_coordinates(mx + dx, np.fliplr(points).T),
            ndi.map_coordinates(my + dy, np.fliplr(points).T),
        ]
    ).T
    return mapped_points_xy


affine_dir = pathlib.Path(
    r"/Users/yuanchen/HMS Dropbox/Yu-An Chen/000 local remote sharing/20240714-deform-registration-crc/img-data"
)

affine_paths = r"""
C17-affine-matrix.csv
C18-affine-matrix.csv
C19-affine-matrix.csv
C20-affine-matrix.csv
C21-affine-matrix.csv
C22-affine-matrix.csv
C23-affine-matrix.csv
C24-affine-matrix.csv
C25-affine-matrix.csv
C26-affine-matrix.csv
C27-affine-matrix.csv
C28-affine-matrix.csv
C29-affine-matrix.csv
C30-affine-matrix.csv
C31-affine-matrix.csv
C32-affine-matrix.csv
C33-affine-matrix.csv
C332-affine-matrix.csv
C34-affine-matrix.csv
C35-affine-matrix.csv
C36-affine-matrix.csv
C37-affine-matrix.csv
C38-affine-matrix.csv
C39-affine-matrix.csv
C40-affine-matrix.csv
"""
affine_paths = """
C01-affine-matrix.csv
C02-affine-matrix.csv
C03-affine-matrix.csv
C04-affine-matrix.csv
C05-affine-matrix.csv
C06-affine-matrix.csv
C07-affine-matrix.csv
C08-affine-matrix.csv
C09-affine-matrix.csv
C10-affine-matrix.csv
C11-affine-matrix.csv
C12-affine-matrix.csv
C13-affine-matrix.csv
C14-affine-matrix.csv
C15-affine-matrix.csv
C16-affine-matrix.csv
"""
affine_paths = """
immune-C01-affine-matrix.csv
immune-C02-affine-matrix.csv
immune-C03-affine-matrix.csv
immune-C04-affine-matrix.csv
immune-C05-affine-matrix.csv
immune-C06-affine-matrix.csv
immune-C07-affine-matrix.csv
immune-C08-affine-matrix.csv
immune-C09-affine-matrix.csv
immune-C10-affine-matrix.csv
immune-C11-affine-matrix.csv
immune-C12-affine-matrix.csv
immune-C13-affine-matrix.csv
immune-C14-affine-matrix.csv
immune-C15-affine-matrix.csv
immune-C16-affine-matrix.csv
"""
affine_paths = [affine_dir / pp for pp in affine_paths.strip().split("\n")]

elastix_dir = pathlib.Path(
    r"/Users/yuanchen/HMS Dropbox/Yu-An Chen/000 local remote sharing/20240714-deform-registration-crc/reg-param/tform"
)

elastix_paths = r"""
C17-tform-elastix-param-0.txt;C17-tform-elastix-param-1.txt
C18-tform-elastix-param-0.txt;C18-tform-elastix-param-1.txt
C19-tform-elastix-param-0.txt;C19-tform-elastix-param-1.txt
C20-tform-elastix-param-0.txt;C20-tform-elastix-param-1.txt
C21-tform-elastix-param-0.txt;C21-tform-elastix-param-1.txt
C22-tform-elastix-param-0.txt;C22-tform-elastix-param-1.txt
C23-tform-elastix-param-0.txt;C23-tform-elastix-param-1.txt
C24-tform-elastix-param-0.txt;C24-tform-elastix-param-1.txt
C25-tform-elastix-param-0.txt;C25-tform-elastix-param-1.txt
C26-tform-elastix-param-0.txt;C26-tform-elastix-param-1.txt
C27-tform-elastix-param-0.txt;C27-tform-elastix-param-1.txt
C28-tform-elastix-param-0.txt;C28-tform-elastix-param-1.txt
C29-tform-elastix-param-0.txt;C29-tform-elastix-param-1.txt
C30-tform-elastix-param-0.txt;C30-tform-elastix-param-1.txt
C31-tform-elastix-param-0.txt;C31-tform-elastix-param-1.txt
C32-tform-elastix-param-0.txt;C32-tform-elastix-param-1.txt
C33-tform-elastix-param-0.txt;C33-tform-elastix-param-1.txt
C332-tform-elastix-param-0.txt;C332-tform-elastix-param-1.txt
C34-tform-elastix-param-0.txt;C34-tform-elastix-param-1.txt
C35-tform-elastix-param-0.txt;C35-tform-elastix-param-1.txt
C36-tform-elastix-param-0.txt;C36-tform-elastix-param-1.txt
C37-tform-elastix-param-0.txt;C37-tform-elastix-param-1.txt
C38-tform-elastix-param-0.txt;C38-tform-elastix-param-1.txt
C39-tform-elastix-param-0.txt;C39-tform-elastix-param-1.txt
C40-tform-elastix-param-0.txt;C40-tform-elastix-param-1.txt
"""
elastix_paths = """
C01-tform-elastix-param-0.txt;C01-tform-elastix-param-1.txt
C02-tform-elastix-param-0.txt;C02-tform-elastix-param-1.txt
C03-tform-elastix-param-0.txt;C03-tform-elastix-param-1.txt
C04-tform-elastix-param-0.txt;C04-tform-elastix-param-1.txt
C05-tform-elastix-param-0.txt;C05-tform-elastix-param-1.txt
C06-tform-elastix-param-0.txt;C06-tform-elastix-param-1.txt
C07-tform-elastix-param-0.txt;C07-tform-elastix-param-1.txt
C08-tform-elastix-param-0.txt;C08-tform-elastix-param-1.txt
C09-tform-elastix-param-0.txt;C09-tform-elastix-param-1.txt
C10-tform-elastix-param-0.txt;C10-tform-elastix-param-1.txt
C11-tform-elastix-param-0.txt;C11-tform-elastix-param-1.txt
C12-tform-elastix-param-0.txt;C12-tform-elastix-param-1.txt
C13-tform-elastix-param-0.txt;C13-tform-elastix-param-1.txt
C14-tform-elastix-param-0.txt;C14-tform-elastix-param-1.txt
C15-tform-elastix-param-0.txt;C15-tform-elastix-param-1.txt
C16-tform-elastix-param-0.txt;C16-tform-elastix-param-1.txt
"""
elastix_paths = """
immune-C01-tform-elastix-param-0.txt;immune-C01-tform-elastix-param-1.txt
immune-C02-tform-elastix-param-0.txt;immune-C02-tform-elastix-param-1.txt
immune-C03-tform-elastix-param-0.txt;immune-C03-tform-elastix-param-1.txt
immune-C04-tform-elastix-param-0.txt;immune-C04-tform-elastix-param-1.txt
immune-C05-tform-elastix-param-0.txt;immune-C05-tform-elastix-param-1.txt
immune-C06-tform-elastix-param-0.txt;immune-C06-tform-elastix-param-1.txt
immune-C07-tform-elastix-param-0.txt;immune-C07-tform-elastix-param-1.txt
immune-C08-tform-elastix-param-0.txt;immune-C08-tform-elastix-param-1.txt
immune-C09-tform-elastix-param-0.txt;immune-C09-tform-elastix-param-1.txt
immune-C10-tform-elastix-param-0.txt;immune-C10-tform-elastix-param-1.txt
immune-C11-tform-elastix-param-0.txt;immune-C11-tform-elastix-param-1.txt
immune-C12-tform-elastix-param-0.txt;immune-C12-tform-elastix-param-1.txt
immune-C13-tform-elastix-param-0.txt;immune-C13-tform-elastix-param-1.txt
immune-C14-tform-elastix-param-0.txt;immune-C14-tform-elastix-param-1.txt
immune-C15-tform-elastix-param-0.txt;immune-C15-tform-elastix-param-1.txt
immune-C16-tform-elastix-param-0.txt;immune-C16-tform-elastix-param-1.txt
"""
elastix_paths = [
    [elastix_dir / ppp for ppp in pp.split(";")]
    for pp in elastix_paths.strip().split("\n")
]

coords_dir = pathlib.Path(
    r"/Users/yuanchen/HMS Dropbox/Yu-An Chen/000 local remote sharing/20240714-deform-registration-crc/img-data"
)
coords_paths = """
C17-xy-moving.csv.zip
C18-xy-moving.csv.zip
C19-xy-moving.csv.zip
C20-xy-moving.csv.zip
C21-xy-moving.csv.zip
C22-xy-moving.csv.zip
C23-xy-moving.csv.zip
C24-xy-moving.csv.zip
C25-xy-moving.csv.zip
C26-xy-moving.csv.zip
C27-xy-moving.csv.zip
C28-xy-moving.csv.zip
C29-xy-moving.csv.zip
C30-xy-moving.csv.zip
C31-xy-moving.csv.zip
C32-xy-moving.csv.zip
C33-xy-moving.csv.zip
C332-xy-moving.csv.zip
C34-xy-moving.csv.zip
C35-xy-moving.csv.zip
C36-xy-moving.csv.zip
C37-xy-moving.csv.zip
C38-xy-moving.csv.zip
C39-xy-moving.csv.zip
C40-xy-moving.csv.zip
"""
coords_paths = """
TNPCRC_01_cellRing.csv.zip
TNPCRC_02_cellRing.csv.zip
TNPCRC_03_cellRing.csv.zip
TNPCRC_04_cellRing.csv.zip
TNPCRC_05_cellRing.csv.zip
TNPCRC_06_cellRing.csv.zip
TNPCRC_08_cellRing.csv.zip
TNPCRC_09_cellRing.csv.zip
TNPCRC_10_cellRing.csv.zip
TNPCRC_11_cellRing.csv.zip
TNPCRC_12_cellRing.csv.zip
TNPCRC_13_cellRing.csv.zip
TNPCRC_14_cellRing.csv.zip
TNPCRC_15_cellRing.csv.zip
TNPCRC_16_cellRing.csv.zip
TNPCRC_17_cellRing.csv.zip
"""
coords_paths = """
immune-TNPCRC_01_cellRing.csv.zip
immune-TNPCRC_02_cellRing.csv.zip
immune-TNPCRC_03_cellRing.csv.zip
immune-TNPCRC_04_cellRing.csv.zip
immune-TNPCRC_05_cellRing.csv.zip
immune-TNPCRC_06_cellRing.csv.zip
immune-TNPCRC_08_cellRing.csv.zip
immune-TNPCRC_09_cellRing.csv.zip
immune-TNPCRC_10_cellRing.csv.zip
immune-TNPCRC_11_cellRing.csv.zip
immune-TNPCRC_12_cellRing.csv.zip
immune-TNPCRC_13_cellRing.csv.zip
immune-TNPCRC_14_cellRing.csv.zip
immune-TNPCRC_15_cellRing.csv.zip
immune-TNPCRC_16_cellRing.csv.zip
immune-TNPCRC_17_cellRing.csv.zip
"""
coords_paths = [coords_dir / pp for pp in coords_paths.strip().split("\n")]


def process_coordniate_file(
    coord_file_path: str | pathlib.Path,
    elastix_tform_paths: list,
    affine_before: skimage.transform.AffineTransform = None,
    affine_after: skimage.transform.AffineTransform = None,
):
    df = pd.read_csv(
        coord_file_path,
        usecols=["CellID", "X_centroid", "Y_centroid"],
        index_col="CellID",
    )
    df_coord = df[["X_centroid", "Y_centroid"]]

    elastix_parameter = itk.ParameterObject.New()
    for ff in elastix_tform_paths:
        elastix_parameter.AddParameterFile(str(ff))

    if affine_before is not None:
        df_coord[["X_centroid", "Y_centroid"]] = affine_before(df_coord.values)
    deform_points = map_moving_points(df_coord.values, elastix_parameter)
    if affine_after is not None:
        deform_points = affine_after(deform_points)
    df_coord[["X_centroid", "Y_centroid"]] = deform_points
    return df_coord


Affine = skimage.transform.AffineTransform
tform1 = Affine(scale=(1 / 2**4,) * 2)
# tform2 = Affine(matrix='')
tform3 = Affine(scale=(2**5,) * 2)

for csv, aa, ee in zip(coords_paths[:], affine_paths[:], elastix_paths[:]):
    print(csv.name)
    tform_before = tform1 + Affine(matrix=np.loadtxt(aa, delimiter=","))
    tform_after = tform3
    process_coordniate_file(
        csv, ee, affine_before=tform_before, affine_after=tform_after
    ).rename(columns=lambda x: f"t{x}").to_csv(
        csv.parent
        / csv.name.replace("-moving.csv.zip", "-moving-mapped.csv.zip").replace(
            "_cellRing.csv.zip", "_cellRing-mapped.csv.zip"
        )
    )
