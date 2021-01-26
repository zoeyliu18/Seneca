### UniMorph Format ###
### lemma, target form, tag ###

'''
Number

Singular: Sg
Plural: Pl
Dual: Du

Gender

Female: F
Male: M
Neutral: Nt / MF (Ask Emily)

Person
1
2
3
Exclusive: e-x; Ex

Tense
present
past
future

'''

import io, os, argparse, random


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type = str, help = '.txt file of Seneca morphology')
	parser.add_argument('--output', type = str, help = 'path to UniMorph formatted data for segmentation analysis')

	args = parser.parse_args()

	gold_features = {'Sg': 'SG',
					'Pl': 'PL',
					'Du': 'DU',
					'F': 'FEM',
					'M': 'MASC',
					'Nt': 'NEUT',
					'MF': 'NEUT',
					'1': '1',
					'2': '2',
					'3': '3',
					'e-x': 'EXCL',
					'Ex': 'EXCL',
					'present': 'PRS',
					'past': 'PST',
					'future': 'FUT'}

	all_stem = []
	all_meaning = []
	all_seg = []
	all_form = []

	with io.open(args.input, encoding = 'utf-8') as f:
		for line in f:
			toks = line.split()
			meaning = toks[0]
			stem = list(toks[1])
			seg = list(toks[-2].replace('-', '!'))
			target = toks[-1]

			all_stem.append(stem)
			all_meaning.append(meaning)
			all_seg.append(seg)
			all_form.append(target)

	### generating train/dev/test split

	heldout_size = 0.6

	index = []
	i = 0
	while i < len(all_seg):
		index.append(i)
		i += 1

	random.shuffle(index)

	total = len(all_seg)
	num_train = total - int(heldout_size * total)
	num_dev = int(num_train / 2)

	train_src = io.open(args.output + 'train_src', 'w', encoding = 'utf-8')
	train_trg = io.open(args.output + 'train_trg', 'w', encoding = 'utf-8')

	dev_src = io.open(args.output + 'dev_src', 'w', encoding = 'utf-8')
	dev_trg = io.open(args.output + 'dev_trg', 'w', encoding = 'utf-8')

	test_src = io.open(args.output + 'test_src', 'w', encoding = 'utf-8')
	test_trg = io.open(args.output + 'test_trg', 'w', encoding = 'utf-8')
	everything = []
	for i in index[ : num_train]:
		form = all_form[i]
		train_src.write(' '.join(c for c in form) + '\n')
		seg = all_seg[i]
		train_trg.write(' '.join(m for m in seg) + '\n')
		for c in form:
			everything.append(c)
		for m in seg:
			everything.append(m)

	heldout_index = index[num_train : ]

	for i in heldout_index[ : num_dev]:
		form = all_form[i]
		dev_src.write(' '.join(c for c in form) + '\n')
		seg = all_seg[i]
		dev_trg.write(' '.join(m for m in seg) + '\n')
		for c in form:
			everything.append(c)
		for m in seg:
			everything.append(m)

	for i in heldout_index[num_dev : ]:
		form = all_form[i]
		test_src.write(' '.join(c for c in form) + '\n')
		seg = all_seg[i]
		test_trg.write(' '.join(m for m in seg) + '\n')
		for c in form:
			everything.append(c)
		for m in seg:
			everything.append(m)

	print(num_train)
	print(num_dev)
	print(len(heldout_index[num_dev : ]))

	print(len(set(everything)))


