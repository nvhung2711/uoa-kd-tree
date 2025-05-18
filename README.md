Wine experts evaluate the quality of wine based on sensory data. We could also collect
the features of wine from objective tests, thus the objective features could be used to
predict the expert’s judgement, which is the quality rating of the wine. This could be
formed as a supervised learning problem with the objective features as the data features
and wine quality rating as the data labels.

In this assignment, we provide objective features obtained from physicochemical
statistics for each white wine sample and its corresponding rating provided by wine
experts. You are expect to implement k-d tree (KDT), and use the training set to
train your k-d tree, then provide wine quality prediction on the test set by searching
the tree.

Wine quality rating is measured in the range of 0-9. In our dataset, we only keep
the samples for quality ratings 5, 6 and 7. The 11 objective features are listed as follows:
• f acid: fixed acidity
• v acid: volatile acidity
• c acid: citric acid
• res sugar: residual sugar
• chlorides: chlorides
• fs dioxide: free sulfur dioxide
• ts dioxide: total sulfur dioxide
• density: density
• pH: pH
• sulphates: sulphates
• alcohol: alcohol


Explanation of the Data.

train: The first 11 columns represent the 11 features and the 12th column is the wine
quality. A sample is depicted as follows:

f_acid v_acid c_acid res_sugar chlorides fs_dioxide ts_dioxide density pH sulphates alcohol quality
8.10 0.270 0.41 1.45 0.033 11.0 63.0 0.99080 2.99 0.56 12.0 5
8.60 0.230 0.40 4.20 0.035 17.0 109.0 0.99470 3.14 0.53 9.7 5
7.90 0.180 0.37 1.20 0.040 16.0 75.0 0.99200 3.18 0.63 10.8 5
8.30 0.420 0.62 19.25 0.040 41.0 172.0 1.00020 2.98 0.67 9.7 5
6.50 0.310 0.14 7.50 0.044 34.0 133.0 0.99550 3.22 0.50 9.5 5

test: Similar to train, but without the 12th colum as they are the values your model
will predict. A sample is depicted as follows:

f_acid v_acid c_acid res_sugar chlorides fs_dioxide ts_dioxide density pH sulphates alcohol
7.0 0.360 0.14 11.60 0.043 35.0 228.0 0.99770 3.13 0.51 8.900000
6.3 0.270 0.18 7.70 0.048 45.0 186.0 0.99620 3.23 0.47 9.000000
7.2 0.290 0.20 7.70 0.046 51.0 174.0 0.99582 3.16 0.52 9.500000
7.1 0.140 0.35 1.40 0.039 24.0 128.0 0.99212 2.97 0.68 10.400000
7.6 0.480 0.28 10.40 0.049 57.0 205.0 0.99748 3.24 0.45 9.300000
1.1 1NN (K-d Tree)

From the given training data, our goal is to learn a function that can predict the wine
quality rating of a wine sample, based on the objective features. In this assignment,
the predictor function will be constructed as a k-d tree. Since the attributes (objective
features) are continuously valued, you shall apply the k-d tree algorithm for continuous
data, as outlined in Algorithms 1. It is the same as taught in the lecture. Once the tree
is constructed, you will search the tree to find the 1-nearest neighbour of a query point
and label the query point. Please refer to the search logic taught in the lecture to write
your code of 1NN search.

Algorithm 1 BuildKdTree(P, D)
Require: A set of points P of M dimensions and current depth D.
1: if P is empty then
2: return null
3: else if P only has one data point then
4: Create new node node
5: node.d ← d
6: node.val ← val
7: node.point ← current point
8: return node
9: else
10: d ← D mod M
11: val ← Median value along dimension among points in P.
12: Create new node node.
13: node.d ← d
14: node.val ← val
15: node.point ← point at the median along dimension d
16: node.lef t ← BuildKdTree( points in P for which value at dimension d is less than or
equal to val, D+1)
17: node.right ← BuildKdTree( points in P for which value at dimension d is greater than
val, D+1)
18: return node
19: end if
Note: Sorting is not necessary in some cases depending on your implementation. Please
figure out whether your code needs to sort the number first. Also, if you compute the
median by yourself, when there’s an even number of points, say [1,2,3,4], the median is
2.5.

Write your k-d tree program in Python 3.6.9 in a file called nn kdtree.py. Your program
must be able to run as follows:
$ python nn_kdtree.py [train] [test] [dimension]
The inputs/options to the program are as follows:
• [train] specifies the path to a set of the training data file.
• [test] specifies the path to a set of testing data file.
• [dimension] is used to decide which dimension to start the comparison. (Algo-
rithm 1).
Given the inputs, your program must construct a k-d tree (following the prescribed
algorithms) using the training data, then predict the quality rating of each of the wine
sample in the testing data. Your program must then print to standard output (i.e.,
the command prompt) the list of predicted wine quality ratings, vertically based on the
order in which the testing cases appear in [test].
