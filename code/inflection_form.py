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
	parser.add_argument('--output', type = str, help = 'path to UniMorph formatted data for inflection analysis')

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
	all_data = []

	with io.open(args.input, encoding = 'utf-8') as f:
		for line in f:
			toks = line.split()
			meaning = toks[0]
			stem = toks[1]
			target = toks[-1]

			temp_features = []
			annotated_features = []

			all_stem.append(stem)
			all_meaning.append(meaning)

			for f in toks[2 : -2]:
				if f[-3 : ] == 'e-x':
					temp_features.append('e-x')
					if '-' in f[ : -3]:
						for w in f[ : -3].split('-'):
							temp_features.append('w')
				else:
					if '-' in f:
						for w in f.split('-'):
							temp_features.append(w)
					else:
						temp_features.append(f)

			person = ['1', '2', '3']

			for f in temp_features:
				if f[-1] in person:
					annotated_features.append(gold_features[f[ : -1]])
					annotated_features.append(gold_features[f[-1]])
				else:
					annotated_features.append(gold_features[f])

			annotated_features.sort()

			all_data.append([stem, target, 'V;' + ';'.join(f for f in annotated_features)])

	### generating train/dev/test split

	heldout_size = 0.2

	unique_stem = list(set(all_stem))
	random.shuffle(unique_stem)

	num_stem = len(unique_stem)
	num_train = num_stem - int(heldout_size * num_stem)
	num_dev = int((num_stem - num_train) / 2)

	train_stem = unique_stem[ : num_train]
	heldout_stem = unique_stem[num_train : ]
	dev_stem = heldout_stem[ : num_dev]
	test_stem = heldout_stem[num_dev : ]

	train_data = io.open(args.output + 'train', 'w', encoding = 'utf-8')
	dev_data = io.open(args.output + 'dev', 'w', encoding = 'utf-8')
	test_data = io.open(args.output + 'test', 'w', encoding = 'utf-8')

	exclude = ["yö", "a:di'", "i'"]

	for tok in all_data:
		if tok[0] in train_stem and tok[0] not in exclude:
			train_data.write('\t'.join(w for w in tok) + '\n')
		if tok[0] in dev_stem and tok[0] not in exclude:
			dev_data.write('\t'.join(w for w in tok) + '\n')
		if tok[0] in test_stem and tok[0] not in exclude:
			test_data.write('\t'.join(w for w in tok) + '\n')

	print(num_train)
	print(num_dev)
	print(len(test_stem))



