# advanced-bokeh-filter
Improved implementation of bokeh filter using python by means of Mask R-CNN to find the contours shape and apply the filter based on detected object shape. This code is an extension of the folowing tutorial: https://www.pyimagesearch.com/2018/11/19/mask-r-cnn-with-opencv/

Graph model file download link to put under the mask-rcnn-coco folder:
http://www.mediafire.com/file/6ck7uiasklxz3yc/frozen_inference_graph.pb/file

All you have to do is launch the python script mask-rcnn1.py using the following command on a linux terminal:
!python /content/mask_rcnn.py --mask-rcnn /content/mask-rcnn-coco --image /content/example_03.jpg --visualize 1

PS: This code was implemented on google colab so make the necessary adjustments. 


