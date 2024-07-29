import pathlib

import itk
import numpy as np
import tifffile
import skimage.transform
import matplotlib.pyplot as plt


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


def warp_moving(moving, elastix_tform_paths):
    elastix_parameter = itk.ParameterObject.New()
    for ff in elastix_tform_paths:
        elastix_parameter.AddParameterFile(str(ff))
    warpped_moving = itk.transformix_filter(
        moving, transform_parameter_object=elastix_parameter
    )
    return warpped_moving


def compare_deformed(
    ref_path,
    moving_path,
    elastix_tform_paths,
):
    ref = tifffile.imread(ref_path)
    moving = tifffile.imread(moving_path)

    warpped_moving = warp_moving(moving, elastix_tform_paths)
    # shape = elastix_parameter.GetParameterMap(0).get("Size")[::-1]
    # shape = np.array(shape, dtype="int")
    # deformation_field = itk.transformix_deformation_field(
    #     itk.GetImageFromArray(np.zeros(shape, dtype="uint8")), elastix_parameter
    # )
    print(f"{ncc(ref, moving):.4f} --> {ncc(ref, warpped_moving):.4f}")
    return (ncc(ref, moving), ncc(ref, warpped_moving))


def translate_moving(ref, moving, downscale_factor=1, plot=False):
    import palom
    import skimage.registration
    import skimage.transform
    import skimage.morphology
    import matplotlib.pyplot as plt

    moving = np.flipud(moving)
    moving = skimage.transform.warp(
        moving, np.eye(3), output_shape=ref.shape, preserve_range=True
    )

    if downscale_factor != 1:
        ref = palom.img_util.cv2_downscale_local_mean(ref, downscale_factor)
        moving = palom.img_util.cv2_downscale_local_mean(moving, downscale_factor)

    shift = skimage.registration.phase_cross_correlation(
        ref,
        moving,
        upsample_factor=downscale_factor,
        return_error=False,
        reference_mask=np.full_like(ref, 1, dtype="bool"),
        moving_mask=moving > 0,
    )

    if plot:
        import matplotlib.pyplot as plt

        _, axs = plt.subplots(1, 2, sharex=True, sharey=True)
        axs[0].imshow(ref)
        axs[1].imshow(
            skimage.transform.warp(
                moving,
                skimage.transform.AffineTransform(translation=shift[::-1]).inverse,
            )
        )
    return shift


elastix_dir = pathlib.Path(
    r"/Users/yuanchen/HMS Dropbox/Yu-An Chen/000 local remote sharing/20240714-deform-registration-crc/reg-param/tform"
)

case_number = range(1, 41)
results = []

for nn in case_number:
    print(f"C{nn:02}")
    ref_path = rf"/Users/yuanchen/HMS Dropbox/Yu-An Chen/000 local remote sharing/20240714-deform-registration-crc/img-data/C{nn:02}-ref.tif"
    moving_ori_path = rf"/Users/yuanchen/HMS Dropbox/Yu-An Chen/000 local remote sharing/20240714-deform-registration-crc/img-data/C{nn:02}-moving-ori.tif"
    img0 = tifffile.imread(ref_path)
    img1 = tifffile.imread(moving_ori_path)
    shift = 4 * np.array(translate_moving(img0, img1, 4))
    img2 = skimage.transform.warp(
        np.flipud(img1),
        skimage.transform.AffineTransform(translation=shift[::-1]).inverse,
        output_shape=img0.shape,
        preserve_range=True,
    ).astype("uint16")
    img1 = skimage.transform.warp(
        np.flipud(img1),
        np.eye(3),
        output_shape=img0.shape,
        preserve_range=True,
    ).astype("uint16")

    moving_path = rf"/Users/yuanchen/HMS Dropbox/Yu-An Chen/000 local remote sharing/20240714-deform-registration-crc/img-data/C{nn:02}-moving.tif"
    elastix_tform_paths = [
        elastix_dir / f"C{nn:02}-tform-elastix-param-0.txt",
        elastix_dir / f"C{nn:02}-tform-elastix-param-1.txt",
    ]
    img3 = tifffile.imread(moving_path)
    img4 = warp_moving(img3, elastix_tform_paths)

    results.append([ncc(img0, ii) for ii in [img1, img2, img3, img4]])

results = np.array(results)

# ---------------------------------------------------------------------------- #
#                               for presentation                               #
# ---------------------------------------------------------------------------- #

plt.figure()
plt.plot(results.T[:, :-2], c="#555555", alpha=0.1)
plt.plot(results.T[:, -2:-1], c="#555555", alpha=0.1, label="C01 - C39")
plt.plot(results.T[:, -1:], c="#555555", alpha=0.8, label="C40")
_ = plt.boxplot(
    results,
    positions=range(4),
    widths=0.2,
    tick_labels=["No registration", "Translation", "Affine", "Non-linear"],
)
plt.ylabel("Normalized cross correlation coefficient")
plt.legend()

import pandas as pd

df = pd.DataFrame(
    results,
    index=[f"C{nn:02}" for nn in case_number],
    columns=["No registration", "Translation", "Affine", "Non-linear"],
)

imgs = []
for nn in [40]:
    print(f"C{nn:02}")
    ref_path = rf"/Users/yuanchen/HMS Dropbox/Yu-An Chen/000 local remote sharing/20240714-deform-registration-crc/img-data/C{nn:02}-ref.tif"
    moving_ori_path = rf"/Users/yuanchen/HMS Dropbox/Yu-An Chen/000 local remote sharing/20240714-deform-registration-crc/img-data/C{nn:02}-moving-ori.tif"
    img0 = tifffile.imread(ref_path)
    img1 = tifffile.imread(moving_ori_path)
    shift = 4 * np.array(translate_moving(img0, img1, 4))
    img2 = skimage.transform.warp(
        np.flipud(img1),
        skimage.transform.AffineTransform(translation=shift[::-1]).inverse,
        output_shape=img0.shape,
        preserve_range=True,
    ).astype("uint16")
    img1 = skimage.transform.warp(
        np.flipud(img1),
        np.eye(3),
        output_shape=img0.shape,
        preserve_range=True,
    ).astype("uint16")

    moving_path = rf"/Users/yuanchen/HMS Dropbox/Yu-An Chen/000 local remote sharing/20240714-deform-registration-crc/img-data/C{nn:02}-moving.tif"
    elastix_tform_paths = [
        elastix_dir / f"C{nn:02}-tform-elastix-param-0.txt",
        elastix_dir / f"C{nn:02}-tform-elastix-param-1.txt",
    ]
    img3 = tifffile.imread(moving_path)
    img4 = warp_moving(img3, elastix_tform_paths)
    imgs.append([img0, img1, img2, img3, img4])

import palom

palom.register.feature_based_registration(
    palom.img_util.cv2_downscale_local_mean(img0, 4),
    palom.img_util.cv2_downscale_local_mean(img1, 4),
    plot_match_result=True,
    auto_mask=True,
    n_keypoints=1500,
)


elastix_parameter = itk.ParameterObject.New()
for ff in elastix_tform_paths:
    elastix_parameter.AddParameterFile(str(ff))
shape = elastix_parameter.GetParameterMap(0).get("Size")[::-1]
shape = np.array(shape, dtype="int")
deformation_field = itk.transformix_deformation_field(
    itk.GetImageFromArray(np.zeros(shape, dtype="uint8")), elastix_parameter
)

inverted_fixed_point = itk.FixedPointInverseDisplacementFieldImageFilter(
    deformation_field,
    NumberOfIterations=10,
    Size=deformation_field.shape[:2][::-1],
)
dx, dy = np.moveaxis(inverted_fixed_point, 2, 0)

_, ax = plt.subplots()
ax.imshow(np.log1p(img3), cmap="gray", vmin=3, vmax=15)
nvec = 40  # Number of vectors to be displayed along each image dimension
nl, nc = shape
step = max(nl // nvec, nc // nvec)

y, x = np.mgrid[:nl:step, :nc:step]
dx_ = dx[::step, ::step]
dy_ = dy[::step, ::step]

ax.quiver(
    x,
    y,
    dx_,
    dy_,
    color="deepskyblue",
    units="xy",
    angles="xy",
    scale_units="xy",
    scale=1 / 7,
)
ax.set_axis_off()


df40 = pd.read_csv(
    "/Users/yuanchen/Dropbox (HMS)/000 local remote sharing/20240714-deform-registration-crc/img-data/C40-xy-moving-mapped-topic.csv.zip"
)
plt.figure()
plt.imshow([[0]])
plt.scatter(
    *df40[["tX_centroid", "tY_centroid"]].values.T,
    s=1,
    lw=0,
    alpha=0.05,
    c=df40["tTopic"],
    cmap="Set3",
    vmin=1,
    vmax=12,
)
plt.gca().axis("off")
plt.gcf().patch.set_facecolor("black")

plt.figure()
plt.imshow(np.arange(1, 13).reshape(-1, 1), cmap="Set3", vmin=1, vmax=12)
plt.gca().set_xticks([])
plt.gca().set_yticks(range(12), [f"Topic {i}" for i in range(1, 13)])
