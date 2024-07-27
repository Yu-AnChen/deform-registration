import pathlib

import itk
import numpy as np
import tifffile
import napari


def _ncc(img1, img2):
    return np.sum(img1.astype("float") * img2.astype("float")) / (
        np.linalg.norm(img1) * np.linalg.norm(img2)
    )

# comparison of cross correlation and normalized dot product
# https://xcdskd.readthedocs.io/en/latest/cross_correlation/cross_correlation_coefficient.html
def norm_dot(img1, img2):
    """
    return normalized dot product of the arrays img1, img2
    """
    # make 1D value lists
    v1 = np.ravel(img1)
    v2 = np.ravel(img2)

    # get the norms of the vectors
    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)
    # print('norms of NDP vectors: ', norm1, norm2)

    ndot = np.dot(v1 / norm1, v2 / norm2)
    return ndot


def norm_data(data):
    """
    normalize data to have mean=0 and standard_deviation=1P
    """
    mean_data = np.mean(data)
    std_data = np.std(data, ddof=1)
    # return (data-mean_data)/(std_data*np.sqrt(data.size-1))
    return (data - mean_data) / (std_data)


def ncc(data0, data1):
    """
    normalized cross-correlation coefficient between two data sets

    Parameters
    ----------
    data0, data1 :  numpy arrays of same size
    """
    return (1.0 / (data0.size - 1)) * np.sum(norm_data(data0) * norm_data(data1))


def compare_deformed(
    ref_path,
    moving_path,
    elastix_tform_paths,
):
    ref = tifffile.imread(ref_path)
    moving = tifffile.imread(moving_path)

    elastix_parameter = itk.ParameterObject.New()
    for ff in elastix_tform_paths:
        elastix_parameter.AddParameterFile(str(ff))
    warpped_moving = itk.transformix_filter(
        moving, transform_parameter_object=elastix_parameter
    )
    # shape = elastix_parameter.GetParameterMap(0).get("Size")[::-1]
    # shape = np.array(shape, dtype="int")
    # deformation_field = itk.transformix_deformation_field(
    #     itk.GetImageFromArray(np.zeros(shape, dtype="uint8")), elastix_parameter
    # )

    print(f"{ncc(ref, moving):.4f} --> {ncc(ref, warpped_moving):.4f}")
    print(f"{_ncc(ref, moving):.4f} --> {_ncc(ref, warpped_moving):.4f}")

    napari_kwargs = dict(blending="additive", visible=False, name=f"C{nn:02}")
    v.add_image(ref, colormap="bop blue", visible=False, name=f"C{nn:02}")
    v.add_image(moving, colormap="bop purple", **napari_kwargs)
    v.add_image(warpped_moving, colormap="bop orange", **napari_kwargs)


elastix_dir = pathlib.Path(
    r"/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/reg-param/tform"
)

v = napari.Viewer()

case_number = range(20, 30)

for nn in case_number:
    print(f"C{nn:02}")
    ref_path = rf"/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C{nn:02}-ref.tif"
    moving_path = rf"/Users/yuanchen/HMS Dropbox/000 local remote sharing/20240714-deform-registration-crc/img-data/C{nn:02}-moving.tif"
    elastix_paths = [
        elastix_dir / f"C{nn:02}-tform-elastix-param-0.txt",
        elastix_dir / f"C{nn:02}-tform-elastix-param-1.txt",
    ]
    compare_deformed(ref_path, moving_path, elastix_paths)
