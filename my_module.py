import numpy as np

from data import country_codes, neighb

native_english_speaking = [5142, 5309, 5502, 5303, 5305, 5526, 5314, 5326, 5339, 5308, 
                           5352, 5514, 5625, 5347, 5311, 5374, 5170, 5390]



#Year, Age, Area, Natio, Amount

def read_csv_file():
    filename = './befkbhalderstatkode.csv'
    dd = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
    return dd

def no_english_non_english():
    dd = read_csv_file()
    
    eng_mask = [i in native_english_speaking for i in dd[:,3]]
    
    no_english = np.array([dd[(dd[:,0] == n) & eng_mask][:,4].sum() for n in dd[:,0]])
    
    total = np.array([dd[dd[:,0] == n][:,4].sum() for n in dd[:,0]])
    
    no_non_english = total - no_english 
    
    return no_english, no_non_english

def filtered_data(dataset, mask):
    return dataset[mask]

def get_data_by_x(dataset, x_value):
    data_dict = {n:dataset[dataset[:,x_value] == n][:,4].sum() for n in dataset[:,x_value]}
    
    keys = []
    acc_sums = []
    acc_sum = 0
    
    for k,v in sorted(data_dict.items(),key=lambda x:x[0]):
        acc_sum += v
        keys.append(k)
        acc_sums.append(acc_sum)
    
    return np.array(keys[:]+acc_sums[:]).reshape(2,len(keys))