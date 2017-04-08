from skimage import io
import numpy as np
import os
from sklearn import svm
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV

#open tagged filelist
fh = open("truthtable_new_16July2016.csv","r")

#read truthtable into memory
fh.readline()
data = fh.readlines()
fh.close()

#initialise arrays for data
#dataset shape is size of flattened image array length*width in pixels
#the first column labels the data as having eggs present or not
#this is a bit of a hack
dataset = np.zeros((1,788066))

print "INFO: Building dataset"

#interate through list of tagged files and find ones that exist
for line in data:

    line = line.split(",")
    line[0] = line[0][1:-1]

    #images are expected to be unzipped into a directory called images
    path = "images/"+line[0]    
    isfile = os.path.isfile(path)

    #if file exist, add contents to data arrays
    if isfile==True:

        #check if eggs are expected in the image
        eggs = int(line[1].rstrip())
        if eggs>0:
            eggs=1

        #import image
        image = io.imread(path,as_grey=True)
        image = np.reshape(image,(788065,1))

        #join image array and label
        example = np.vstack((eggs,image))
        #this is a row vector with label and image
        example = np.transpose(example) 

        #append to data array
        dataset = np.vstack((dataset,example))

#remove first row from initialisation
#this is a hack
dataset = dataset[1:]

#initialise classifier
classifier = svm.SVC()

#save this many data samples from the dataset for testing
test_samples = 14

#setup training and test data and target arrays
training_data = dataset[:-test_samples,1:]
training_target = dataset[:-test_samples,0]

test_data = dataset[-test_samples:,1:]
test_target = dataset[-test_samples:,0]

#pca, todo grid search parameters for PCA
n_comp = 50
print("INFO: PCA, n_components="+str(n_comp))
pca = PCA(n_components=n_comp,whiten=True,svd_solver='auto')
pca.fit(training_data)
traindata_pca = pca.transform(training_data)
test_pca = pca.transform(test_data)

#train model via grid search
print("INFO: Grid search")
gsc = GridSearchCV(estimator=svm.SVC(),
                param_grid={ 'C': [1, 2, 3, 4, 5],
                'kernel': [ 'linear', 'poly', 'rbf', 'sigmoid' ] },
                cv=5 )
gsc.fit(traindata_pca,training_target)

#print results
res = gsc.score(test_pca,test_target)
print("%3f"%(res))
#result 0.714
