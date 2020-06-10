# -*- coding: utf-8 -*-
#################################
## extract as type and as site ##
#################################

# import modules
import os
import sys
import time
import argparse

# import parameter
parser = argparse.ArgumentParser()
parser.add_argument("-AS",help="AS file from rMATS")
#parser.add_argument("-type",help=" 'gtf' or 'gff' ")
args = parser.parse_args()

if args.AS:
    print("Loading alternative splicing site files %s" % args.AS)
else:
    print("Error: no specific alternative splicing dir")
    sys.exit(1)

dir_now = os.getcwd()
dir_as = args.AS
filenames = os.listdir(dir_as)



for i in filenames:
    file_in_path = dir_as+i
    file_out_path = 'out/as/'+i
    file_in = open(file_in_path,'r').readlines()
    file_out = open(file_out_path,'w')
    for line in file_in:
        line_sets = line.split('\t')
        geneid = line_sets[1]
        genename = line_sets[2]
        chromosome = line_sets[3]
        strand = line_sets[4]
        #print(chromosome)
        if line_sets[0] == "ID":
            continue
        else:
            if i.split(".")[0] == "A3SS":
                pvalue = line_sets[18]
                inlevel1 = line_sets[20]
                inlevel2 = line_sets[21]
                if float(pvalue) <= 0.05:
                    if line_sets[4] == "+":
                        splice_site1 = line_sets[5]
                        splice_site2 = line_sets[7]
                    if line_sets[4] == "-":
                        splice_site1 = line_sets[6]
                        splice_site2 = line_sets[8]
                    seq = geneid+"\t"+strand+"\t"+genename+"\t"+chromosome+"\t"+splice_site1+"\t"+splice_site2+"\t"+"NA"+"\t"+"NA"+"\t"+pvalue+"\t"+inlevel1+'\t'+inlevel2
                    file_out.writelines(seq+"\n")
                else:
                    continue
            if i.split(".")[0] == "A5SS":
                pvalue = line_sets[18]
                inlevel1 = line_sets[20]
                inlevel2 = line_sets[21]
                if float(pvalue)<=0.05:
                    if line_sets[4] == "+":
                        splice_site1 = line_sets[8]
                        splice_site2 = line_sets[6]
                    if line_sets[4] == "-":
                        splice_site1 = line_sets[7]
                        splice_site2 = line_sets[5]
                    seq = geneid+"\t"+strand+"\t"+genename+"\t"+chromosome+"\t"+splice_site1+"\t"+splice_site2+"\t"+"NA"+"\t"+"NA"+"\t"+pvalue+"\t"+inlevel1+'\t'+inlevel2
                    file_out.write(seq+"\n")
                else:
                    continue
            if i.split(".")[0] == "MXE":
                pvalue = line_sets[20]
                inlevel1 = line_sets[22]
                inlevel2 = line_sets[23]
                if float(pvalue) <= 0.05:
                    splice_site1 = line_sets[5]
                    splice_site2 = line_sets[6]
                    splice_site3 = line_sets[7]
                    splice_site4 = line_sets[8]
                    seq1 = geneid+"\t"+strand+"\t"+genename+"\t"+chromosome+"\t"+splice_site1+"\t"+splice_site2+"\t"+splice_site3+"\t"+splice_site4+"\t"+pvalue+"\t"+inlevel1+'\t'+inlevel2
                    #seq2 = geneid+"\t"+strand+"\t"+genename+"\t"+chromosome+"\t"+splice_site3+"\t"+splice_site4+"\t"+pvalue
                    seq = seq1
                    file_out.write(seq+"\n")
                else:
                    continue
            if i.split(".")[0] == "SE":
                pvalue = line_sets[18]
                inlevel1 = line_sets[20]
                inlevel2 = line_sets[21]
                if float(pvalue) <= 0.05:
                    splice_site1 = line_sets[5]
                    splice_site2 = line_sets[6]
                    seq = geneid+"\t"+strand+"\t"+genename+"\t"+chromosome+"\t"+splice_site1+"\t"+splice_site2+"\t"+"NA"+"\t"+"NA"+"\t"+pvalue+"\t"+inlevel1+'\t'+inlevel2
                    file_out.write(seq+"\n")
                else:
                    continue
            if i.split(".")[0] == "RI":
                pvalue = line_sets[18]
                inlevel1 = line_sets[20]
                inlevel2 = line_sets[21]
                if float(pvalue)<=0.05:
                    splice_site1 = line_sets[8]
                    splice_site2 = line_sets[9]
                    seq = geneid+"\t"+strand+"\t"+genename+"\t"+chromosome+"\t"+splice_site1+"\t"+splice_site2+"\t"+"NA"+"\t"+"NA"+"\t"+pvalue+"\t"+inlevel1+'\t'+inlevel2
                    file_out.write(seq+"\n")
                else:
                    continue
            else:
                pass
    file_out.close()

filenames1 = os.listdir("out/as/")
file_as_out = open('out/as.txt','a+')
for i in filenames1:
    path_in = "out/as/"+i
    file_in = open(path_in,'r')
    as_type = i.split(".")[0]
    for line in file_in.readlines():
        file_as_out.writelines(line.strip()+"\t"+as_type+"\n")
file_as_out.close()

print("Step3 is done")