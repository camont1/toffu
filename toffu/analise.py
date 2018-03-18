import numpy as np
import cv2
#import sklearn as sk

def entropy_image(filename,bins=30):
    """
    extracts the renyi entropy of image stored under filename.
    """
    img = cv2.imread(filename,0)/255.0 # gray images
    p,_ = np.histogram( img, range=[0.0,1.0],bins=bins )
    return -np.log(np.dot(p,p)/(np.sum(p)**2.0))

def estimatives(data,max_split=5):
    """
    returns multiscale estimatives from data.

    data: input. list representation of an image
    """
    m = len(data)
    k = 0
    avg = []
    var = []
    entropy = []
    while (m > 0) and (k < max_split):
        z = data[:(m*(2**k))].reshape( m , 2**k )
        avg.append( np.mean(z ,axis=0) )
        var.append( np.var( z ,axis=0) )
        tmp = []
        for col in range(2**k):
            p,_ =np.histogram( z[:,col], range=[0.0,1.0])
            sq_p = np.sum(p)**2.0
            tmp.append( -np.log(np.dot(p,p)/sq_p ))
        entropy.append(tmp)
        k  += 1
        m = m // 2
    return avg,var,entropy

def img_to_array(filename):
    img = cv2.imread(filename,0)/255.0
    return img.reshape( np.prod(img.shape) )
