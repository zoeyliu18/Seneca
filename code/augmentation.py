import io, os, argparse, random, statistics, itertools


def read_data(file):

	data = []

	with io.open(file, encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			data.append(''.join(w for w in toks))

	return data


### A ! B ! C ###
### A ! B ###
### maintain morpheme order ###

def cropping(data):
	
	new_data = []

	for seg in data:
		seg = seg.split('!')

		if len(seg) > 2:

			i = 1

			while i < len(seg) - 1:
				new_data.append('!'.join(m for m in seg[0 : i + 1]))
				new_data.append('!'.join)
				i += 1

	return list(set(new_data))


### A ! B ! C ###
### B ! A ! C ###

def rotation(data):

	new_data = []

	for seg in data:
		seg = seg.split('!')

		if len(seg) > 1:
			random.shuffle(seg)

			all_candidates = list(itertools.permutations(seg))

			for tok in all_candidates:
				tok = list(tok)
				if tok != seg:
					new_data.append('!'.join(m for m in tok))

	return list(set(new_data))


### A ! B ! C ###
### B ! A ###

def cropping_rotation(data):


	### generate rotation data for all words ###

	rotation_data = rotation(data)

	### combine rotation data with original data ###

	all_data = rotation_data + data

	### cropping all data ###

	return cropping(all_data)


### asdfwef --> asdfwef ###

def get_vocab(data):

	all_chr = []

	for seg in data:
		seg = seg.split('!')
		for morph in seg:
			morph = list(morph)
			for m in morph:
				all_chr.append(m)

	vocab = list(set(all_chr))

	return vocab

### A ! B ! C ###
### B A C ###

def dar_true(data):

	new_data = []

	for seg in data:
		seg = seg.split('!')

		if len(seg) > 1:
			random.shuffle(seg)

			all_candidates = list(itertools.permutations(seg))

			for tok in all_candidates:
				tok = list(tok)
				if tok != seg:
					new_data.append(''.join(m for m in tok))

	return list(set(new_data))


def dar_random(data):

	vocab = get_vocab(data)

	new_data = []

	all_length = []

	for seg in data:
		seg = seg.split('!')
		length = 0
		for m in seg:
			length += len(m)
		all_length.append(length)

	max_len = max(all_length) ### longest word

	idx = 0

	while idx < 10:

		for i in range(len(data)):
			length = 0
			while length == 0:
				length = random.choice(range(max_len))

			random_string = ''.join(random.choice(vocab) for idx in range(length))
			new_data.append(random_string)

		idx += 1

	return list(set(new_data))


def add_random(data):

	vocab = get_vocab(data)

	new_data = []

	all_length = []

	for seg in data:
		seg = seg.split('!')
		for m in seg:
			all_length.append(len(m))

	max_len = max(all_length)   ### longest morpheme

	for i in range(len(data)):
		length = 0
		while length == 0:
			length = random.choice(range(max_len))

		random_string = ''.join(random.choice(vocab) for idx in range(length))
		new_seg = data[i] + '!' + random_string
		new_data.append(new_seg)

	return list(set(new_data))


###### hallucination #####


def get_morph(data):

	all_morph = []

	for seg in data:
		seg = seg.split('!')
		for m in seg:
			all_morph.append(m)

	return set(all_morph)


def new_morph(morph, vocab, morph_list):

	new_morph = [morph[0]]

	for c in list(morph[1 : -1]):
		random_c = random.choice(vocab)
		new_morph.append(random_c)

	new_morph.append(morph[-1])

	return ''.join(c for c in new_morph)


def hallucinate(data):

	vocab = get_vocab(data)

	all_morph = get_morph(data)

	new_data = []

	for seg in data:
		seg = seg.split('!')

		idx = 0

		while idx < 10:

			for i in range(len(seg)):
				new_seg = []
		
				if len(seg[i]) >= 3:
					m = seg[i]
			
					new_m = new_morph(m, vocab, all_morph)

					while new_m in all_morph:
						new_m = new_morph(m, vocab, all_morph)

					for z in range(i):
						new_seg.append(seg[z])

					new_seg.append(new_m)

					for z in range(i + 1, len(seg)):
						new_seg.append(seg[z])

					if len(new_seg) != 0:

						new_data.append('!'.join(m for m in new_seg))

			idx += 1

	return new_data

def bible(data, bible):

	bible_src = []
	bible_tgt = []

	with io.open(bible, encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip()
			bible_src.append(toks + ' Z')
			bible_tgt.append(toks)

	return bible_src, bible_tgt


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type = str, help = 'training tgt file')
	parser.add_argument('--output', type = str, help = 'path to augmented training file; both src + tgt')
	parser.add_argument('--method', type = str, help = 'augmentation method')
	parser.add_argument('--dev', help = 'file to be modifed for multi-task learning')
	parser.add_argument('--test', help = 'file to be modifed for multi-task learning')
	parser.add_argument('--k', help = 'augmentation size')
	parser.add_argument('--bible', help = 'bible file')

	args = parser.parse_args()

	all_methods = {'c': cropping, 
					'r': rotation, 
					'cr': cropping_rotation, 
					'dart': dar_true, 
					'multit': dar_true, 
					'darr': dar_random, 
					'multir': dar_random, 
					'ar': add_random, 
					'h': hallucinate,
					'b': bible
					}

	original = read_data(args.input)

	augmented_data = ''

	dev_data = []
	test_data = []

	if args.method in ['c', 'r', 'ar', 'h']:
		augmented_data = all_methods[args.method](original) + original

	if args.method in ['cr']:
		augmented_data = all_methods[args.method](original)

	if args.method in ['dart', 'darr']:
		augmented_data = all_methods[args.method](original) + original

	if args.method in ['multit', 'multir']:
		new_original = []
		for tok in original:
			tok = tok + 'Q'
			new_original.append(tok)

		new_augmentation = []
		for tok in all_methods[args.method](original):
			tok = tok + 'Q'
			new_augmentation.append(tok)

		augmented_data = new_augmentation + new_original

		if args.dev:

			with io.open(args.dev, encoding = 'utf-8') as f:
				for line in f:
					toks = line.strip().split()
					toks.insert(0, 'Q')
					dev_data.append(toks)

		if args.test:

			with io.open(args.test, encoding = 'utf-8') as f:
				for line in f:

					toks = line.strip().split()
					toks.insert(0, 'Q')
					test_data.append(toks)


	## copy: A ! B ! C --> A ! B ! C ##
	## switch: A ! B ! C --> A  B  C ##

	if args.method in ['copy', 'switch']:
		augmented_data = original


	### multi-task with bible data ###

	bible_src = ''
	bible_tgt = ''

	if args.method in ['b']:
		bible_src, bible_tgt = all_methods[args.method](original, args.bible)
		augmented_data = original 

	name = args.input.split('/')[-1]


	if len(dev_data) != 0:
		dev_name = args.dev.split('/')[-1] + '_' + args.method

		with io.open(args.output + dev_name, 'w', encoding = 'utf-8') as f:
			for tok in dev_data:
				f.write(' '.join(w for w in tok) + '\n')

	if len(test_data) != 0:
		test_name = args.test.split('/')[-1] + '_' + args.method

		with io.open(args.output + test_name, 'w', encoding = 'utf-8') as f:
			for tok in test_data:
				f.write(' '.join(w for w in tok) + '\n')


	if args.k:
		augmented_data = random.choices(augmented_data, k = args.k)

	tgt_data = []
	src_data = []

	for seg in augmented_data:
		seg = list(seg)
		tgt_data.append(seg)
		if args.method in ['copy']:
			src_data.append(seg)
		if args.method in ['b']:
			new_seg = [m for m in seg if m != '!']
			new_seg.append('Y')
			src_data.append(new_seg)
		else:
			src_data.append([m for m in seg if m != '!'])

	if args.method == 'b':
		for seg in bible_tgt:
			tgt_data.append(seg.split())
		for seg in bible_src:
			src_data.append(seg.split())

	if args.method == 'switch':

		for seg in augmented_data:
			seg = list(seg)
			tgt_data.append([m for m in seg if m != '!'])
			src_data.append(seg)
		

	with io.open(args.output + name + '_' + args.method, 'w', encoding = 'utf-8') as f:
		for tok in tgt_data:
		#	f.write(' '.join(m for m in tok if m not in ['Q', 'W']) + '\n')
			f.write(' '.join(m for m in tok) + '\n')

	src_name = name.replace('tgt', 'src')

	with io.open(args.output + src_name + '_' + args.method, 'w', encoding = 'utf-8') as f:
		for tok in src_data:
			f.write(' '.join(m for m in tok) + '\n')
