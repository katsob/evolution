library(ggplot2)

fs <- list.files('.', recursive = TRUE)
fs <- fs[grepl('curve.csv', fs)]

data <- lapply(fs, function(f) read.csv(f))
names(data) <- sapply(fs, function(s) substr(s,20,39))
data <- dplyr::bind_rows(data, .id='params')

ggplot(data) + 
    geom_line(aes(x=generation, y=cans, color=params, group=params)) +
    theme(legend.position = c(.85,.25), 
          legend.background = element_rect(fill=alpha('white',0.4))) +
    scale_y_continuous(breaks = pretty(data$cans, n = 12)) +
    scale_x_continuous(breaks = pretty(data$generation, n = 20))

ggsave('learning_curves.png', dpi=100, width=10, height = 5)

