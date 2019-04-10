import numpy as np
import xarray 

## Prepare data:
#
point = {'x': np.array(-0.47652306228698005),
         'y': np.array([[-0.41809043],
                      [ 0.48407823]])}
points = 10 * [point]

## Convert to Xray DataArrays:
#
list_x = [p['x'] for p in points]
list_y = [p['y'] for p in points]
da_x = xarray.DataArray(list_x, [('x', range(len(list_x)))])
da_y = xarray.DataArray(list_y, [
     ('x', range(len(list_y))),
     ('y0', range(2)), 
     ('y1', [0]), 
 ])