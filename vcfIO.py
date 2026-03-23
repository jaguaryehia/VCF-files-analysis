from vcfHandel import *


class vcfIO:
    def __init__(self, vcf_file):
        self.Data = read_vcf(vcf_file)

    def print_header(self):
        # print pandas column names
        print(self.Data.columns.values)

    def return_sample_values(self, sample_name):
        return return_sample_values(self.Data, sample_name)

    def return_samples_values(self, samples):
        values = []
        for sample in samples:
            values.append(self.return_sample_values(sample))
        return values
    def return_sample_row(self,sample_name,nameOfValue):
        return return_sample_by_row(self.Data,sample_name,nameOfValue)