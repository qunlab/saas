################################################
## extract id and symbol from gtf or gff file ##
################################################

# load module
import os
import sys
import argparse
# pass parameter
parser = argparse.ArgumentParser()
parser.add_argument("-ann",help="gtf or gff file from ensembl or NCBI")
parser.add_argument("-type",help=" 'gtf' or 'gff' ")
args = parser.parse_args()

if args.ann:
    print("Loading anntation file...")
else:
    print("Error: no specific anntation file")
    sys.exit(1)

if args.type:
    print("File type:%s \nPlease waite" %args.type)
else:
    print("Error: no specific extract type 'gtf' or 'gff' ")
    sys.exit(1)

# files
dir_now = os.getcwd()
if not os.path.exists("out"):
    os.makedirs("out")
if not os.path.exists("out/as"):
    os.makedirs("out/as")
if not os.path.exists("out/exp"):
    os.makedirs("out/exp")
if os.path.exists("out/as.txt"):
    os.remove("out/as.txt")
path_in = dir_now+"/"+args.ann
file_out = open("out/exp/symbol.txt","w+")
file_out.writelines("chr"+"\t"+"id"+"\t"+"symbol"+"\n")
# if not os.path.exists("symbol.txt"):
    # file_out = open("out/exp/symbol.txt","w+")
    # file_out.writelines("chr"+"\t"+"id"+"\t"+"symbol"+"\n")
# else:
    # os.remove("symbol.txt")
    # file_out = open("out/exp/symbol.txt","w+")
    # file_out.writelines("chr"+"\t"+"id"+"\t"+"symbol"+"\n")
file_in =open(path_in,"r").readlines()
for line in file_in:
    if line[0] == "#":
        pass
    else:
        line_sets = line.split('\t')
        if args.type == "gtf":
            if line_sets[2] == "gene":
                chromosome = line_sets[0].strip()
                geneid = line_sets[8].split(";")[0].split('"')[1].strip()
                genename = line_sets[8].split(";")[1].split('"')[1].strip()
                result=line_sets[8].find('gene_name')>=0
                #print(result)
                if result == True:
                    genename = line_sets[8].split("gene_name")[1].split('"')[1].strip()
                else:
                    genename = geneid
                seq = chromosome+'\t'+geneid+'\t'+genename
                file_out.writelines(seq+'\n')
            else:
                pass
        elif args.type == "gff":
            if line_sets[2] == "gene":
                chromosome = line_sets[0].strip()
                geneid = line_sets[8].split("ID=")[1].split(";")[0]
                genename = line_sets[8].split("Name=")[1].split(";")[0]
                seq = chromosome+'\t'+geneid+'\t'+genename
                file_out.writelines(seq+'\n')
            else:
                pass
        else:
            print("please specific type")
            sys.exit(1)
print("Step1 is done")
file_out.close()
