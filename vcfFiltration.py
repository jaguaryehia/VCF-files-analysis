from vcfIO import vcfIO


class VCFFiltration(vcfIO):

    def returnToDataFrame(self,dataframe, position):
        return dataframe.iloc[position]

    def dictionary(self, dataframe):
        dic = dict()
        for i, index in enumerate(dataframe.index.tolist()):
            dic[index] = dataframe.iloc[i]['INFO']
        return dic

    def DP_Filtration(self, dic):
        matched_data = []
        for key, value in dic.items():
            data_dictionary = {}
            for item in value.split(';'):
                split_item = item.split('=')
                if len(split_item) == 2:
                    data_dictionary[split_item[0]] = split_item[1]

            if int(data_dictionary.get('DP', '30')) >= 30:
                matched_data.append(key)

        return matched_data

    def AD_Filtration(self,dic):
        matched_data = []
        for key, value in dic.items():
            if int(value[1].split(',')[0]) >= 3 and int(value[1].split(',')[1]) >= 3:
                matched_data.append(key)
        return matched_data

    def AF_Filtration(self,dic, low, high):
        matched_data = []
        for key, value in dic.items():
            if ((float(value[2]) * 100) >= low) and ((float(value[2]) * 100) <= high):
                matched_data.append(key)
        return matched_data

