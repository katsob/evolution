library(ggplot2)

fs <- list.files('.', recursive = TRUE)
fs <- fs[grepl('curve.csv', fs)]

data <- lapply(fs, function(f) read.csv(f))
names(data) <- sapply(fs, function(s) substr(s,20,39))
data <- dplyr::bind_rows(data, .id='params')

ggplot(data) + 
    geom_line(aes(x=generation, y=cans, color=params, group=params)) +
    theme(legend.position = c(.75,.25), 
          legend.background = element_rect(fill=alpha('white',0.4))) 

ggsave('learning_curves.png', dpi=100, width=10, height = 6)

