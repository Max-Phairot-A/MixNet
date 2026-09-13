import argparse
import mixnet.preprocessing as prep
from mixnet.preprocessing.config import CONSTANT

'''

1. In case of preparing a particular dataset, please run the script as an example: python prep_FBCSP.py --dataset 'BCIC2a'
2. In case of preparing multiple datasets, please run the script as an example: python prep_FBCSP.py --dataset 'BCIC2a' && python prep_FBCSP.py --dataset 'BCIC2b' && python prep_FBCSP.py --dataset 'BNCI2015_001' && python prep_FBCSP.py --dataset 'SMR_BCI' && python prep_FBCSP.py --dataset 'HighGamma' && python prep_FBCSP.py --dataset 'OpenBMI'
3. In case of preparing only a particular setting, please add the --setting argument (dependent/independent/both, default: both) as an example: python prep_FBCSP.py --dataset 'BCIC2a' --setting 'dependent'

'''

k_folds = 5 
pick_smp_freq = 100
n_components = 2 # 2 is the default as the original paper
bands = [[4, 8], [8, 12], [12, 16], 
            [16, 20], [20, 24], [24, 28], 
            [28, 32], [32, 36], [36, 40]]
n_features = 8
order = 5 # filter order
save_path = 'datasets'
num_class = 2 # Only binary classification task is conducted in this manuscript

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, default='BCIC2a', help='dataset name: ex. [BCIC2a/BCIC2b/BNCI2015_001/SMR_BCI/HighGamma/OpenBMI]')
parser.add_argument('--setting', type=str, default='both', choices=['dependent', 'independent', 'both'], help='which setting to prepare: subject dependent, subject independent, or both')
args = parser.parse_args()

run_dependent = args.setting in ['dependent', 'both']
run_independent = args.setting in ['independent', 'both']

if args.dataset == 'BCIC2a':
    print("============== The {} dataset is being prepared ==========".format(args.dataset))
    if run_dependent:
        prep.BCIC2a.fbcsp.subject_dependent_setting(k_folds=k_folds,
                                                    pick_smp_freq=pick_smp_freq, 
                                                    n_components=n_components,
                                                    bands=bands, 
                                                    n_features=n_features,
                                                    order=order, 
                                                    save_path=save_path, 
                                                    num_class=num_class, 
                                                    sel_chs=CONSTANT['BCIC2a']['sel_chs'])
    if run_independent:
        prep.BCIC2a.fbcsp.subject_independent_setting(k_folds=k_folds,
                                                      pick_smp_freq=pick_smp_freq, 
                                                      n_components=n_components,
                                                      bands=bands, 
                                                      n_features=n_features,
                                                      order=order, 
                                                      save_path=save_path, 
                                                      num_class=num_class, 
                                                      sel_chs=CONSTANT['BCIC2a']['sel_chs'])
elif args.dataset == 'BCIC2b':
    print("============== The {} dataset is being prepared ==========".format(args.dataset))
    if run_dependent:
        prep.BCIC2b.fbcsp.subject_dependent_setting(k_folds=k_folds,
                                                    pick_smp_freq=pick_smp_freq, 
                                                    n_components=n_components,
                                                    bands=bands, 
                                                    n_features=n_features,
                                                    order=order, 
                                                    save_path=save_path, 
                                                    num_class=num_class, 
                                                    sel_chs=CONSTANT['BCIC2b']['sel_chs'])
    if run_independent:
        prep.BCIC2b.fbcsp.subject_independent_setting(k_folds=k_folds,
                                                    pick_smp_freq=pick_smp_freq, 
                                                    n_components=n_components,
                                                    bands=bands, 
                                                    n_features=n_features,
                                                    order=order, 
                                                    save_path=save_path, 
                                                    num_class=num_class, 
                                                    sel_chs=CONSTANT['BCIC2b']['sel_chs'])

elif args.dataset == 'BNCI2015_001':
    print("============== The {} dataset is being prepared ==========".format(args.dataset))
    if run_dependent:
        prep.BNCI2015_001.fbcsp.subject_dependent_setting(k_folds=k_folds,
                                                        pick_smp_freq=pick_smp_freq, 
                                                        n_components=n_components,
                                                        bands=bands, 
                                                        n_features=n_features,
                                                        order=order, 
                                                        save_path=save_path, 
                                                        num_class=num_class, 
                                                        sel_chs=CONSTANT['BNCI2015_001']['sel_chs'])   
    if run_independent:
        prep.BNCI2015_001.fbcsp.subject_independent_setting(k_folds=k_folds,
                                                        pick_smp_freq=pick_smp_freq, 
                                                        n_components=n_components,
                                                        bands=bands, 
                                                        n_features=n_features,
                                                        order=order, 
                                                        save_path=save_path, 
                                                        num_class=num_class, 
                                                        sel_chs=CONSTANT['BNCI2015_001']['sel_chs'])
elif args.dataset == 'SMR_BCI':
    print("============== The {} dataset is being prepared ==========".format(args.dataset))
    if run_independent:
        prep.SMR_BCI.fbcsp.subject_independent_setting(k_folds=k_folds,
                                                       pick_smp_freq=pick_smp_freq, 
                                                       n_components=n_components,
                                                       bands=bands, 
                                                       n_features=n_features,
                                                       order=order, 
                                                       save_path=save_path, 
                                                       num_class=num_class, 
                                                       sel_chs=CONSTANT['SMR_BCI']['sel_chs'])
    if run_dependent:
        prep.SMR_BCI.fbcsp.subject_dependent_setting(k_folds=k_folds,
                                                     pick_smp_freq=pick_smp_freq, 
                                                     n_components=n_components,
                                                     bands=bands, 
                                                     n_features=n_features,
                                                     order=order, 
                                                     save_path=save_path, 
                                                     num_class=num_class, 
                                                     sel_chs=CONSTANT['SMR_BCI']['sel_chs'])
elif args.dataset == 'HighGamma':
    print("============== The {} dataset is being prepared ==========".format(args.dataset))
    if run_dependent:
        prep.HighGamma.fbcsp.subject_dependent_setting(k_folds=k_folds,
                                                    pick_smp_freq=pick_smp_freq, 
                                                    n_components=n_components,
                                                    bands=bands, 
                                                    n_features=n_features,
                                                    order=order, 
                                                    save_path=save_path, 
                                                    num_class=num_class, 
                                                    sel_chs=CONSTANT['HighGamma']['sel_chs'])
    if run_independent:
        prep.HighGamma.fbcsp.subject_independent_setting(k_folds=k_folds,
                                                    pick_smp_freq=pick_smp_freq, 
                                                    n_components=n_components,
                                                    bands=bands, 
                                                    n_features=n_features,
                                                    order=order, 
                                                    save_path=save_path, 
                                                    num_class=num_class, 
                                                    sel_chs=CONSTANT['HighGamma']['sel_chs'])
elif args.dataset == 'OpenBMI':
    print("============== The {} dataset is being prepared ==========".format(args.dataset))    
    if run_dependent:
        prep.OpenBMI.fbcsp.subject_dependent_setting(k_folds=k_folds,
                                                     pick_smp_freq=pick_smp_freq, 
                                                     n_components=n_components,
                                                     bands=bands, 
                                                     n_features=n_features,
                                                     order=order, 
                                                     save_path=save_path, 
                                                     num_class=num_class, 
                                                     sel_chs=CONSTANT['OpenBMI']['sel_chs'])
    if run_independent:
        prep.OpenBMI.fbcsp.subject_independent_setting(k_folds=k_folds,
                                                       pick_smp_freq=pick_smp_freq, 
                                                       n_components=n_components,
                                                       bands=bands, 
                                                       n_features=n_features,
                                                       order=order, 
                                                       save_path=save_path, 
                                                       num_class=num_class, 
                                                       sel_chs=CONSTANT['OpenBMI']['sel_chs'])
else:
    raise Exception('Path Error: {} does not exist, please correct the dataset name.'.format(args.dataset))