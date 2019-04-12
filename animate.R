#!/usr/bin/env Rscript

# # install.packages('devtools')
# devtools::install_github('thomasp85/gganimate')
library(ggplot2)
library(gganimate)
library(reshape2)
library(dplyr)

args = commandArgs(trailingOnly=TRUE)
evolution_dir <- args[1]
epoch_nr <- args[2]

anim_dir <- sprintf('%s/animations', evolution_dir)
anim_out_path <- sprintf('%s/epoch%s.gif', anim_dir, epoch_nr)

if(!file.exists(anim_out_path)){
    board <- read.csv(file.path(evolution_dir, sprintf('epoch%s_board.csv', epoch_nr)), header = TRUE)
    path <- read.csv(file.path(evolution_dir, sprintf('epoch%s_path.csv', epoch_nr)), header = FALSE)
    if(!dir.exists(anim_dir))
        dir.create(anim_dir)
    
    board$can <- factor(board$can)
    path <- cbind(path, step=seq(0, nrow(path)-1))
    colnames(path) <- c('x','y', 'step')
    class(path$step)
    ggplot() + 
        geom_tile(data=board, aes(x = x, y = y, fill = can)) +
        scale_fill_manual(values = c('#f4cc70', '#de7a22')) +
        geom_point(data=path, aes(x = x, y = y), color='#20948b', size=12, shape=18) +
        labs(x='', y='', title='Step: {frame_time}') +
        theme(legend.position = 'none', 
              axis.ticks=element_blank(), 
              axis.text.x = element_blank(),
              axis.text.y = element_blank(),
              plot.title = element_text(face = "bold", size=20))  +
        transition_time(step) +
        ease_aes('linear', interval=.001) -> anim
    anim
    
    anim_save(anim_out_path, anim)
}    
