
import io, os, argparse, random, statistics
from collections import Counter

def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    helper.__name__= func.__name__

    return helper

def memoize(func):
    mem = {}
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in mem:
            mem[key] = func(*args, **kwargs)
        return mem[key]
    return memoizer

@call_counter
@memoize    
def levenshtein(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1
    
    res = min([levenshtein(s[:-1], t)+1,
               levenshtein(s, t[:-1])+1, 
               levenshtein(s[:-1], t[:-1]) + cost])

    return res


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--gold', type = str, help = 'gold-standard segmentation')
	parser.add_argument('--pred', type = str, help = 'predicted segmentation')

	args = parser.parse_args()

	gold = []
	pred = []

	gold_morphs = []
	pred_morphs = []

	gold_total = 0
	pred_total = 0

	with io.open(args.gold, encoding = 'utf-8') as f:
		for line in f:
			tok = line.strip()
			gold.append(tok)
			morphs = tok.split('!')
			gold_morphs.append(morphs)
			gold_total += len(morphs)

	with io.open(args.pred, encoding = 'utf-8') as f:
		for line in f:
			tok = line.strip()
			pred.append(tok)
			morphs = tok.split('!')
			pred_morphs.append(morphs)
			pred_total += len(morphs)

	all_labeled = []  ### full form accuracy
	all_unlabeled = [] ### segmentation accuracy, regardless of the form of each morpheme

	all_correct_total = []
	all_ave_dist = []

	all_F1 = []

	### start bootstrap ###

	n = len(gold)

	### making index list ###

	form_index = []
	i = 0
	while i < n:
		form_index.append(i)
		i += 1

	morph_index = []
	i = 0
	while i < len(gold_morphs):
		morph_index.append(i)
		i += 1

	for time in range(10000):

		select_form = random.choices(form_index, k = n)
		select_morph = random.choices(morph_index, k = len(morph_index))
		
		### four metrics ###

		labeled = 0
		unlabeled = 0
		correct_total = 0
		ave_dist = 0

		### constructiong sample ###

		gold_sample = []
		pred_sample = []

		gold_morphs_sample = []
		pred_morphs_sample = []

		for idx in select_form:
			gold_sample.append(gold[idx])
			pred_sample.append(pred[idx])

		for idx in select_morph:
			gold_morphs_sample.append(gold_morphs[idx])
			pred_morphs_sample.append(pred_morphs[idx])

		for i in range(n):
			if gold_sample[i].count('!') == pred_sample[i].count('!'):
				unlabeled += 1
			if gold_sample[i] == pred_sample[i]:
				labeled += 1

			for m in pred_morphs_sample[i]:
				if m in gold_morphs_sample[i]:
					correct_total += 1

			ave_dist += levenshtein(gold_sample[i], pred_sample[i])

		labeled = round(labeled * 100 / n, 2)
		unlabeled = round(unlabeled * 100 / n, 2)
		ave_dist = round(ave_dist / n, 2)

		precision = correct_total / pred_total
		recall = correct_total / gold_total
		F1 = 2 * (precision * recall) / (precision + recall)
		F1 = round(F1 * 100, 2)
		
		all_labeled.append(labeled)
		all_unlabeled.append(unlabeled)

		all_correct_total.append(correct_total)
		all_ave_dist.append(ave_dist)

		all_F1.append(F1)

	all_labeled.sort()
	all_unlabeled.sort()
	all_ave_dist.sort()
	all_F1.sort()


	print('Labeled: ' + str(round(statistics.mean(all_labeled), 2)) + ' ' + str(all_labeled[250]) + ' ' + str(all_labeled[9750]))
	print('Unlabeled: ' + str(round(statistics.mean(all_unlabeled), 2)) + ' ' + str(all_unlabeled[250]) + ' ' + str(all_unlabeled[9750]))
	print('F1: ' + str(round(statistics.mean(all_F1), 2)) + ' ' + str(all_F1[250]) + ' ' + str(all_F1[9750]))
	print('Average distance: ' + str(round(statistics.mean(all_ave_dist), 2)) + ' ' + str(all_ave_dist[250]) + ' ' + str(all_ave_dist[9750]))


