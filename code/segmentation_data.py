import io, os, argparse, random, statistics


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type = str, help = '.txt file of Seneca morphology')
	parser.add_argument('--output', type = str, help = 'path to generated segmentation data')
	parser.add_argument('--lang', type = str, help = 'languages')
	parser.add_argument('--k', type = str, help = 'sample size')

	args = parser.parse_args()

	lang = args.lang

	all_stem = []
	all_meaning = []
	all_form = []
	all_seg = []

	coarse_form = []
	coarse_seg = []
	grammar_form = []
	grammar_seg = []

	all_morphs = []
	num_morph = []


	if lang == 'seneca':

		with io.open(args.input, encoding = 'utf-8') as f:
			for line in f:
				toks = line.split()
				meaning = toks[0]
				stem = list(toks[1])
				seg = list(toks[-2].replace('-', '!'))
				target = toks[-1]

				all_stem.append(stem)
				all_meaning.append(meaning)
				coarse_seg.append(seg)
				coarse_form.append(target)


	if len(coarse_form) != 0:
		for i in range(len(coarse_form)):
			if coarse_form[i] not in all_form:
				all_form.append(coarse_form[i])
				all_seg.append(coarse_seg[i])

	for seg in all_seg:
		seg = ''.join(w for w in seg)
		morphs = seg.split('!')
		for m in morphs:
			all_morphs.append(m)
			num_morph.append(len(morphs))

	if lang == 'seneca_other':

		with io.open(args.input + 'all-annotations.txt', encoding = 'utf-8') as f:
			for line in f:
				toks = line.strip().split('\t')
				coarse_form.append(toks[0])
				seg = toks[1].replace(' ','!')
				coarse_seg.append(list(seg))


		with io.open(args.input + 'segmentation.txt', encoding = 'utf-8') as f:
			for line in f:
				toks = line.strip().split('\t')
				if len(toks) == 3:
					coarse_form.append(toks[1])
					seg = toks[-1].replace('-', '!')
					coarse_seg.append(list(seg))


		with io.open(args.input + 'seneca.morf.annotation', encoding = 'utf-8') as f:
			for line in f:
				toks = line.strip().split()
				coarse_form.append(toks[0])
				seg = ' '.join(m for m in toks[1: ])
				coarse_seg.append(list(seg.replace(' ', '!')))


		with io.open(args.input + 'all-forms-from-spreadsheet.txt', encoding = 'utf-8') as f:
			for line in f:
				toks = line.split()
				seg = list(toks[-2].replace('-', '!'))
				target = toks[-1]

				grammar_seg.append(seg)
				grammar_form.append(target)

	

	### filter out words that have already been documented in the grammar book ###

	if len(coarse_form) != 0:
		for i in range(len(coarse_form)):
			if coarse_form[i] not in all_form and coarse_form[i] not in grammar_form:
				all_form.append(coarse_form[i])
				all_seg.append(coarse_seg[i])

	for seg in all_seg:
		seg = ''.join(w for w in seg)
		morphs = seg.split('!')
		for m in morphs:
			all_morphs.append(m)
			num_morph.append(len(morphs))

	print(len(set(all_morphs)))
	print(len(all_morphs))

	ave_morph = []

	for i in range(10000):
		sample = random.choices(num_morph, k = len(num_morph))

		ave = round(sum(sample) / len(num_morph), 2)
		ave_morph.append(ave)

	ave_morph.sort()

	print(statistics.mean(ave_morph))
	print(ave_morph[250])
	print(ave_morph[9750])

	'''

	if lang in ['mayo', 'mexicanero', 'nahuatl', 'wixarika']:

		with io.open(args.input + lang + '-task2-train_src', encoding = 'utf-8') as f:
			for line in f:
				toks = line.strip()
				all_form.append(toks)

		with io.open(args.input + lang + '-task2-train_trg', encoding = 'utf-8') as f:
			for line in f:
				toks = line.strip()
				all_seg.append(toks)

		with io.open(args.input + lang + '-task2-dev_src', encoding = 'utf-8') as f:
			for line in f:
				toks = line.strip()
				all_form.append(toks)

		with io.open(args.input + lang + '-task2-dev_trg', encoding = 'utf-8') as f:
			for line in f:
				toks = line.strip()
				all_seg.append(toks)

		with io.open(args.input + lang + '-task2-test_src', encoding = 'utf-8') as f:
			for line in f:
				toks = line.strip()
				all_form.append(toks)

		with io.open(args.input + lang + '-task2-test_trg', encoding = 'utf-8') as f:
			for line in f:
				toks = line.strip()
				all_seg.append(toks)

	### selecting 1,000 words for every language 

	old_all_form = all_form
	old_all_seg = all_seg
	all_form = []
	all_seg = []

	index = []
	i = 0
	while i < len(old_all_seg):
		index.append(i)
		i += 1

	### change k for minimal resource settings, or for experiments on languages other than seneca ###

	select = random.sample(index, k = int(args.k))

	for i in select:
		all_form.append(old_all_form[i])
		all_seg.append(old_all_seg[i])

	### generating train/dev/test split

	heldout_size = 0.6

	for z in range(1, 11):

		index = []
		i = 0
		while i < len(all_seg):
			index.append(i)
			i += 1

		random.shuffle(index)

		total = len(all_seg)
		num_train = total - int(heldout_size * total)
		num_dev = int(num_train / 2)

		train_src = io.open(args.output + lang + '_' + 'train_src' + '_' + str(z), 'w', encoding = 'utf-8')
		train_trg = io.open(args.output + lang + '_' + 'train_tgt' + '_' + str(z), 'w', encoding = 'utf-8')

		dev_src = io.open(args.output + lang + '_' + 'dev_src' + '_' + str(z), 'w', encoding = 'utf-8')
		dev_trg = io.open(args.output + lang + '_' + 'dev_tgt' + '_' + str(z), 'w', encoding = 'utf-8')

		test_src = io.open(args.output + lang + '_' + 'test_src' + '_' + str(z), 'w', encoding = 'utf-8')
		test_trg = io.open(args.output + lang + '_' + 'test_tgt' + '_' + str(z), 'w', encoding = 'utf-8')

		for i in index[ : num_train]:
			form = all_form[i]
			train_src.write(' '.join(c for c in form) + '\n')
			seg = all_seg[i]
			train_trg.write(' '.join(m for m in seg) + '\n')


		heldout_index = index[num_train : ]

		for i in heldout_index[ : num_dev]:
			form = all_form[i]
			dev_src.write(' '.join(c for c in form) + '\n')
			seg = all_seg[i]
			dev_trg.write(' '.join(m for m in seg) + '\n')


		for i in heldout_index[num_dev : ]:
			form = all_form[i]
			test_src.write(' '.join(c for c in form) + '\n')
			seg = all_seg[i]
			test_trg.write(' '.join(m for m in seg) + '\n')

		z += 1

'''
