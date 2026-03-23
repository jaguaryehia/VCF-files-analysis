import seqIO
from seqIO import *
from ExtractList import *


class AnalysisHummer:
    def __init__(self, hammer_file, seq_file, output_file, formatter=100):
        self.formatter = formatter
        self.hammer_file = readHUMMEROutput(hammer_file)
        self.seq_dict = extractSeqFromFastaFile(seq_file, self.hammer_file)
        self.output_file = writeSeqs(self.seq_dict, output_file, formatter)

    def getHUMMER(self):
        return self.hammer_file

    def getSeqDict(self,id_seq, start, end):
        return getGeneByIndex(self.seq_dict,id_seq,start,end)
