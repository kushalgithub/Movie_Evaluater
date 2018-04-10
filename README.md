# Movie_Evaluater
The file contains following folders:

1>Code
2>Data

1>Code

In code folders there are 24 python files.
--->Where movie1.py to movie20.py python files are used for collecting tweets.
--->Reduced_Final.py file contains the code for getting the unique tweets from the files that are generated from movie1 to movie20.
--->trial.py is used for generating the training dataset.
--->trial_test.py file is used for generating the testing data set.
--->project.py file is used for applying the SVM on training and testing dataset.

2>Data 
In this folder there are 22 datafiles.

--->The files that are starting with the reduced are used for the training and testing data.
--->train.txt file is the file used as training dataset.
--->test.txt file is the file used as testing dataset.
--->predicted_tweets.txt is the file that is generated after running the project.py file. 


For running the data:

The libraries that are required:

-->sklearn
-->pylab
-->numpy
-->tweepy
-->json

Step 1:

By running the movie1.py to movie20.py there will be 20 different files generated.

Step 2:

Run those 20 different files of step1  to Reduced_final.py that will give you reduced_moviename.txt.

Step 3:

Take any of 15 reduced files that are generated in step 2 for training data and 5 files for testing data.
Use trial.py for generating train.txt which is your training data and trial_test.py for generating
test.txt which is your testing data.

Step 4:

Run training and testing data to the project.py which will generate predicted_tweets.txt.

Step 5:

Through predicted_tweets we can identify the prediction.  
