###########################
## merge all exp samples ##
###########################


args <- commandArgs(T)
filenames <- list.files(args[1])
path1 <- paste(args[1],filenames[1],seq="")
path1 <- gsub(" ","",path1)
n <- length(filenames)
a <- read.csv(path1)
# loop
for (i in 2:n){
	path <- paste(args[1],filenames[i],sep="")
	path <- gsub(" ","",path)
	print(path)
	b = read.csv(path,header = T)
	a = merge(a,b,by="X",all=FALSE)
}
write.csv(a,"out/exp/merge.csv",row.names=F)

####################################
## match id and symbol in all exp ##
####################################

symbol_file = read.table('out/exp/symbol.txt',header=T)
exp_file = read.csv('out/exp/merge.csv',header=T)
exp_file_colnames <- colnames(exp_file)
exp_file_colnames[1] <- "id"
colnames(exp_file) <- exp_file_colnames
outfile <- merge(symbol_file,exp_file,by="id",all=FALSE)
write.csv(outfile,'out/exp/symbol_id_exp.csv',row.names=FALSE)

####################################
## calculate mean Female/Male exp ##
####################################
female_sample <- gsub(" ","",args[2])
male_sample <- gsub(" ","",args[3])
female_name1 <- gsub('_female.txt','',female_sample)
male_name1 <- gsub('_male.txt','',male_sample)
#print(female_name1)
female_name <- paste(female_name1,'_mean_female',sep='')
male_name <- paste(male_name1,'_mean_male',sep='')
female_sample_file <- read.table(female_sample)
male_sample_file <- read.table(male_sample)
sample_number <- length(female_sample_file[,1])
females <- as.character(female_sample_file[,1])
males <- as.character(male_sample_file[,1])
#print(females)
exp_female <- outfile[females[1]]
#head(exp_female)
exp_male <- outfile[males[1]]
#head(exp_male)

if (length(females) == 1){
	exp_female = exp_female
}
if (length(females) != 1){

	for (i in 2:length(females)){
		exp_female <- exp_female + outfile[females[i]]
		#exp_male <- exp_male + outfile[males[i]]
	}
}

if (length(males) == 1){
	exp_male = exp_male
}
if (length(males) != 1){
	for (i in 2:length(males)){
		#exp_female <- exp_female + outfile[females[i]]
		exp_male <- exp_male + outfile[males[i]]
	}
}
outfile$mean_female <- exp_female[,1]/sample_number
outfile$mean_male <- exp_male[,1]/sample_number
names(outfile)[names(outfile)=="mean_female"]= female_name
names(outfile)[names(outfile)=="mean_male"]= male_name
write.csv(outfile,'out/final_exp.csv',row.names=FALSE)

print("Step2 is done")
