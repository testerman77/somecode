# coding=utf-8
from PIL import Image
import imagehash
import argparse
import shelve
import glob

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "path to input dataset of images")
ap.add_argument("-s", "--shelve", required = True,
	help = "output shelve database")
ap.add_argument("-q", "--query",
	help = "path to the query image")
args = vars(ap.parse_args())


db = shelve.open(args["shelve"], writeback = True)

query = args.get("query", None)
if query:
	queryImage = Image.open(query)
	h = str(imagehash.dhash(queryImage))
	filenames = db.get(h, None)

	if filenames:
		print "Matched %d images" % (len(filenames))
		for filename in filenames:
			image = Image.open(args["dataset"] + "/" + filename)
			image.show()
	else:
		print "Not matched,will add to database"
		filename = query[query.rfind("/") + 1:]
		db[h] = db.get(h, []) + [filename]
else:
	for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
		image = Image.open(imagePath)
		h = str(imagehash.dhash(image))
		filename = imagePath[imagePath.rfind("/") + 1:]
		db[h] = db.get(h, []) + [filename]

db.close()