import glob
import sys
import een
import os

camera = sys.argv[3] 

#login and get image list
ctx = een.login(sys.argv[1], sys.argv[2])
img_list = ctx.image_list(esn=camera, asset_type="thumb", time=een.timestamp("now"), count=-500)

try:
	os.mkdir("src")
except:
	pass

#fetch the images
for v in img_list:
	print("fetching %s" % v['s'])
	img = ctx.fetch_image(esn=camera, time=v['s'], asset_type="preview")
	fh  = open("src/" + v['s'] + ".jpeg", "wb")
	fh.write(img)
	fh.close()

ctx.logout()

#glob the jpegs and create a video
#glob = glob.glob('*.jpeg')
#os.system("ffmpeg -r 25 -qscale 2 -i *.jpeg out.mp4")
