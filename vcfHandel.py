from collections import OrderedDict
import gzip
import pandas as pd

def read_vcf(filename):
    print(filename)
    if filename.endswith('.gz'):
        f = gzip.open(filename, 'rt')
    else:
        f = open(filename, 'r')
    header = []
    data = []
    for line in f:
        if line.startswith('#CHROM'):
            header.append(line.strip())
        if line.startswith('#'):
            continue
        else:
            data.append(line.strip())
    f.close()
    header = header[0].split('\t')
    data = [line.split('\t') for line in data]
    df = pd.DataFrame(data, columns=header)
    return df

def return_sample_values(Data, sample_name):
    return Data[sample_name].values

def return_sample_by_row(Data,sample_name_col,name_of_sample):
    return Data.
