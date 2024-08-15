from min2net.models import *
from min2net.loss import *
from min2net.utils import dotdict
from tensorflow.keras.optimizers import Adam
from os import path

def get_params(dataset, train_type, data_type, num_class, num_chs, adaptive_gradient=False, policy=None, loss_weights=None, log_dir='logs', **kwargs):
    
    model_name  = 'SpectralSpatialCNN'
    n_subjects   = 9  if dataset == 'BCIC2a' else \
                   9  if dataset == 'BCIC2b' else \
                   12 if dataset == 'BNCI2015_001' else \
                   14 if dataset == 'SMR_BCI' else \
                   14 if dataset == 'HighGamma' else \
                   54 if dataset == 'OpenBMI' else 0
    
    if num_chs == 3:
        input_shape = (11,11,1)
    else:
        if dataset == 'SMR_BCI':
            input_shape  = (23,23,1) 
        elif dataset == 'BNCI2015_001':
            input_shape  = (21,21,1) 
        elif dataset == 'BCIC2b':
            input_shape  = (11,11,1) 
        else: 
            input_shape = (28,28,1)
    loss_weights = [1.] if loss_weights == None else loss_weights
    
    # The below log_path use 
    # log_path = '{}/{}/{}_{}_classes_{}'.format(log_dir, 
    #                                                 model_name, 
    #                                                 train_type, 
    #                                                 str(num_class), 
    #                                                 dataset)
    log_path = '{}/{}/{}_{}'.format(log_dir, 
                                                    model_name, 
                                                    train_type,  
                                                    dataset)
    
    if train_type == 'subject_dependent':
        factor = 0.5
        es_patience = 20
        lr = 0.00001
        min_lr = 0.00001
        batch_size = 32 if dataset == 'HighGamma' or dataset == 'BCIC2b' or dataset == 'BNCI2015_001' else 10 # 10 for other datasets
        patience = 5
        epochs = 200
        min_epochs = 0
        dropout_rate = 0.5
    elif train_type == 'subject_independent':
        factor = 0.5
        es_patience = 20
        lr = 0.00001
        min_lr = 0.00001
        batch_size = 100 #100
        patience = 5
        epochs = 200
        min_epochs = 0
        dropout_rate = 0.5
        
    params = dotdict({
                'model': SpectralSpatialCNN,
                'model_params': dotdict({
                        'model_name': model_name, 
                        'input_shape': input_shape,
                        'class_balancing': True,
                        'f1_average': 'macro',
                        'num_class': num_class, 
                        'loss': [SparseCategoricalCrossentropy()],
                        'loss_names': ['crossentropy'],
                        'loss_weights': loss_weights,
                        'epochs': epochs,
                        'batch_size': batch_size,
                        'dropout_rate': dropout_rate,
                        'optimizer': Adam(beta_1=0.9, beta_2=0.999, epsilon=1e-08),
                        'lr': lr,
                        'min_lr': min_lr,
                        'factor': factor,
                        'patience': patience,
                        'es_patience': es_patience,
                        'min_epochs': min_epochs,
                        'verbose': 1, 
                        'log_path': log_path,
                        'data_format': 'channels_last'
                }),

                'data_params': dotdict({
                        'dataset': dataset,
                        'train_type': train_type,
                        'data_format': 'NSHWD',
                        'data_type': data_type,
                        'dataset_path': 'datasets',
                        'n_subjects': n_subjects,
                        'n_folds': 5,
                        'num_class': num_class,
                        'load_path': 'datasets/{}/{}/{}_class/'.format(dataset, data_type, num_class)
                }), 
                
                'log_path': log_path
            }) 
    
    return params
  