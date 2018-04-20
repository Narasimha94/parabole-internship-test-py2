import logging
import os

#Reads and returns the list of files from a directory
def read_directory(mypath):
    current_list_of_files = []

    while True:
        for (_, _, filenames) in os.walk(mypath):
            current_list_of_files = filenames
        logging.info("Reading the directory for the list of file names")
        return current_list_of_files



#Function you will be working with
def creating_subclusters(list_of_terms, name_of_file):

    wordcount = Counter(file.read(name_of_file).split(" "))

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)
 
true_k = 2
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=wordcount, n_init=1)
model.fit(X)
 
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
    print
 
 
print(" ")
print(Prediction)
 
Y = vectorizer.transform([list_of_terms])
prediction = model.predict(Y)
print(prediction)
file = open(name_of_file,”w”) 
file.write(prediction) 


#Main function
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    #Folder where the input files are present
    mypath = "input"
    list_of_input_files = read_directory(mypath)
    for each_file in list_of_input_files:
        with open(os.path.join(mypath,each_file), "r") as f:
            file_contents = f.read()
        list_of_term_in_cluster = file_contents.split()

        # Sending the terms to be converted to subclusters in your code
        creating_subclusters(list_of_term_in_cluster, each_file)


#End of code
