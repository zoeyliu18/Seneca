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

import io, os, argparse


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type = str, help = '.txt file of Seneca morphology')
	parser.add_argument('--output', type = str, help = 'UniMorph formatted data for inflection analysis')

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

	all_meaning = []

	output = io.open(args.output, 'w', encoding = 'utf-8')

	with io.open(args.input, encoding = 'utf-8') as f:
		for line in f:
			toks = line.split()
			meaning = toks[0]
			lemma = toks[1]
			target = toks[-1]

			temp_features = []
			annotated_features = []

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

			all_meaning.append(meaning)

			person = ['1', '2', '3']

			for f in temp_features:
				if f[-1] in person:
					annotated_features.append(gold_features[f[ : -1]])
					annotated_features.append(gold_features[f[-1]])
				else:
					annotated_features.append(gold_features[f])

			annotated_features.sort()

			output.write(lemma + '\t' + target + '\t' + ';'.join(f for f in annotated_features) + '\n')

	print(len(set(all_meaning)))
