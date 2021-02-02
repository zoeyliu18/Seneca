library(ggplot2)
library('RColorBrewer')
library(gridExtra)
library(tidyverse)

results <- read.csv('results.csv', header = T, sep = '\t')

low_resource %>% 
  ggplot(aes(x = Data, y = Mean, group = Metric, color = Metric)) +
  geom_point(aes(color = Metric, shape = Metric)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 3, 6)) +
  scale_color_manual(values = c("forestgreen", "steelblue", "peru")) + 
  geom_line(aes(color = Metric, linetype = Metric)) + 
  scale_x_continuous(breaks=seq(1, 10, 1)) +
  ylim(-1, 100) +
  theme_classic() + 
#  facet_grid(~Metric) +
  theme(text = element_text(size=20, family="Times")) + 
  theme(legend.position="top") +
  xlab("Split") + 
  ylab("Mean")