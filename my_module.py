import numpy as np

from data import country_codes, neighb

native_english_speaking = [5142, 5309, 5502, 5303, 5305, 5526, 5314, 5326, 5339, 5308, 
                           5352, 5514, 5625, 5347, 5311, 5374, 5170, 5390]
# part 2
def read_csv_file():
    filename = './befkbhalderstatkode.csv'
    dd = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
    return dd

# part 3
def no_english_non_english():
    dd = read_csv_file()
    
    eng_mask = [i in native_english_speaking for i in dd[:,3]]
    
    no_english = np.array([dd[(dd[:,0] == n) & eng_mask][:,-1].sum() for n in list(set(dd[:,0]))])
    
    total = np.array([dd[dd[:,0] == n][:,-1].sum() for n in list(set(dd[:,0]))])
    no_non_english = total - no_english
    
    return no_english, no_non_english
# part 4
def filtered_data(data, mask):
    return data[mask]

# part 5
def get_data_by_x(data, x_value):
    # sum data for same xkey
    data_dict = {n:data[data[:,x_value] == n][:,-1].sum() for n in list(set(data[:,x_value]))}
    
    sorted_data = sorted(list(data_dict.items()),key=lambda x:x[0])
    data2d = np.array(sorted_data)
    
    return data2d