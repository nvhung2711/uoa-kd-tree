import sys
import math
#READ INPUTS

#getting the file paths
train_path = sys.argv[1]
test_path = sys.argv[2]
d_start = sys.argv[3] #start_dimension
d_start = int(d_start)

train_f = open(train_path, "r")
test_f = open(test_path, "r")

train_f.readline() #get rid of the first line
test_f.readline() #get rid of the first line

#store the train data in list
train_data = train_f.read() #read the rest of train data
lines = train_data.split('\n')

train_data = []
for line in lines:
    line = " ".join(line.split())
    data = line.split(' ')
    train_data.append(data)

train_data.pop() #pop the last line which contains an empty string

#convert data type to float and the last one to int
for data in train_data:
    for feature in data[:-1]:
        feature = float(feature)
    
    data[-1] = int(data[-1])

#store the test data in list
test_data = test_f.read() #read the rest of test data
lines = test_data.split('\n')

test_data = []
for line in lines:
    line = " ".join(line.split())
    data = line.split(' ')
    test_data.append(data)

test_data.pop() #pop the last line which contains an empty string

#convert data type to float and the last one to int
for data in test_data:
    for feature in data[:-1]:
        feature = float(feature)

#number of features
M = len(test_data[0])





#______________________________________________________________________________
#FUNCTION
def build_kd_tree(points, depth = 0, m = M, k = d_start):
    """
    This function takes a set of training points to build a k-d tree
    """
    n = len(points)

    if n == 0:
        return None
    elif n == 1:
        axis = (depth + k) % m
        return{
            'axis': axis,
            'val': points[0][axis],
            'point': points[0],
            'left': None,
            'right':None
        }
    else:
        axis = (depth + k) % m
        sorted_points = sorted(points, key=lambda point: point[axis])

        return {
            'axis': axis,
            'val': sorted_points[(n-1)//2][axis],
            'point': sorted_points[(n-1)//2],
            'left': build_kd_tree(sorted_points[:(n-1)//2+1], depth + 1),
            'right': build_kd_tree(sorted_points[(n-1)//2+1:], depth + 1)
        }

def distance(point1, point2, m = M):
    """
    This function calculates the distance squared between the two points in multi dimensions
    """
    dis = 0
    for i in range(m):
        d_axis = float(point1[i]) - float(point2[i])
        dis += d_axis * d_axis

    return math.sqrt(dis)

def closer_distance(target, point1, point2):
    """
    This function will compare the distance between target with point 1 and target with point 2.
    It returns the shorter distance.
    """
    if point1 is None:
        return point2


    if point2 is None:
        return point1


    distance1 = distance(target, point1)
    distance2 = distance(target, point2)

    if distance1 < distance2:
        return point1
    else:
        return point2

#traverse the k-d tree to get the closet point
def kd_closest_point(root, target, depth = 0, best = None, m = M):
    """
    This function will take a target point and find the point in k-d tree with the shortest distance
    """
    if root is None:
        return None

    axis = root['axis']

    next_branch = None
    opposite_branch = None

    if target[axis] <= root['point'][axis]:
        next_branch = root['left']
        opposite_branch = root['right']
    else:
        next_branch = root['right']
        opposite_branch = root['left']

    best = closer_distance(target, kd_closest_point(next_branch, target, depth + 1), root['point'])

    if distance(target, best) > (float(target[axis]) - float(root['point'][axis])):
        best = closer_distance(target, kd_closest_point(opposite_branch, target, depth + 1), best)

    return best

def closest_point(all_points, new_point):
    """
    This function brute force all the points and find the one with shortest distance
    """
    best_point = None
    best_distance = None

    for current_point in all_points:
        current_distance = distance(new_point, current_point)

        if best_distance is None or current_distance < best_distance:
            best_distance = current_distance
            best_point = current_point

    return best_point



#____________________________________________________________________________________
#DRIVER
kd_tree = build_kd_tree(train_data, 0)

for i, x in enumerate(test_data):
    # closest = closest_point(train_data, x)
    # print(closest)
    kd_closet = kd_closest_point(kd_tree, x, 0)
    print(kd_closet[-1])