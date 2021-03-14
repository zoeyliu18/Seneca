library(ggplot2)
library('RColorBrewer')
library(gridExtra)
library(tidyverse)
library(wesanderson)
library(ggpubr)


######### Evaluation results ############

data <- read.csv('evaluation.csv', header = T, sep = ',')

data$Model[data$Model == 'tuning parameters'] <- 'tuning'
data$Model[data$Model == 'multi-task learning'] <- 'multi-task'

data$Setting <- factor(data$Setting,levels=c('in-domain', 'cross-domain', 'crosslinguistic'))
data$Model <- factor(data$Model,levels=c('baseline', 'tuning', 'self-training', 'multi-task', 'transfer', 'fine-tuning'))

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
        axis.text.x = element_text(angle = 20),
        legend.title=element_text(size=12)) +  
  theme(legend.position="top") +
  xlab("") + 
  ylab("")

ggsave('set_acc.pdf', height = 2.5, width = 7.5)

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
        axis.text.x = element_text(angle = 20),
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
        axis.text.x = element_text(angle = 20),
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



############# Testing results ###############

data <- read.csv('test.csv', header = T, sep = ',')
data$Metric <- factor(data$Metric,levels=c('Accuracy', 'F1', 'Avg. Distance'))
data$Design <- factor(data$Design,levels=c('development set', 'development domain'))

acc <- subset(data, Metric %in% c('Accuracy'))
f1 <- subset(data, Metric %in% c('F1'))
dist <- subset(data, Metric %in% c('Avg. Distance'))

set <- subset(data, Design %in% c('development set'))
domain <- subset(data, Design %in% c('development domain'))


acc %>% 
  ggplot(aes(x = Split, y = Mean, group = Model, color = Model)) +
  geom_point(aes(color = Model, shape = Model)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 16)) +
  scale_color_manual(values = c("forestgreen", "steelblue")) + 
  #  geom_line(aes(color = Metric, linetype = Metric)) + 
  ylim(50, 100) +
  theme_classic() + 
  facet_wrap(~Design, scales="free") +
  theme(text = element_text(size=12, family="Times"),
        axis.text.x = element_text(angle = 0),
        legend.title=element_text(size=12)) +  
  theme(legend.position="top") +
  xlab("") + 
  ylab("")

ggsave('test_acc.pdf', height = 3, width = 6)

f1 %>% 
  ggplot(aes(x = Split, y = Mean, group = Model, color = Model)) +
  geom_point(aes(color = Model, shape = Model)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 16)) +
  scale_color_manual(values = c("forestgreen", "steelblue")) + 
  #  geom_line(aes(color = Metric, linetype = Metric)) + 
  ylim(50, 100) +
  theme_classic() + 
  facet_wrap(~Design, scales="free") +
  theme(text = element_text(size=12, family="Times"),
        axis.text.x = element_text(angle = 0),
        legend.title=element_text(size=12)) +  
  theme(legend.position="top") +
  xlab("") + 
  ylab("")

ggsave('test_f1.pdf', height = 3, width = 6)

dist %>% 
  ggplot(aes(x = Split, y = Mean, group = Model, color = Model)) +
  geom_point(aes(color = Model, shape = Model)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 16)) +
  scale_color_manual(values = c("forestgreen", "steelblue")) + 
  #  geom_line(aes(color = Metric, linetype = Metric)) + 
  ylim(0, 1) +
  theme_classic() + 
  facet_wrap(~Design, scales="free") +
  theme(text = element_text(size=12, family="Times"),
        axis.text.x = element_text(angle = 0),
        legend.title=element_text(size=12)) +  
  theme(legend.position="top") +
  xlab("") + 
  ylab("")

ggsave('test_dist.pdf', height = 3, width = 6)


set %>% 
  ggplot(aes(x = Split, y = Mean, group = Model, color = Model)) +
  geom_point(aes(color = Model, shape = Model)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 16)) +
  scale_color_manual(values = c("forestgreen", "steelblue")) + 
  #  geom_line(aes(color = Metric, linetype = Metric)) + 
#  ylim(50, 100) +
  theme_classic() + 
  facet_grid(~Metric) +
#  facet_grid(~Metric, scale="free", space="free_x") +
  theme(text = element_text(size=12, family="Times"),
        axis.text.x = element_text(angle = 0),
        legend.title=element_text(size=12)) +  
  theme(legend.position="top") +
  xlab("") + 
  ylab("")

ggsave('test_set.pdf', height = 3, width = 8)

domain %>% 
  ggplot(aes(x = Split, y = Mean, group = Model, color = Model)) +
  geom_point(aes(color = Model, shape = Model)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 16)) +
  scale_color_manual(values = c("forestgreen", "steelblue")) + 
  #  geom_line(aes(color = Metric, linetype = Metric)) + 
  #  ylim(50, 100) +
  theme_classic() + 
  facet_wrap(~Metric) +#, scales="free") +#, space="free_x") +
  theme(text = element_text(size=12, family="Times"),
        axis.text.x = element_text(angle = 0),
        legend.title=element_text(size=12)) +  
  theme(legend.position="top") +
  xlab("") + 
  ylab("")



########################################

set_acc <- ggplot(subset(set, Metric == 'Accuracy'), aes(x = Split, y = Mean, group = Model, color = Model)) +
  geom_point(aes(color = Model, shape = Model)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 16)) +
  scale_color_manual(values = c("forestgreen", "steelblue")) + 
  #  geom_line(aes(color = Metric, linetype = Metric)) + 
  ylim(50, 100) +
  theme_classic() + 
  facet_wrap(~Metric) +#, scales="free") +#, space="free_x") +
  theme(text = element_text(size=12, family="Times"),
        axis.text.x = element_text(angle = 0),
        legend.title=element_text(size=12)) +  
  theme(legend.position="top") +
  xlab("") + 
  ylab("") 

set_f1 <- ggplot(subset(set, Metric == 'F1'), aes(x = Split, y = Mean, group = Model, color = Model)) +
  geom_point(aes(color = Model, shape = Model)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 16)) +
  scale_color_manual(values = c("forestgreen", "steelblue")) + 
  #  geom_line(aes(color = Metric, linetype = Metric)) + 
  ylim(50, 100) +
  theme_classic() + 
  facet_wrap(~Metric) +#, scales="free") +#, space="free_x") +
  theme(text = element_text(size=12, family="Times"),
        axis.text.x = element_text(angle = 0),
        legend.title=element_text(size=12)) +  
  theme(legend.position="top") +
  xlab("") + 
  ylab("") 

set_dist <- ggplot(subset(set, Metric == 'Avg. Distance'), aes(x = Split, y = Mean, group = Model, color = Model)) +
  geom_point(aes(color = Model, shape = Model)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 16)) +
  scale_color_manual(values = c("forestgreen", "steelblue")) + 
  #  geom_line(aes(color = Metric, linetype = Metric)) + 
  ylim(0, 1) +
  theme_classic() + 
  facet_wrap(~Metric) +#, scales="free") +#, space="free_x") +
  theme(text = element_text(size=12, family="Times"),
        axis.text.x = element_text(angle = 0),
        legend.title=element_text(size=12)) +  
  theme(legend.position="top") +
  xlab("") + 
  ylab("") 

ggarrange(set_acc, set_f1, set_dist, nrow = 1, ncol = 3, common.legend = TRUE, legend = 'top')

ggsave('test_set.pdf', height = 3, width = 8)

domain_acc <- ggplot(subset(domain, Metric == 'Accuracy'), aes(x = Split, y = Mean, group = Model, color = Model)) +
  geom_point(aes(color = Model, shape = Model)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 16)) +
  scale_color_manual(values = c("forestgreen", "steelblue")) + 
  #  geom_line(aes(color = Metric, linetype = Metric)) + 
  ylim(50, 100) +
  theme_classic() + 
  facet_wrap(~Metric) +#, scales="free") +#, space="free_x") +
  theme(text = element_text(size=12, family="Times"),
        axis.text.x = element_text(angle = 0),
        legend.title=element_text(size=12)) +  
  theme(legend.position="top") +
  xlab("") + 
  ylab("") 

domain_f1 <- ggplot(subset(domain, Metric == 'F1'), aes(x = Split, y = Mean, group = Model, color = Model)) +
  geom_point(aes(color = Model, shape = Model)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 16)) +
  scale_color_manual(values = c("forestgreen", "steelblue")) + 
  #  geom_line(aes(color = Metric, linetype = Metric)) + 
  ylim(50, 100) +
  theme_classic() + 
  facet_wrap(~Metric) +#, scales="free") +#, space="free_x") +
  theme(text = element_text(size=12, family="Times"),
        axis.text.x = element_text(angle = 0),
        legend.title=element_text(size=12)) +  
  theme(legend.position="top") +
  xlab("") + 
  ylab("") 

domain_dist <- ggplot(subset(domain, Metric == 'Avg. Distance'), aes(x = Split, y = Mean, group = Model, color = Model)) +
  geom_point(aes(color = Model, shape = Model)) +
  geom_errorbar(aes(ymin = CI25, ymax = CI975), width = .2) +
  scale_shape_manual(values = c(16, 16)) +
  scale_color_manual(values = c("forestgreen", "steelblue")) + 
  #  geom_line(aes(color = Metric, linetype = Metric)) + 
  ylim(0, 1) +
  theme_classic() + 
  facet_wrap(~Metric) +#, scales="free") +#, space="free_x") +
  theme(text = element_text(size=12, family="Times"),
        axis.text.x = element_text(angle = 0),
        legend.title=element_text(size=12)) +  
  theme(legend.position="top") +
  xlab("") + 
  ylab("") 

ggarrange(domain_acc, domain_f1, domain_dist, nrow = 1, ncol = 3, common.legend = TRUE, legend = 'top')
  
ggsave('test_domain.pdf', height = 3, width = 8)
