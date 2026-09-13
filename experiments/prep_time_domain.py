import argparse
import mixnet.preprocessing as prep
from mixnet.preprocessing.config import CONSTANT

'''

1. In case of preparing a particular dataset, please run the script as an example: python prep_time_domain.py --dataset 'BCIC2a'
2. In case of preparing multiple datasets, please run the script as an example: python prep_time_domain.py --dataset 'BCIC2a' && python prep_time_domain.py --dataset 'BCIC2b' && python prep_time_domain.py --dataset 'BNCI2015_001' && python prep_time_domain.py --dataset 'SMR_BCI' && python prep_time_domain.py --dataset 'HighGamma' && python prep_time_domain.py --dataset 'OpenBMI'
3. In case of preparing only a particular setting, please add the --setting argument (dependent/independent/both, default: both) as an example: python prep_time_domain.py --dataset 'BCIC2a' --setting 'dependent'

'''
k_folds = 5
pick_smp_freq = 100
bands = [8, 30]
order = 5
save_path = 'datasets'
num_class = 2

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, default='BCIC2a', help='dataset name: ex. [BCIC2a/BCIC2b/BNCI2015_001/SMR_BCI/HighGamma/OpenBMI]')
parser.add_argument('--setting', type=str, default='both', choices=['dependent', 'independent', 'both'], help='which setting to prepare: subject dependent, subject independent, or both')
args = parser.parse_args()

run_dependent = args.setting in ['dependent', 'both']
run_independent = args.setting in ['independent', 'both']

if args.dataset == 'BCIC2a':
    print("============== The {} dataset is being prepared ==========".format(args.dataset))
    if run_dependent:
        prep.BCIC2a.time_domain.subject_dependent_setting(k_folds=k_folds,
                                                          pick_smp_freq=pick_smp_freq, 
                                                          bands=bands, 
                                                          order=order, 
                                                          save_path=save_path, 
                                                          num_class=num_class, 
                                                          sel_chs=CONSTANT['BCIC2a']['sel_chs'])
    
    if run_independent:
        prep.BCIC2a.time_domain.subject_independent_setting(k_folds=k_folds,
                                                            pick_smp_freq=pick_smp_freq, 
                                                            bands=bands, 
                                                            order=order, 
                                                            save_path=save_path, 
                                                            num_class=num_class, 
                                                            sel_chs=CONSTANT['BCIC2a']['sel_chs'])
elif args.dataset == 'BCIC2b':  
    print("============== The {} dataset is being prepared ==========".format(args.dataset))
    if run_dependent:
        prep.BCIC2b.time_domain.subject_dependent_setting(k_folds=k_folds,
                                                            pick_smp_freq=pick_smp_freq, 
                                                            bands=bands, 
                                                            order=order, 
                                                            save_path=save_path, 
                                                            num_class=num_class, 
                                                            sel_chs=CONSTANT['BCIC2b']['sel_chs'])
    
    if run_independent:
        prep.BCIC2b.time_domain.subject_independent_setting(k_folds=k_folds,
                                                          pick_smp_freq=pick_smp_freq, 
                                                          bands=bands, 
                                                          order=order, 
                                                          save_path=save_path, 
                                                          num_class=num_class, 
                                                          sel_chs=CONSTANT['BCIC2b']['sel_chs'])
    
elif args.dataset == 'BNCI2015_001':
    print("============== The {} dataset is being prepared ==========".format(args.dataset))    
    if run_dependent:
        prep.BNCI2015_001.time_domain.subject_dependent_setting(k_folds=k_folds,
                                                           pick_smp_freq=pick_smp_freq, 
                                                           bands=bands, 
                                                           order=order, 
                                                           save_path=save_path, 
                                                           num_class=num_class, 
                                                           sel_chs=CONSTANT['BNCI2015_001']['sel_chs'])
    
    if run_independent:
        prep.BNCI2015_001.time_domain.subject_independent_setting(k_folds=k_folds,
                                                             pick_smp_freq=pick_smp_freq, 
                                                             bands=bands, 
                                                             order=order, 
                                                             save_path=save_path, 
                                                             num_class=num_class, 
                                                             sel_chs=CONSTANT['BNCI2015_001']['sel_chs'])

elif args.dataset == 'SMR_BCI':  
    print("============== The {} dataset is being prepared ==========".format(args.dataset))
    if run_dependent:
        prep.SMR_BCI.time_domain.subject_dependent_setting(k_folds=k_folds,
                                                           pick_smp_freq=pick_smp_freq, 
                                                           bands=bands, 
                                                           order=order, 
                                                           save_path=save_path, 
                                                           num_class=num_class, 
                                                           sel_chs=CONSTANT['SMR_BCI']['sel_chs'])
    
    if run_independent:
        prep.SMR_BCI.time_domain.subject_independent_setting(k_folds=k_folds,
                                                             pick_smp_freq=pick_smp_freq, 
                                                             bands=bands, 
                                                             order=order, 
                                                             save_path=save_path, 
                                                             num_class=num_class, 
                                                             sel_chs=CONSTANT['SMR_BCI']['sel_chs'])

elif args.dataset == 'HighGamma':
    print("============== The {} dataset is being prepared ==========".format(args.dataset))
    if run_dependent:
        prep.HighGamma.time_domain.subject_dependent_setting(k_folds=k_folds,
                                                           pick_smp_freq=pick_smp_freq, 
                                                           bands=bands, 
                                                           order=order, 
                                                           save_path=save_path, 
                                                           num_class=num_class, 
                                                           sel_chs=CONSTANT['HighGamma']['sel_chs'])
    
    if run_independent:
        prep.HighGamma.time_domain.subject_independent_setting(k_folds=k_folds,
                                                             pick_smp_freq=pick_smp_freq, 
                                                             bands=bands, 
                                                             order=order, 
                                                             save_path=save_path, 
                                                             num_class=num_class, 
                                                             sel_chs=CONSTANT['HighGamma']['sel_chs'])

elif args.dataset == 'OpenBMI': 
    print("============== The {} dataset is being prepared ==========".format(args.dataset))
    if run_dependent:
        prep.OpenBMI.time_domain.subject_dependent_setting(k_folds=k_folds,
                                                           pick_smp_freq=pick_smp_freq, 
                                                           bands=bands, 
                                                           order=order, 
                                                           save_path=save_path, 
                                                           num_class=num_class, 
                                                           sel_chs=CONSTANT['OpenBMI']['sel_chs'])
    
    
    if run_independent:
        prep.OpenBMI.time_domain.subject_independent_setting(k_folds=k_folds,
                                                             pick_smp_freq=pick_smp_freq, 
                                                             bands=bands, 
                                                             order=order, 
                                                             save_path=save_path, 
                                                             num_class=num_class, 
                                                             sel_chs=CONSTANT['OpenBMI']['sel_chs'])
    
else:
    raise Exception('Path Error: {} does not exist, please correct the dataset name.'.format(args.dataset))