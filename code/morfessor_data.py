import io, os, argparse, random, statistics


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type = str, help = 'input path')
	parser.add_argument('--output', type = str, help = 'path to generated segmentation data')
	parser.add_argument('--lang', type = str, help = 'languages')
	parser.add_argument('--m', help = 'multi-task or not')
	parser.add_argument('--x', help = 'using Mexican languages or not')
	parser.add_argument('--e', help = 'experiment 1 or 2')

	args = parser.parse_args()

	lang = args.lang

	train_src = []

	train_seg = []
	dev_seg = []
	test_seg = []

	with io.open(args.input + lang + '_train_src_1', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			train_src.append(toks[-1])


	with io.open(args.input + lang + '_train_tgt_1', encoding = 'utf-8') as f:
		for line in f:
			toks = ''
			if args.x == 'x':
				toks = line.strip().replace('+', ' -').split()
			else:
				toks = line.strip().split()

			temp = ''.join(c for c in toks).split('!')
			seg = ' + '.join(m for m in temp)

			train_seg.append(seg)

	if args.e:
		with io.open(args.input + args.e + '_dev_tgt_1', encoding = 'utf-8') as f:
			for line in f:
				toks = line.strip().split()
				temp = ''.join(c for c in toks).split('!')
				seg = ' + '.join(m for m in temp)

				dev_seg.append(seg)

	else:
		with io.open(args.input + lang + '_dev_tgt_1', encoding = 'utf-8') as f:
			for line in f:
				toks = line.strip().split()
				temp = ''.join(c for c in toks).split('!')
				seg = ' + '.join(m for m in temp)

				dev_seg.append(seg)

#	with io.open(args.input + lang + '_test_tgt_1', encoding = 'utf-8') as f:
#		for line in f:
#			toks = line.strip().split()
#			temp = ''.join(c for c in toks).split('!')
#			seg = ' + '.join(m for m in temp)

#			test_seg.append(seg)

	if args.m == 'm':

		old_train_seg = train_seg
		train_seg = []

		for tok in zip(old_train_seg, train_src):
			new = tok[0] + ' + ' + tok[-1]
			train_seg.append(new)

	with io.open(args.output + lang + '_' + 'train', 'w', encoding = 'utf-8') as f:
			for seg in set(train_seg):
				c = train_seg.count(seg)
				f.write(str(c) + ' ' + seg + '\n')

#	with io.open(args.output + lang + '_' + 'test', 'w', encoding = 'utf-8') as f:
#			for seg in set(test_seg):
#				c = test_seg.count(seg)
#				f.write(str(c) + ' ' + seg + '\n')
	

	with io.open(args.output + lang + '_' + 'train_word', 'w', encoding = 'utf-8') as f:
		for seg in train_seg:
			#	c = train_seg.count(seg)
				seg = seg.replace(' + ', '')
			#	f.write(str(c) + ' ' + seg + '\n')
				f.write(seg + '\n')

	if args.e:

		with io.open(args.output + args.e + '_' + 'dev_word', 'w', encoding = 'utf-8') as f:
			for seg in dev_seg:
			#	c = dev_seg.count(seg)
				seg = seg.replace(' + ', '')
			#	f.write(str(c) + ' ' + seg + '\n')
				if args.m == 'm':
					f.write(seg + 'Y' + '\n')
				else:
					f.write(seg + '\n')

	else:

		with io.open(args.output + lang + '_' + 'dev_word', 'w', encoding = 'utf-8') as f:
			for seg in dev_seg:
			#	c = dev_seg.count(seg)
				seg = seg.replace(' + ', '')
			#	f.write(str(c) + ' ' + seg + '\n')
				if args.m == 'm':
					f.write(seg + 'Y' + '\n')
				else:
					f.write(seg + '\n')

#	with io.open(args.output + lang + '_' + 'test_word', 'w', encoding = 'utf-8') as f:
#			for seg in test_seg:
			#	c = test_seg.count(seg)
#				seg = seg.replace(' + ', '')
			#	f.write(str(c) + ' ' + seg + '\n')
#				f.write(seg + '\n')




