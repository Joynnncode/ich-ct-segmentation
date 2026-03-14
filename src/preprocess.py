# -*- coding: utf-8 -*-
"""Preprocess.py
Huanxin_Chen

"""



from __future__ import annotations

from typing import Optional, Sequence, Tuple

import numpy as np


ArrayLike = np.ndarray


def normalize_minmax(image: ArrayLike) -> ArrayLike:
    """
    Scale an image to the range [0, 1].

    Parameters
    ----------
    image : np.ndarray
        Input image array.

    Returns
    -------
    np.ndarray
        Min-max normalised image.
    """
    image = np.asarray(image, dtype=np.float32)
    img_min = np.min(image)
    img_max = np.max(image)

    if np.isclose(img_max, img_min):
        return np.zeros_like(image, dtype=np.float32)

    return (image - img_min) / (img_max - img_min)


def zscore_normalize(image: ArrayLike) -> ArrayLike:
    """
    Apply z-score normalisation.

    Parameters
    ----------
    image : np.ndarray
        Input image array.

    Returns
    -------
    np.ndarray
        Z-score normalised image.
    """
    image = np.asarray(image, dtype=np.float32)
    mean = np.mean(image)
    std = np.std(image)

    if np.isclose(std, 0.0):
        return np.zeros_like(image, dtype=np.float32)

    return (image - mean) / std


def clip_intensity(
    image: ArrayLike,
    lower: float = 0.5,
    upper: float = 99.5,
) -> ArrayLike:
    """
    Clip image intensities using percentile thresholds.

    Parameters
    ----------
    image : np.ndarray
        Input image.
    lower : float
        Lower percentile.
    upper : float
        Upper percentile.

    Returns
    -------
    np.ndarray
        Clipped image.
    """
    image = np.asarray(image, dtype=np.float32)

    if lower < 0 or upper > 100 or lower >= upper:
        raise ValueError("Percentile values must satisfy 0 <= lower < upper <= 100.")

    lo = np.percentile(image, lower)
    hi = np.percentile(image, upper)
    return np.clip(image, lo, hi)


def window_and_normalize(
    image: ArrayLike,
    window_center: float = 40.0,
    window_width: float = 80.0,
) -> ArrayLike:
    """
    Apply a CT-style intensity window, then min-max normalise to [0, 1].

    Parameters
    ----------
    image : np.ndarray
        Input image.
    window_center : float
        Window centre.
    window_width : float
        Window width.

    Returns
    -------
    np.ndarray
        Windowed and normalised image.
    """
    image = np.asarray(image, dtype=np.float32)
    lower = window_center - window_width / 2.0
    upper = window_center + window_width / 2.0
    windowed = np.clip(image, lower, upper)
    return normalize_minmax(windowed)


def crop_center(
    image: ArrayLike,
    crop_size: Sequence[int],
) -> ArrayLike:
    """
    Crop the centre region of a 2D or 3D image.

    Parameters
    ----------
    image : np.ndarray
        2D or 3D image.
    crop_size : sequence of int
        Desired crop size. Must match image ndim.

    Returns
    -------
    np.ndarray
        Centre crop.

    Raises
    ------
    ValueError
        If crop size dimensionality is invalid or too large.
    """
    image = np.asarray(image)
    crop_size = tuple(int(x) for x in crop_size)

    if image.ndim != len(crop_size):
        raise ValueError("crop_size must have the same number of dimensions as image.")

    for dim, crop in zip(image.shape, crop_size):
        if crop > dim:
            raise ValueError("crop_size cannot exceed image dimensions.")

    starts = [(dim - crop) // 2 for dim, crop in zip(image.shape, crop_size)]
    ends = [start + crop for start, crop in zip(starts, crop_size)]
    slices = tuple(slice(start, end) for start, end in zip(starts, ends))

    return image[slices]


def crop_to_bounding_box(
    image: ArrayLike,
    mask: ArrayLike,
    margin: int = 5,
) -> Tuple[ArrayLike, ArrayLike]:
    """
    Crop image and mask around the non-zero region of the mask.

    Parameters
    ----------
    image : np.ndarray
        Input image.
    mask : np.ndarray
        Binary or non-zero mask with same shape as image.
    margin : int
        Extra padding around the bounding box.

    Returns
    -------
    (np.ndarray, np.ndarray)
        Cropped image and cropped mask.

    Raises
    ------
    ValueError
        If image and mask shapes differ.
    """
    image = np.asarray(image)
    mask = np.asarray(mask)

    if image.shape != mask.shape:
        raise ValueError("image and mask must have the same shape.")

    coords = np.argwhere(mask > 0)
    if coords.size == 0:
        return image.copy(), mask.copy()

    mins = np.maximum(coords.min(axis=0) - margin, 0)
    maxs = np.minimum(coords.max(axis=0) + margin + 1, image.shape)

    slices = tuple(slice(int(lo), int(hi)) for lo, hi in zip(mins, maxs))
    return image[slices], mask[slices]


def resize_nearest_2d(
    image: ArrayLike,
    output_shape: Tuple[int, int],
) -> ArrayLike:
    """
    Resize a 2D image using nearest-neighbour sampling only with NumPy.

    This is intended as a lightweight demonstration utility.

    Parameters
    ----------
    image : np.ndarray
        2D input image.
    output_shape : tuple[int, int]
        Target (height, width).

    Returns
    -------
    np.ndarray
        Resized image.
    """
    image = np.asarray(image)
    if image.ndim != 2:
        raise ValueError("resize_nearest_2d expects a 2D image.")

    out_h, out_w = output_shape
    if out_h <= 0 or out_w <= 0:
        raise ValueError("output_shape values must be positive.")

    in_h, in_w = image.shape
    row_idx = np.linspace(0, in_h - 1, out_h).round().astype(int)
    col_idx = np.linspace(0, in_w - 1, out_w).round().astype(int)

    return image[row_idx][:, col_idx]


def create_synthetic_ct_slice(
    shape: Tuple[int, int] = (256, 256),
    lesion_center: Tuple[int, int] = (128, 128),
    lesion_radius: int = 18,
    seed: Optional[int] = 42,
) -> ArrayLike:
    """
    Create a synthetic CT-like slice for demonstration.

    Parameters
    ----------
    shape : tuple[int, int]
        Output image shape.
    lesion_center : tuple[int, int]
        Centre of synthetic bright lesion.
    lesion_radius : int
        Radius of circular lesion.
    seed : int | None
        Random seed.

    Returns
    -------
    np.ndarray
        Synthetic image.
    """
    if seed is not None:
        np.random.seed(seed)

    image = np.random.normal(loc=35, scale=18, size=shape).astype(np.float32)

    yy, xx = np.ogrid[:shape[0], :shape[1]]
    cy, cx = lesion_center
    lesion = (yy - cy) ** 2 + (xx - cx) ** 2 <= lesion_radius ** 2

    image[lesion] += 45.0
    return image
