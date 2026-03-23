import pandas as pd
import gzip
import os

"""
    this function read file vcf and return it to dataframe
        input:
            :param Data - pandas dataframe : vcf data
        output:
            :return vcf : vcf as dataframe
"""


def read_vcf(filename):
    print(filename)
    if filename.endswith('.vcf.gz'):
        try:
            f = gzip.open(filename, 'rt', encoding='utf-8')
            # Check the gzip header to confirm if the file is valid
            f.read(1)
            f.seek(0)
        except OSError:
            f = open(filename, 'r', encoding='utf-8')
    elif filename.endswith('.vcf'):
        f = open(filename, 'r', encoding='utf-8')
    else:
        raise ValueError("Invalid file extension: {}".format(filename))

    header = []
    data1 = []
    data2 = []
    for line in f:
        if line.startswith('#CHROM'):
            header.append(line.strip())
        if line.startswith('#'):
            data2.append(line)
        else:
            data1.append(line.strip())
    f.close()
    header = header[0].split('\t')
    data1 = [line.split('\t') for line in data1]
    dataframe = pd.DataFrame(data1, columns=header)
    return dataframe, data2


"""
    this function get dataframe and convert it to dictionary
        input:
            :param Data - pandas dataframe : vcf data 
        output:
            :return : dict() that has the key and value for comparing 
"""


def dictionary(dataframe):
    dic = dict()
    for i, index in enumerate(dataframe.index.tolist()):
        dic[index] = dataframe.iloc[i][-1].split(":")
    return dic


"""
    this function get dataframe and position numbers after comparing to get them from the dataframe
        input:
            :param Data - pandas dataframe : vcf data
            :param Position - position numbers : list of positions numbers
        output:
            :return : dataframe that has the target positions 
"""


def returnToDataFrame(dataframe, position):
    return dataframe.iloc[position]


"""
    this function get dictionary of the dataframe and splitting and compare the condition that has 
    the target positions indexes
        input:
            :param Data - pandas dataframe : vcf data
            :param Data - low the lowest number of the range that user want to compare
            :param Data - high the highest number of the range that user want to compare

        output:
            :return : list that has the target positions indexes 
"""


def fromOneToThirty(dic, low, high):
    matched_data = []
    for key, value in dic.items():
        if ((float(value[2]) * 100) >= low) and ((float(value[2]) * 100) <= high):
            matched_data.append(key)
    return matched_data


"""
    this function write the target vcf data
        input:
            :param data_frame - pandas dataframe
            :param filename - the new filename for the target vcf
            :param rest_data - the rest of the data in the file
        output:
            :return : vcf file 
"""


def write_vcf(data_frame, filename, rest_data):
    if filename.endswith('.gz'):
        f = gzip.open(filename, 'wt')
    else:
        f = open(filename, 'w')
    header = ''.join([i for i in rest_data])
    f.write(header)
    for index, row in data_frame.iterrows():
        f.write('\t'.join(row.values.tolist()) + '\n')
    f.close()


"""
    this function call the all functions take  only the directory
        input:
            :param directory_name - directory name
        output:
            :return : list of files that in the target directory
"""


def getDirectory(directory_name):
    vcf_files = [file for file in os.listdir(directory_name)
                 if file.endswith('.vcf') or file.endswith('vcf.gz')]
    return vcf_files


"""
    this function call the all functions take  only the directory
        input:
            :param directory_name - directory name
        output:
            write the file with the same name with counter
"""


def main(dictionary_name, save_folder):
    os.makedirs(os.path.join(save_folder, "filtered data/AF_filtered"), exist_ok=True)
    for i, file_name in enumerate(getDirectory(dictionary_name)):
        df, data = read_vcf(os.path.join(dictionary_name, file_name))
        # the function calling fromOneToThirty has two const numbers that you can change them 1.0,30.0
        write_vcf(returnToDataFrame(df, fromOneToThirty(dictionary(df), 1.0, 30.0)),
                  os.path.join(os.path.join(save_folder, "filtered data/AF_filtered"), file_name + '.vcf'),
                  data)


"""

 calling all the functions in main

"""

if __name__ == '__main__':
    main('new_vcf_file_to_filtered', 'new_vcf_file_to_filtered')
