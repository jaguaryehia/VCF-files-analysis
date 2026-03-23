import gzip
import pandas as pd
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
    f = None
    if filename.endswith('.vcf.gz'):
        f = open(filename, 'rt',errors="ignore")
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
    return dataframe[['POS', 'INFO']].set_index('POS').to_dict()['INFO']


"""
    this function get dataframe and position numbers after comparing to get them from the dataframe
        input:
            :param Data - pandas dataframe : vcf data
            :param Position - position numbers : list of positions numbers
        output:
            :return : dataframe that has the target positions
"""


def returnToDataFrame(dataframe, position):
    return dataframe[dataframe['INFO'].isin(position)]


"""
    this function get dictionary of the dataframe and splitting and compare the condition that has the target DP
        input:
            :param Data - pandas dataframe : vcf data
        output:
            :return : dataframe that has the target DP
"""


def splittingAndComparing(dic):
    matched_data = set()
    for key, value in dic.items():
        data_dictionary = {}
        for item in value.split(';'):
            split_item = item.split('=')
            if len(split_item) == 2:
                data_dictionary[split_item[0]] = split_item[1]

        if int(data_dictionary.get('DP', '30')) >= 30:
            matched_data.add(value)

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
                 if file.endswith('.vcf.gz')]
    return vcf_files


"""
    this function call the all functions take  only the directory
        input:
            :param directory_name - directory name
        output:
            write the file with the same name with counter
"""


def main(dictionary_name):
    for i in range(len(getDirectory(dictionary_name))):
        df, data = read_vcf(os.path.join(dictionary_name, getDirectory(dictionary_name)[i]))
        write_vcf(returnToDataFrame(df, splittingAndComparing(dictionary(df))),
                  getDirectory(dictionary_name)[i] + '(' + str(i) + ')' + '.vcf', data)


"""

    calling all the functions in main

"""

if __name__ == '__main__':
    main('VCF files/')
