from skimage import measure
from pandas import DataFrame
#https://zhuanlan.zhihu.com/p/636212572
#https://scikit-image.org/docs/stable/auto_examples/segmentation/plot_regionprops.html

# get properties of label image
props = measure.regionprops_table(masks, properties=['centroid',
                                                     'area',
                                                     'axis_major_length',
                                                     'axis_minor_length'])
props_dataframe = DataFrame(props)
props_dataframe.to_csv('./props_table.csv')
