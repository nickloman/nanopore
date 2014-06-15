runstats<-read.table("salm.run.stats.txt", header=T)
runstats_small=subset(runstats, Template < 10000 & Complement < 10000)
# Thanks Jason for the tip!
smoothScatter(runstats_small$Template, runstats_small$Complement, xlab="Number of Template Events", ylab="Number of Complement Events")
