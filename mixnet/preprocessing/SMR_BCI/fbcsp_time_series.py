import numpy as np
from sklearn.model_selection import StratifiedKFold
import os
from min2net.preprocessing.FBCSP_no_selBest import FBCSP
from min2net.preprocessing.SMR_BCI import raw
from min2net.preprocessing.config import CONSTANT
CONSTANT = CONSTANT['SMR_BCI']
raw_path = CONSTANT['raw_path']
n_subjs = CONSTANT['n_subjs']
# n_chs = CONSTANT['n_chs']
n_trials_tr = CONSTANT['n_trials_tr'] 
n_trials_te = CONSTANT['n_trials_te']
orig_smp_freq = CONSTANT['orig_smp_freq']
MI_len = CONSTANT['MI']['len']

def subject_dependent_setting(k_folds, pick_smp_freq, n_components, bands, n_features, order, save_path, num_class=2, sel_chs=None):
    sel_chs = CONSTANT['sel_chs'] if sel_chs == None else sel_chs
    n_folds = k_folds
    n_chs = len(sel_chs)
    save_path = save_path + '/SMR_BCI/fbcsp_time_series/{}_class/{}_csp_components/subject_dependent'.format(num_class,n_components)

    X_train_all, y_train_all = np.zeros((n_subjs, n_trials_tr, n_chs, int(MI_len*pick_smp_freq))), np.zeros((n_subjs, n_trials_tr))
    X_test_all, y_test_all = np.zeros((n_subjs, n_trials_te, n_chs, int(MI_len*pick_smp_freq))), np.zeros((n_subjs, n_trials_te))

    id_chosen_chs = raw.chanel_selection(sel_chs)
    for s in range(n_subjs):
        X_train, y_train, X_test, y_test = __load_SMR_BCI(raw_path, s+1, pick_smp_freq, id_chosen_chs)
        X_train_all[s], y_train_all[s] = X_train, y_train
        X_test_all[s], y_test_all[s] = X_test, y_test

    for directory in [save_path]:
        if not os.path.exists(directory):
            os.makedirs(directory)
    # Carry out subject-dependent setting with 5-fold cross validation
    for person, (X_tr, y_tr, X_te, y_te) in enumerate(zip(X_train_all, y_train_all, X_test_all, y_test_all)):
        if len(X_tr.shape) != 3:
            raise Exception('Dimension Error, must have 3 dimension')

        skf = StratifiedKFold(n_splits=n_folds, random_state=42, shuffle=True)
        for fold, (train_index, val_index) in enumerate(skf.split(X_tr , y_tr)):
            print('FOLD:', fold+1, 'TRAIN:', len(train_index), 'VALIDATION:', len(val_index))
            X_tr_cv, X_val_cv = X_tr[train_index], X_tr[val_index]
            y_tr_cv, y_val_cv = y_tr[train_index], y_tr[val_index]

            # Peforming FBCSP feature extraction
            fbcsp_scaler = FBCSP(bands=bands, smp_freq=pick_smp_freq, num_class=num_class, order=order, n_components=n_components, n_features=n_features)
            X_tr_fbcsp = fbcsp_scaler.fit_transform(X_tr_cv, y_tr_cv)
            X_val_fbcsp = fbcsp_scaler.transform(X_val_cv)
            X_te_fbcsp = fbcsp_scaler.transform(X_te)
            print('Check dimension of training data {}, val data {} and testing data {}'.format(X_tr_fbcsp.shape, X_val_fbcsp.shape, X_te_fbcsp.shape))

            SAVE_NAME = 'S{:03d}_fold{:03d}'.format(person+1, fold+1)
            __save_data_with_valset(save_path, SAVE_NAME, X_tr_fbcsp, y_tr_cv, X_val_fbcsp, y_val_cv, X_te_fbcsp, y_te)
            print('The preprocessing of subject {} from fold {} is DONE!!!'.format(person+1, fold+1))

def subject_independent_setting(k_folds, pick_smp_freq, n_components, bands, n_features, order, save_path, num_class=2, sel_chs=None):
    sel_chs = CONSTANT['sel_chs'] if sel_chs == None else sel_chs
    n_folds = k_folds
    n_chs = len(sel_chs)
    save_path = save_path + '/SMR_BCI/fbcsp_time_series/{}_class/{}_csp_components/subject_independent'.format(num_class,n_components)

    X_train_all, y_train_all = np.zeros((n_subjs, n_trials_tr, n_chs, int(MI_len*pick_smp_freq))), np.zeros((n_subjs, n_trials_tr))
    X_test_all, y_test_all = np.zeros((n_subjs, n_trials_te, n_chs, int(MI_len*pick_smp_freq))), np.zeros((n_subjs, n_trials_te))

    id_chosen_chs = raw.chanel_selection(sel_chs)
    for s in range(n_subjs):
        X_train, y_train, X_test, y_test = __load_SMR_BCI(raw_path, s+1, pick_smp_freq, id_chosen_chs)
        X_train_all[s], y_train_all[s] = X_train, y_train
        X_test_all[s], y_test_all[s] = X_test, y_test

    for directory in [save_path]:
        if not os.path.exists(directory):
            os.makedirs(directory)

    # Carry out subject-independent setting with 5-fold cross validation
    for person, (X_val, y_val, X_te, y_te) in enumerate(zip(X_train_all, y_train_all, X_test_all, y_test_all)):
        train_subj = [i for i in range(n_subjs)]
        train_subj = np.delete(train_subj, person) # remove test subject

         # Generating fake data to used for k-fold cross-validation only
        fake_tr = np.zeros((len(train_subj), 2))
        fake_tr_la = np.zeros((len(train_subj)))

        skf = StratifiedKFold(n_splits=n_folds, random_state=42, shuffle=True)
        for fold, (train_ind, val_ind) in enumerate(skf.split(fake_tr , fake_tr_la)):
            print('FOLD:', fold+1, 'TRAIN:', len(train_ind), 'VALIDATION:', len(val_ind))
            train_index, val_index = train_subj[train_ind], train_subj[val_ind]
            X_train_cat = np.concatenate((X_train_all[train_index].reshape(-1,n_chs,int(MI_len*pick_smp_freq)), X_test_all[train_index].reshape(-1,n_chs,int(MI_len*pick_smp_freq))), axis=0)
            X_val_cat = np.concatenate((X_train_all[val_index].reshape(-1,n_chs,int(MI_len*pick_smp_freq)), X_test_all[val_index].reshape(-1,n_chs,int(MI_len*pick_smp_freq))), axis=0)
            y_train_cat = np.concatenate((y_train_all[train_index].reshape(-1), y_test_all[train_index].reshape(-1)), axis=0)
            y_val_cat = np.concatenate((y_train_all[val_index].reshape(-1), y_test_all[val_index].reshape(-1)), axis=0)
             # Peforming FBCSP feature extraction
            fbcsp_scaler = FBCSP(bands=bands, smp_freq=pick_smp_freq, num_class=num_class, order=order, n_components=n_components, n_features=n_features)
            X_train_fbcsp = fbcsp_scaler.fit_transform(X_train_cat, y_train_cat)
            X_val_fbcsp = fbcsp_scaler.transform(X_val_cat)
            X_test_fbcsp = fbcsp_scaler.transform(X_te)
            print("Check dimension of training data {}, val data {} and testing data {}".format(X_train_fbcsp.shape, X_val_fbcsp.shape, X_test_fbcsp.shape))

            SAVE_NAME = 'S{:03d}_fold{:03d}'.format(person+1, fold+1)
            __save_data_with_valset(save_path, SAVE_NAME, X_train_fbcsp, y_train_cat, X_val_fbcsp, y_val_cat, X_test_fbcsp, y_te)
            print('The preprocessing of subject {} from fold {} is DONE!!!'.format(person+1, fold+1))

def __load_SMR_BCI(PATH, subject, new_smp_freq, id_chosen_chs):
    start = CONSTANT['MI']['start'] # 4
    stop = CONSTANT['MI']['stop'] # 8
    X_train, y_tr, X_test, y_te  = raw.load_crop_data(PATH=PATH, subject=subject, start=start, stop=stop, new_smp_freq=new_smp_freq, id_chosen_chs=id_chosen_chs)
    return X_train, y_tr, X_test, y_te


def __save_data_with_valset(save_path, NAME, X_train, y_train, X_val, y_val, X_test, y_test):
    np.save(save_path+'/X_train_'+NAME+'.npy', X_train)
    np.save(save_path+'/X_val_'+NAME+'.npy', X_val)
    np.save(save_path+'/X_test_'+NAME+'.npy', X_test)
    np.save(save_path+'/y_train_'+NAME+'.npy', y_train)
    np.save(save_path+'/y_val_'+NAME+'.npy', y_val)
    np.save(save_path+'/y_test_'+NAME+'.npy', y_test)
    print('save DONE')
