import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-ann",help="gtf or gff file from ensembl or NCBI")
parser.add_argument("-type",help=" 'gtf' or 'gff' ")
parser.add_argument("-exp",help=" exp file dir ")
parser.add_argument("-female",help=" female sample ")
parser.add_argument("-male",help=" male sample ")
parser.add_argument("-AS",help="AS file from rMATS")
parser.add_argument("-info",help="remarks of sample")
parser.add_argument("-out",help="out of process")
args = parser.parse_args()
#####################################
process_seq1 = "python src/step1.py -ann "+" "+args.ann+" "+"-type "+" "+ args.type
os.system(process_seq1)
#####################################
process_seq2 = "Rscript src/step2.R "+" "+args.exp+" "+args.female+" "+args.male
os.system(process_seq2)
#####################################
process_seq3 = "python src/step3.py -AS "+" "+args.AS
os.system(process_seq3)
#####################################
a = os.path.getsize('out/as.txt')
if str(a) == "0":
    try:
        sys.exit(0)
    except:
        print('AS file is NA')
    finally:
        print('clean-up, program quit')
#####################################
if str(a) != "0":
    process_seq4 = "Rscript src/step4.R " + " "+args.info+" "+args.out
    os.system(process_seq4)