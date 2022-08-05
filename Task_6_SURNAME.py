# -*- coding: utf-8 -*-
"""
Introduction to Programming and Applied Statistics

======================
Final Project - TASK 6
======================
"""
import bk_functions as bk
import math
"""
Subtask 6.1
-----------
Define a function that creates a multipart geojson
with N points randomly distributed over a geographical domain.
The function should takes as arguments the number of points and
the bounding box coordinates (lon_E, lat_S, lon_W, lat_N) of the
geograhical domain.
"""
extent  = (90, 20, 70, 40)
extent2 = (90.00252, 20.225, 20.1, 40.3)

def gen_randpoint_dict(extent, number):
    feature = bk.Feature(featuretype="MultiPoint")
    feature.gen_randscatter(extent, number)
    mpgobj = bk.GeojsonObject()
    mpgobj.append(feature)
    return mpgobj

ftobj = gen_randpoint_dict(extent, 200)

ftobj.set_path_abs("randompoints.geojson")

ftobj.dump()

"""
Subtask 6.2
-----------
Define a function that creates a checkerboard grid of points for
a predifed geographic region. To do this your function should
generate points over a regular grid but keep only every second point.
The function should take as inputs:

- the distance between the points in the x- and in the y-dimension.
- the bounding box coordinates (lon_E, lat_S, lon_W, lat_N) of the
"""
def create_checkerboard(extent, dist_x, dist_y) -> bk.Feature:
    checker_ft = bk.Feature(featuretype="MultiPoint")
    checker_ft.gen_grid_adv(extent, dist_x, dist_y, matrixname="checkerboard")
    return checker_ft

gobj = bk.GeojsonObject()
gobj.append(create_checkerboard(extent, 1, 1))
gobj.dump("checkerboard.geojson")


"""
Subtask 6.3
-----------
Define a function that creates a randomized grid of points over
a predifed geographic region. To achieve this, your function should
generate points over a regular grid and then randomly shift them along
the x- and y-axis according to some random value. The random value should
not be greater than a max_shift threshold.

The function should take as inputs:

- the distance between the points in the x- and in the y-dimension.
- the max_shift value.
- the bounding box coordinates (lon_E, lat_S, lon_W, lat_N) of the
  geograhical domain


Hint: Check the material of L6.
"""

def random_grid(extent, grid_spacing_x, grid_spacing_y, shift, offset_fixed=False, iterations=1) -> bk.GeojsonObject:
    shift_ft = bk.Feature(featuretype="MultiPoint")
    shift_ft.gen_grid(extent, grid_spacing_x, grid_spacing_y)

    shift_ft_obj = bk.GeojsonObject()
    for foo in range(iterations):
        shift_ft_obj.append(shift_ft.offset_circular(shift, offset_fixed=offset_fixed))

    return shift_ft_obj
    
shift_ft_obj = random_grid(extent, 5, 5, 1, offset_fixed=False, iterations=50)
shift_ft_obj.dump("offset_dict.geojson")