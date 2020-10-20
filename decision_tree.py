from helpers import extract_X_y, split_dataset, get_mode
from information import get_best_split_along_feature
import numpy as np

class Node:
    '''
    object that defines the nodes of a decision tree
    the root node defines the whole decision tree, since it possesses its children nodes as attributes
    '''
    def __init__(self, depth, feature=None, threshold=None, value=None, right_moves=None):
        '''
        'feature' and 'threshold' define the decision represented by the node (these are None for a leaf node)
        if the node is a leaf node, its 'value' attribute is not None. 
        'rightmoves' describes the position of a node relative to the leftmost node; this will be useful for plotting.
        '''
        self.feature = feature
        self.threshold = threshold
        self.value=value
        self.left_child=None
        self.right_child=None
        self.depth=depth
        self.right_moves=right_moves

    def get_label(self):
        if self.value is not None:
            label = "Leaf node: value {}".format(self.value)
        else:
            label = "Decision node: feature{} >= {}".format(self.feature, self.threshold)

        return label

def find_split(training_dataset):

    '''
    Find the best way to split 'training dataset' so as to maxmimise the information gain.
    '''
    X, y, features = extract_X_y(training_dataset, True)
        
    # declare best feature, split threshold and corresponding entropy.
    # note that maximising the information gain is equivalent to minimising the entropy of the child nodes
    # (question: is this always true? can you have nodes which are only able to decrease information? Answer: no.)
    feature0=None
    split0=None
    e0 = np.inf
    
    # loop over features; test all splits
    for each_feature in range(features):
        if (X[:, each_feature] == X[:, each_feature][0]).all():
            continue
        split, e = get_best_split_along_feature(training_dataset, each_feature)
        if e <= e0:
            e0 = e
            split0 = split
            feature0 = each_feature
            
    # returns None, None if features are all the same (no split can be defined).
    return split0, feature0

def decision_tree_learning(training_dataset, depth, right_moves=None):
    '''
    return a node that represents the optimal decision (wrt information gain) represented by this node
    '''
    X, y = extract_X_y(training_dataset)

    # if all labels are the same, make this a leaf node
    if np.all(y == y[0]).all():
        return Node(depth, value=y[0], right_moves=right_moves), depth
    
    else:
        # find the optimal split
        split, feature_to_split = find_split(training_dataset)

        # if split is undefined, make the current node a leaf node with modal value
        if feature_to_split is None:
            return Node(depth, alue=get_mode(y), right_moves=right_moves), depth

        # define the current node, use recursion to define its children
        node = Node(depth, feature=feature_to_split, threshold=split, right_moves=right_moves)
        l_dataset, r_dataset = split_dataset(training_dataset, split, feature_to_split)
        l_branch, l_depth = decision_tree_learning(l_dataset, depth+1, right_moves)
        if right_moves is not None:
            right_moves += 1
        r_branch, r_depth = decision_tree_learning(r_dataset, depth+1, right_moves)
        node.left_child = l_branch
        node.right_child = r_branch

        # return the current node
        return node, max(l_depth, r_depth)