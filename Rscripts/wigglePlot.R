library(ggplot2)

a<-read.table("channel_110_read_9_template.events.txt", sep="\t", header=TRUE)
b<-cbind(a, "category"=as.integer((a$start - 4414) / 25))
ggplot(b, aes(x=start, y=mean)) + geom_step() + facet_wrap(~category, ncol=1, scales="free_x") + scale_x_continuous('total time 273 seconds') + scale_y_continuous('mean signal (picoamps)') + opts(strip.background = theme_blank(), strip.text.x = theme_blank(), axis.text.x = theme_blank())
ggsave("wiggle_plot_v2.pdf", width=11, height=8)
