# SAAS---Sex-associated Alternative Splicing
## Preparing
**you can process your data with this script, here we provide a demo for users**<br>
**Notes: you can download this script and run it in your computer(need to download gtf/gff files. [Mus_musculus](http://ftp.ensembl.org/pub/release-97/gtf/mus_musculus/Mus_musculus.GRCm38.97.gtf.gz))**
1. [python 3.7](https://www.python.org/)
2. [R 3.6.0](https://cran.r-project.org/mirrors.html)
3. you got your RNA-seq analysis data.--- [example](https://github.com/leequn/saas/tree/master/exp_kidney)
4. you got your alternative splicing analysis data by [rMATS](http://rnaseq-mats.sourceforge.net/).--- [example](https://github.com/leequn/saas/tree/master/as_kidney)
5. sex samples lable. ---[example: female](https://github.com/leequn/saas/blob/master/kidney_female.txt), [example: male](https://github.com/leequn/saas/blob/master/kidney_male.txt)
6. sample information(i.e. development age, tissues).---[example](https://github.com/leequn/saas/blob/master/info_kidney.txt)
7. .gtf/.gff  [example: Mus_musculus](http://ftp.ensembl.org/pub/release-97/gtf/mus_musculus/Mus_musculus.GRCm38.97.gtf.gz)
## Usage
### Example
**Files dir**
```
demo/
├── as_kidney
│   ├── A3SS.MATS.txt
│   ├── A5SS.MATS.txt
│   ├── MXE.MATS.txt
│   ├── RI.MATS.txt
│   └── SE.MATS.txt
├── exp_kidney
│   ├── SRR945382.csv
│   ├── SRR945383.csv
│   ├── SRR945384.csv
│   ├── SRR945385.csv
│   ├── SRR945386.csv
│   ├── SRR945387.csv
│   ├── SRR945388.csv
│   ├── SRR945389.csv
│   ├── SRR945390.csv
│   ├── SRR945391.csv
│   ├── SRR945392.csv
│   └── SRR945393.csv
├── info_kidney.txt
├── kidney_female.txt
├── kidney_male.txt
├── Mus_musculus.GRCm38.97.gtf
├── process.py
├── README
└── src
    ├── step1.py
    ├── step2.R
    ├── step3.py
    └── step4.R

```
### Run SAAS Script
#### Windows
```
python .\process.py -ann .\Mus_musculus.GRCm38.97.gtf -type gtf -exp .\exp_kidney\ -female .\kidney_female.tx t -male .\kidney_male.txt -AS .\as_kidney\ -info .\info_kidney.txt -out kidney_saas.csv
```
#### Centos
```
python process.py -ann Mus_musculus.GRCm38.97.gtf -type gtf -exp exp_kidney/ -female kidney_female.txt -male kidney_male.txt -AS as_kidney/ -info info_kidney.txt  -out kidney_saas.csv
```
#### Success
```
Loading anntation file...
File type:gtf 
Please waite
Step1 is done
[1] "process first exp"
[1] "merge files"
[1] "exp_kidney/SRR945383.csv"
[1] "exp_kidney/SRR945384.csv"
[1] "exp_kidney/SRR945385.csv"
[1] "exp_kidney/SRR945386.csv"
[1] "exp_kidney/SRR945387.csv"
[1] "exp_kidney/SRR945388.csv"
[1] "exp_kidney/SRR945389.csv"
[1] "exp_kidney/SRR945390.csv"
[1] "exp_kidney/SRR945391.csv"
[1] "exp_kidney/SRR945392.csv"
[1] "exp_kidney/SRR945393.csv"
[1] "Step2 is done"
Loading alternative splicing site files as_kidney/
Step3 is done
[1] "Step4 is done"
```
### All Arguments
```
usage: process.py [-h] [-ann ANN] [-type TYPE] [-exp EXP] [-female FEMALE]
                  [-male MALE] [-AS AS] [-info INFO] [-out OUT]

optional arguments:
  -h, --help      show this help message and exit
  -ann ANN        gtf or gff file from ensembl or NCBI
  -type TYPE      'gtf' or 'gff'
  -exp EXP        exp file dir
  -female FEMALE  female sample
  -male MALE      male sample
  -AS AS          AS file from rMATS
  -info INFO      remarks of sample
  -out OUT        out of process
```
## Output
What we need is **kidney_saas.csv**
```
out/
├── as
│   ├── A3SS.MATS.txt
│   ├── A5SS.MATS.txt
│   ├── MXE.MATS.txt
│   ├── RI.MATS.txt
│   └── SE.MATS.txt
├── as.txt
├── exp
│   ├── merge.csv
│   ├── symbol_id_exp.csv
│   └── symbol.txt
├── final_exp.csv
├── kidney_saas.csv
└── out
```

