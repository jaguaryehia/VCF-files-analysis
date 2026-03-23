import vcfIO

DataFile="MP.vcf"

vcf = vcfIO.vcfIO(DataFile)
print(vcf.Data)
#print(vcf.Data)
# return EY0050481 EY0050482 EY0050483 EY0050484 values
# print(vcf.return_samples_values(("EY0050481", "EY0050482", "EY0050483", "EY0050484")))
print(vcf.return_sample_row('NC_030808.1'))
#print(vcf.return_sample_values('EY0050481'))
# print header
#vcf.print_header()