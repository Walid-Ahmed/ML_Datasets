
#usage
#python exploreDataset.py. --datasetDir  Cyclone_Wildfire_Flood_Earthquake_Database    -- channels  3


import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import argparse


image_types = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff",".ppm")


def list_images(basePath, contains=None):
    # return the set of files that are valid
    return list_files(basePath, validExts=image_types, contains=contains)


def list_files(basePath, validExts=None, contains=None):
    # loop over the directory structure
    for (rootDir, dirNames, filenames) in os.walk(basePath):
        # loop over the filenames in the current directory
        for filename in filenames:
            # if the contains string is not none and the filename does not contain
            # the supplied string, then ignore the file
            if contains is not None and filename.find(contains) == -1:
                continue

            # determine the file extension of the current file
            ext = filename[filename.rfind("."):].lower()

            # check to see if the file is an image and should be processed
            if validExts is None or ext.endswith(validExts):
                # construct the path to the image and yield it
                imagePath = os.path.join(rootDir, filename)
                yield imagePath

def getTrainStatistics2(datasetDir):

    print("__________________________________________________________________________________________________________")
    print(datasetDir)
    for (dirpath, dirnames, filenames) in os.walk(datasetDir):
        imagePaths = sorted(list(list_images(dirpath)))
        print('[INFO] Total images of {} is {} '.format(dirpath ,len(imagePaths)))
    print("__________________________________________________________________________________________________________")




    def drarwGridOfImages(dataSetDir,fileNameToSaveImage=None,channels=3):



	  #print(train_label1_fnames[:10])
	  #print(train_label2_fnames[:10])
	  imagePaths = sorted(list(paths.list_images(dataSetDir)))



	  # Parameters for our graph; we'll output images in a 4x4 configuration
	  nrows = 4
	  ncols = 4

	  pic_index = 0 # Index for iterating over images

	  #display a batch of 4*4 pictures

	  # Set up matplotlib fig, and size it to fit 4x4 pics
	  fig = plt.gcf()
	  fig.set_size_inches(ncols*4, nrows*4)

	  pic_index+=8
	  random.shuffle(imagePaths)
	  imagePaths=imagePaths[0:16]





	  for i, img_path in enumerate(imagePaths):
	    # Set up subplot; subplot indices start at 1
	    sp = plt.subplot(nrows, ncols, i + 1)
	    sp.axis('Off') # Don't show axes (or gridlines)

	    if (channels==3):
	      img = mpimg.imread(img_path)
	    else:
	      img=Image.open(img_path).convert('L')
	    plt.imshow(img)
	 

	  if(fileNameToSaveImage != None):
	    plt.savefig(fileNameToSaveImage)
	  plt.show()


if __name__ == "__main__":

	# construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("--datasetDir", required=True, help="datasetDir")
    ap.add_argument("--channels", type=int, default=3, help="number of channels")
    ap.add_argument("--fileNameToSaveImage", type=str, default="demoImage.png", help="number of channels")


    #read the arguments
    args = vars(ap.parse_args())
    datasetDir=args["datasetDir"]
    channels=args["channels"]
    fileNameToSaveImage=args["fileNameToSaveImage"]



	getTrainStatistics2(datasetDir)
	drarwGridOfImages(dataSetDir,fileNameToSaveImage,channels)


