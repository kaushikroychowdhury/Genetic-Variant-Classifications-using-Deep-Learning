# IMPORTING RELEVANT LIBRARIES
import pandas as pd
pd.set_option('display.expand_frame_repr', False)

#loading the data

raw_data = pd.read_csv("clinvar_conflicting.csv")
#print(raw_data.head())
#print('\n')
#print(raw_data.describe(include='all'))

cols_to_remove = ['REF', 'ALT', 'CLNDISDB','CLNDISDBINCL','CLNDN','CLNDNINCL','CLNHGVS','CLNSIGINCL','CLNVC','CLNVI','MC','SSR','Allele','Consequence','IMPACT','SYMBOL','Feature_type','Feature','BIOTYPE','EXON','INTRON','Amino_acids','Codons','DISTANCE','BAM_EDIT','SIFT','PolyPhen','MOTIF_NAME','MOTIF_POS','HIGH_INF_POS','MOTIF_SCORE_CHANGE','LoFtool','cDNA_position','CDS_position','Protein_position','BLOSUM62']
data = raw_data.drop(cols_to_remove, axis=1)

# print(data.head())
# print('\n')
# print(data.describe(include='all'))

#print(data.isnull().sum())

data_without_mv = data.dropna(axis=0)

# print(data_without_mv.isnull().sum())
# print(data_without_mv.describe())

#cols = list(data_without_mv.columns.values)
cols = ['CHROM', 'POS', 'AF_ESP', 'AF_EXAC', 'AF_TGP', 'ORIGIN', 'STRAND', 'CADD_PHRED', 'CADD_RAW', 'CLASS']
data_without_mv = data_without_mv[cols]

#print(data_without_mv.columns.values)
#print(data_without_mv.head())

data_without_mv = data_without_mv[data_without_mv.CHROM != 'X']
data_without_mv = data_without_mv[data_without_mv.CHROM != 'MT']
data_without_mv.to_csv("clinvar_conflicting_cleaned.csv", header = False, index = False)
