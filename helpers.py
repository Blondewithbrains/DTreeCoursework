import numpy as np

def extract_X_y(dataset, return_num_features=False):
    '''
    Extracts the features (X) and labels (y) from the data matrix (dataset)
    Optionally returns the number of features (return_num_features=True)
    '''
    instances, columns = np.shape(dataset)
    features = columns-1
    
    # the labels form the final column of the data matrix
    X = dataset[:,:features]
    y = dataset[:,features]
    
    if return_num_features:
        return X, y, features
    
    else:
        return X, y

def split_dataset(data, threshold, feature):
    '''
    splits the dataset (data) along some critical value (split_threshold) of the specified feature (feature)
    assigns 
    '''
    right_dataset = data[data[:, feature] >= threshold]
    left_dataset = data[data[:, feature] < threshold]
    
    return left_dataset, right_dataset

def get_mode(list_like):
    '''
    calculate the mode of the list-like object
    '''
    l_l = np.asarray(list_like)
    unique_elements = set(list_like)
    counts_dict = {unique_element:np.sum(l_l[l_l == unique_element]) for unique_element in unique_elements}
    return max(counts_dict, key=counts_dict.get)