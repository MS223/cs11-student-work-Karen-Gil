class color(object)
royalblue=color()
plum= color()
honeydew=color()

# (65,105,225)
royalblue.r= 65
royalblue.g= 105
royalblue.b=225

# 221,160,221)
plum.r= 221
plum.g=106
plum.b=221

# (240,255,240)
honeydew.r=240
honeydew.g=225
honeydew.b=240

def add_color(color1,color2):
    r = (color1.r+color2.r)/2
    print r
