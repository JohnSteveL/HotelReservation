from scipy.stats import randint,uniform

LIGHTGBM_PARAMS = {
    'n_estimators' : randint(100,500),
    'max_depth' : randint(10,70),
    'learning_rate' : uniform(0.01,0.02),
    'num_leaves' : randint(10,90),
    'boosting_type' : ['gbdt' , 'dart' , 'goss']
}

RANDOM_SEARCH_PARAMS = {
    'n_iter' : 2,
    'cv' : 2,
    'n_jobs' : -1,
    'verbose': 2,
    'random_state' : 42,
    'scoring' : 'accuracy'
}