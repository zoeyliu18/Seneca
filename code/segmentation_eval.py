
import io, os, argparse, random
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
			morphs = tok.split('|')
			gold_morphs.append(morphs)
			gold_total += len(morphs)

	with io.open(args.pred, encoding = 'utf-8') as f:
		for line in f:
			tok = line.strip()
			pred.append(tok)
			morphs = tok.split('|')
			pred_morphs.append(morphs)
			pred_total += len(morphs)

	labeled = 0  ### full form accuracy
	unlabeled = 0 ### segmentation accuracy, regardless of the form of each morpheme

	correct_total = 0
	ave_dist = 0

	for i in range(len(gold)):
		if gold[i].count('!') == pred[i].count('!'):
			unlabeled += 1
		if gold[i] == pred[i]:
			labeled += 1

		for m in pred_morphs[i]:
			if m in gold_morphs[i]:
				correct_total += 1

		ave_dist += levenshtein(gold[i], pred[i])

	precision = correct_total / pred_total
	recall = correct_total / gold_total
	F1 = 2 * (precision * recall) / (precision + recall)
	ave_dist = round(ave_dist / len(gold), 2)

	print('Labeled: ' + str(round(labeled * 100 / len(gold), 2)))
	print('Unlabeled: ' + str(round(unlabeled * 100 / len(gold), 2)))
	print('F1: ' + str(round(F1 * 100, 2)))
	print('Average distance: ' + str(ave_dist))
