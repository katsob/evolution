library(ggplot2)

args = commandArgs(trailingOnly=TRUE)
model <- args[1]
data <- read.csv(sprintf('%s/learn_curve.csv', model))
p <- ggplot(data) + geom_line(aes(x=generation, y=cans))
ggsave(sprintf('%s/learn_curve.png', model), p, width = 15, height = 5)
