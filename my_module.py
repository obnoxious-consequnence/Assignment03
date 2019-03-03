import numpy as np
from data import country_codes, neighb

native_english_speaking = [5142, 5309, 5502, 5303, 5305, 5526, 5314, 5326, 5339, 5308, 
                           5352, 5514, 5625, 5347, 5311, 5374, 5170, 5390]
# Part 02
def read_csv_file():
    filename = './befkbhalderstatkode.csv'
    dd = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
    return dd

# Part 03
def no_english_non_english():
    
    dd = read_csv_file()
   
    eng_mask = [i in native_english_speaking for i in dd[:,3]]
    
    no_english = np.array([dd[(dd[:,0] == n) & eng_mask][:,4].sum() for n in list(set(dd[:,0]))])
    
    total = np.array([dd[dd[:,0] == n][:,-1].sum() for n in list(set(dd[:,0]))])
    no_non_english = total - no_english
    
    return no_english, no_non_english

"""def numOfCit(array,year):
    #englishNative =[5142, 5309, 5502, 5303, 5305, 5526, 5314, 5326, 5339, 5308, 5352, 5514, 5625, 5347, 5311, 5374, 5170, 5390]
    #for n in range(len(englishNative)):
    irMask = (array[:,0] == year) & (array[:,3] == 5142)
    antBarMask = (array[:,0] == year) & (array[:,3] == 5309)
    ausMask = (array[:,0] == year) & (array[:,3] == 5502)
    bahaMask = (array[:,0] == year) & (array[:,3] == 5303)
    barbMask = (array[:,0] == year) & (array[:,3] == 5305)
    belMask = (array[:,0] == year) & (array[:,3] == 5526)
    canMask = (array[:,0] == year) & (array[:,3] == 5314)
    doMask = (array[:,0] == year) & (array[:,3] == 5326)
    grenMask = (array[:,0] == year) & (array[:,3] == 5339)
    guyMask = (array[:,0] == year) & (array[:,3] == 5308)
    jaMask = (array[:,0] == year) & (array[:,3] == 5352)
    nzMask = (array[:,0] == year) & (array[:,3] == 5514)
    sknMask = (array[:,0] == year) & (array[:,3] == 5625)
    slMask = (array[:,0] == year) & (array[:,3] == 5347)
    svgMask = (array[:,0] == year) & (array[:,3] == 5311)
    tntMask = (array[:,0] == year) & (array[:,3] == 5374)
    gbMask = (array[:,0] == year) & (array[:,3] == 5170)
    USAMask = (array[:,0] == year) & (array[:,3] == 5390)
    totalMask = (array[:,0] == year)
    englishSum = np.sum(array[irMask][:,4])+np.sum(array[antBarMask][:,4])+np.sum(array[ausMask][:,4])+np.sum(array[bahaMask][:,4])+np.sum(array[barbMask][:,4])+np.sum(array[belMask][:,4])+np.sum(array[canMask][:,4])+np.sum(array[doMask][:,4])+np.sum(array[grenMask][:,4])+np.sum(array[guyMask][:,4])+np.sum(array[jaMask][:,4])+np.sum(array[nzMask][:,4])+np.sum(array[sknMask][:,4])+np.sum(array[slMask][:,4])+np.sum(array[svgMask][:,4])+np.sum(array[tntMask][:,4])+np.sum(array[gbMask][:,4])+np.sum(array[USAMask][:,4])
    return "Sum of english speaking: ",englishSum, "Total non english: ", np.sum(array[totalMask][:,4])-englishSum;
""" 

# Part 04
def filtered_data(data, mask):
    return data[mask]

# Part 05
def get_data_by_x(data, x_value):
    
    data_dict = {n:data[data[:,x_value] == n][:,-1].sum() for n in list(set(data[:,x_value]))}
    
    sorted_data = sorted(list(data_dict.items()),key=lambda x:x[0])
    data2d = np.array(sorted_data)
    
    return data2d

# Credit for assistance: Anxious Depression