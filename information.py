import helpers
import numpy as np

def get_entropy(dataset):
    '''
    calculates the Shannon entropy (in nats: 1 nat ~ 1.44 bits)
    class probabilities are estimated via relative frequency in 'dataset'
    '''
    X, y = helpers.extract_X_y(dataset)

    # use set() to find all unique labels
    unique_elements = set(y)
    
    # find the relative frequencies of each label
    probabilities = np.empty(len(unique_elements))
    for i, each_unique_element in enumerate(unique_elements):
        probabilities[i] = np.sum(y==each_unique_element)
    probabilities /= len(y)
    
    # calculate & return entropy
    entropy = sum([-np.log(p)*p for p in probabilities])
    return entropy

def get_split_entropy(dataset, feature, split):
    '''
    calculate the entropy of two datasets, formed by splitting 'dataset' according to 'split' and 'feature'.
    note that we don't need to normalise the total entropy (normalisation is arbitrary)
    '''
    left_dataset, right_dataset = helpers.split_dataset(dataset, split, feature)
    return get_entropy(left_dataset)*len(left_dataset) + get_entropy(right_dataset)*len(right_dataset)

def get_best_split_along_feature(training_dataset, feature):
    '''
    get the split threshold for which entropy is minimised
    '''
    X, y = helpers.extract_X_y(training_dataset)

    # extract a vector of feature values for each instance
    x = set(X[:, feature])
    x = np.asarray(sorted(list(x)))
    
    # initiate the best entropy and split; try to minimise the entropy.
    e0 = np.inf
    split0 = None
    
    # if there are only two instances, split along the middle.
    if len(x) <= 2:
        return np.mean(x), 0
    
    # try all splits, look for the lowest entropy.
    for split in x[1:-2]:
        e = get_split_entropy(training_dataset, feature, split)
        if e <= e0:
            e0 = e
            split0 = split
            
    return split0, e0