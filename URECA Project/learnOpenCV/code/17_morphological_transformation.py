#https://www.youtube.com/watch?v=xSzsD4kXhRw&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=19

#cv.dilate applies a small shape(eg.square) to remove patches in the image (eg. light reflection on smarties)

#cv.erode does the opposite, applies a small shape to erode/smoothen, but increases patch sizes

#morphologyEx:opening is erosion followed by dilation. usually better
#morphologyEx:closing is dilation followed by erosion
#morphologyEx:gradient is difference between dilation and erosion
#morphologyEx:tophat is difference between image and opening