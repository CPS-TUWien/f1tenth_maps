# ---------------------------------------------------------------------------------------------------------------------
# Author (original Version): Thomas Pintaric (thomas.pintaric@gmail.com)
# Author (modified Version): Andreas Brandstaetter
# SPDX-License-Identifier: GPL-3.0-or-later
# ---------------------------------------------------------------------------------------------------------------------

import os
import argparse
import yaml
import numpy as np
import scipy.interpolate as si
import cmapy
from skimage import io, morphology, img_as_ubyte
from scipy import ndimage
# import h5py


# ======================================================================================================================

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--start_x', help='starting position (x) in world coordinates', default='0.0')
    parser.add_argument('--start_y', help='starting position (y) in world coordinates', default='0.0')
    parser.add_argument('--input', help='filename of the map description (.yaml)')
    parser.add_argument('--output', help='filename of the output dataset (.npz)')
    parser.add_argument('--export_images', help='export each layer as bitmap (for debugging purposes)', action='store_true')
    args = parser.parse_args()

    data = np.load('../pl.h5.npz')

    print("Verbose infos:")
    print("Starting position (world coordinates): [x,y] = [{:.2f}, {:.2f}]".format(
        data["arr_0"][0], data["arr_0"][1]
    ))
    print("Starting position (grid coordinates): [x,y] = [{:f}, {:f}]".format(
        data["arr_0"][2], data["arr_0"][3]
    ))
    print("Center position (grid coordinates): [x,y] = [{:.2f}, {:.2f}]".format(
        data["arr_0"][4], data["arr_0"][5]
    ))
    print("Occupied threshold: {:.4f}".format(data["arr_0"][6]))
    print("Min. pixel value*: {:8.4f} (*) before normalization".format(data["arr_0"][7]))
    print("Max. pixel value*: {:8.4f}".format(data["arr_0"][8]))
    print("Dimensions: {:f} x {:f}".format(data["arr_0"][9], data["arr_0"][10]))


