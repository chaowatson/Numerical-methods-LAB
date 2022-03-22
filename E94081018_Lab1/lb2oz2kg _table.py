print("lb    oz    kg")
lb = 1
for i in range(10):
    oz = lb * 16  # transform cm to inch
    kg = lb * 0.45359  # get the integer part of feet
    print("{0:2d}".format(lb), ",", "{0:3d}".format(oz), ",", "{:.5f}".format(kg))
    lb = lb + 1
