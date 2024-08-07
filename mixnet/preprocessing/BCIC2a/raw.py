import numpy as np
import scipy.io as sio
from min2net.utils import resampling
from min2net.preprocessing.config import CONSTANT
CONSTANT = CONSTANT['BCIC2a']
# n_chs = CONSTANT['n_chs']
n_trials = CONSTANT['n_trials']
window_len = CONSTANT['trial_len']*CONSTANT['orig_smp_freq']
orig_chs = CONSTANT['orig_chs']
trial_len = CONSTANT['trial_len'] 
orig_smp_freq = CONSTANT['orig_smp_freq']

def read_raw(PATH, subject, training, num_class, id_chosen_chs):
    data, label = [], []
    NO_valid_trial = 0
    if training:
        mat = sio.loadmat(PATH+'/A0'+str(subject)+'T.mat')['data']
    else:
        mat = sio.loadmat(PATH+'/A0'+str(subject)+'E.mat')['data']
    for ii in range(0,mat.size):
        mat_1 = mat[0,ii]
        mat_2 = [mat_1[0,0]]
        mat_info = mat_2[0]
        _X = mat_info[0]
        _trial = mat_info[1]
        _y = mat_info[2]
        _fs = mat_info[3]
        _classes = mat_info[4]
        _artifacts = mat_info[5]
        _gender = mat_info[6]
        _age = mat_info[7]
        for trial in range(0,_trial.size):
            # num_class = 2: picked only class 1 (left hand) and class 2 (right hand) for our propose
            if(_y[trial][0] <= num_class): 
                data.append(np.transpose(_X[int(_trial[trial]):(int(_trial[trial])+window_len), id_chosen_chs])) # selected merely motor cortices region
                label.append(int(_y[trial]) -1 ) # -1 to adjust the values of class to be in range 0 and 1
    data_arr = np.array(data)
    label_arr = np.array(label)
    return data_arr, label_arr

def chanel_selection(sel_chs): 
    chs_id = []
    for name_ch in sel_chs:
        ch_id = np.where(np.array(orig_chs) == name_ch)[0][0]
        chs_id.append(ch_id)
        print('chosen_channel:', name_ch, '---', 'Index_is:', ch_id)
    return chs_id
        
def load_crop_data(PATH, subject, start, stop, new_smp_freq, num_class, id_chosen_chs):
    start_time = int(start*new_smp_freq) # 2*
    stop_time = int(stop*new_smp_freq) # 6*
    X_train, y_tr = read_raw(PATH=PATH, subject=subject,
                             training=True, num_class=num_class, id_chosen_chs=id_chosen_chs)
    X_test, y_te = read_raw(PATH=PATH, subject=subject,
                            training=False, num_class=num_class, id_chosen_chs=id_chosen_chs)
    if new_smp_freq < orig_smp_freq:
        X_train = resampling(X_train, new_smp_freq, trial_len)
        X_test = resampling(X_test, new_smp_freq, trial_len)
    X_train = X_train[:,:,start_time:stop_time]
    X_test = X_test[:,:,start_time:stop_time]
    print("Verify dimension training {} and testing {}".format(X_train.shape, X_test.shape)) 
    return X_train, y_tr, X_test, y_te 