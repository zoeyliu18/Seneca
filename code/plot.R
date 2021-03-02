library(ggplot2)
library('RColorBrewer')
library(gridExtra)
library(tidyverse)
library(wesanderson)

results <- read.csv('results.csv', header = T, sep = ',')

results %>% 
  ggplot(aes(x = Data, y = Mean, group = Metric, color = Metric)) +
  geom_point(aes(color = Metric, shape = Metric)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 3, 6)) +
  scale_color_manual(values = c("forestgreen", "steelblue", "mediumpurple4")) + 
  geom_line(aes(color = Metric, linetype = Metric)) + 
  scale_x_continuous(breaks=seq(1, 10, 1)) +
  ylim(-1, 100) +
  theme_classic() + 
  facet_grid(~Language) +
  theme(text = element_text(size=15, family="Times")) + 
  theme(legend.position="top") +
  xlab("Split") + 
  ylab("Mean")

ggsave('low_resource.pdf', height = 4, width = 8)

######### Evaluation results ############

data <- read.csv('evaluation.csv', header = T, sep = ',')
data$Setting <- factor(data$Setting,levels=c('in-domain', 'domain transfer', 'crosslinguistic transfer'))
data$Model[data$Model == 'tuning parameters'] <- 'tuning'
data$Model[data$Model == 'multi-task learning'] <- 'multi-task'

set <- subset(data, Design %in% c('set'))
domain <- subset(data, Design %in% c('domain'))

set_acc <- subset(set, Metric %in% c('Accuracy'))
set_f1 <- subset(set, Metric %in% c('F1'))
set_dist <- subset(set, Metric %in% c('Avg. Distance'))

set_acc %>% 
  ggplot(aes(x = Model, y = Mean, group = Evaluation, color = Evaluation)) +
  geom_point(aes(color = Evaluation, shape = Evaluation)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 3, 6)) +
  scale_color_manual(values = c("forestgreen", "steelblue")) + 
#  geom_line(aes(color = Metric, linetype = Metric)) + 
  ylim(0, 100) +
  theme_classic() + 
  facet_grid(~Setting, scale="free", space="free_x") +
  theme(text = element_text(size=15, family="Times"),
        axis.text.x = element_text(angle = 0),
        legend.title=element_text(size=12)) +  
  theme(legend.position="top") +
  xlab("") + 
  ylab("")

ggsave('set_acc.pdf', height = 2.8, width = 7.8)

set_f1 %>% 
  ggplot(aes(x = Model, y = Mean, group = Evaluation, color = Evaluation)) +
  geom_point(aes(color = Evaluation, shape = Evaluation)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 3, 6)) +
  scale_color_manual(values = c("mediumpurple4", "peru")) + 
  ylim(0, 100) +
  theme_classic() + 
  facet_grid(~Setting, scale="free", space="free_x") +
  theme(text = element_text(size=15, family="Times"),
        axis.text.x = element_text(angle = 0),
        legend.title=element_text(size=12)) +  
  theme(legend.position="top") +
  xlab("") + 
  ylab("")

ggsave('set_f1.pdf', height = 2.8, width = 7.8)

set_dist %>% 
  ggplot(aes(x = Model, y = Mean, group = Evaluation, color = Evaluation)) +
  geom_point(aes(color = Evaluation, shape = Evaluation)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 3, 6)) +
  scale_color_brewer(palette="Dark2") +
  ylim(0, 6) +
  theme_classic() + 
  facet_grid(~Setting, scale="free", space="free_x") +
  theme(text = element_text(size=15, family="Times"),
        axis.text.x = element_text(angle = 0),
        legend.title=element_text(size=12)) +  
  theme(legend.position="top") +
  xlab("") + 
  ylab("")

ggsave('set_dist.pdf', height = 2.8, width = 7.8)

domain_acc <- subset(domain, Metric %in% c('Accuracy'))
domain_f1 <- subset(domain, Metric %in% c('F1'))
domain_dist <- subset(domain, Metric %in% c('Avg. Distance'))

domain_acc %>% 
  ggplot(aes(x = Model, y = Mean, group = Evaluation, color = Evaluation)) +
  geom_point(aes(color = Evaluation, shape = Evaluation)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 3, 6)) +
  scale_color_manual(values = c("forestgreen", "steelblue")) + 
  #  geom_line(aes(color = Metric, linetype = Metric)) + 
  ylim(0, 100) +
  theme_classic() + 
  facet_grid(~Setting, scale="free", space="free_x") +
  theme(text = element_text(size=15, family="Times"),
        axis.text.x = element_text(angle = 0),
        legend.title=element_text(size=12)) +  
  theme(legend.position="top") +
  xlab("") + 
  ylab("")

ggsave('domain_acc.pdf', height = 2.8, width = 7.8)

domain_f1 %>% 
  ggplot(aes(x = Model, y = Mean, group = Evaluation, color = Evaluation)) +
  geom_point(aes(color = Evaluation, shape = Evaluation)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 3, 6)) +
  scale_color_manual(values = c("mediumpurple4", "peru")) + 
  ylim(0, 100) +
  theme_classic() + 
  facet_grid(~Setting, scale="free", space="free_x") +
  theme(text = element_text(size=15, family="Times"),
        axis.text.x = element_text(angle = 0),
        legend.title=element_text(size=12)) +  
  theme(legend.position="top") +
  xlab("") + 
  ylab("")

ggsave('domain_f1.pdf', height = 2.8, width = 7.8)

domain_dist %>% 
  ggplot(aes(x = Model, y = Mean, group = Evaluation, color = Evaluation)) +
  geom_point(aes(color = Evaluation, shape = Evaluation)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 3, 6)) +
  scale_color_brewer(palette="Dark2") +
  ylim(0, 6) +
  theme_classic() + 
  facet_grid(~Setting, scale="free", space="free_x") +
  theme(text = element_text(size=15, family="Times"),
        axis.text.x = element_text(angle = 0),
        legend.title=element_text(size=12)) + 
  theme(legend.position="top") +
  xlab("") + 
  ylab("")

ggsave('domain_dist.pdf', height = 2.8, width = 7.8)

