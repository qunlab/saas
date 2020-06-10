############################
## match as with diff exp ##
############################
args <- commandArgs(T)
as_file <- read.table("out/as.txt",header=FALSE)
exp_file <- read.csv("out/final_exp.csv",header=T)
colnames(as_file) <- c("id","strand","symbol","chr","as_site1","as_site2","as_site3","as_site4","as_pvalue","inlevle1","inlevel2","as_type")
#head(as_file)
c = merge(as_file,exp_file,by="id",all=FALSE)
path1 = args[1]
path1 = gsub(" ","",path1)
info_file = read.table(path1,header=T)
num = length(c$id)
c$Remark = rep(info_file[1,2],num)
c$Organism = rep(info_file[2,2],num)
c$Tissue = rep(info_file[3,2],num)
c$GEO_accession = rep(info_file[4,2],num)
path2 = paste("out/",args[2],sep="")
path2 = gsub(" ","",path2)
write.csv(c,path2)
#head(c)
print("Step4 is done")