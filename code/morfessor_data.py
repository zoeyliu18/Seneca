import io, os, argparse, random, statistics


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type = str, help = 'input path')
	parser.add_argument('--output', type = str, help = 'path to generated segmentation data')
	parser.add_argument('--lang', type = str, help = 'languages')

	args = parser.parse_args()

	lang = args.lang

	train_seg = []
	dev_seg = []
	test_seg = []

	with io.open(args.input + lang + '_train_tgt_1', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			temp = ''.join(c for c in toks).split('!')
			seg = ' + '.join(m for m in temp)

			train_seg.append(seg)

	with io.open(args.input + lang + '_dev_tgt_1', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			temp = ''.join(c for c in toks).split('!')
			seg = ' + '.join(m for m in temp)

			dev_seg.append(seg)

	with io.open(args.input + lang + '_test_tgt_1', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			temp = ''.join(c for c in toks).split('!')
			seg = ' + '.join(m for m in temp)

			test_seg.append(seg)

	with io.open(args.output + lang + '_' + 'train' + '_1', 'w', encoding = 'utf-8') as f:
			for seg in set(train_seg):
				c = train_seg.count(seg)
				f.write(str(c) + ' ' + seg + '\n')

	with io.open(args.output + lang + '_' + 'dev' + '_1', 'w', encoding = 'utf-8') as f:
			for seg in set(dev_seg):
				c = dev_seg.count(seg)
				f.write(str(c) + ' ' + seg + '\n')

	with io.open(args.output + lang + '_' + 'test' + '_1', 'w', encoding = 'utf-8') as f:
			for seg in set(test_seg):
				c = test_seg.count(seg)
				f.write(str(c) + ' ' + seg + '\n')

	with io.open(args.output + lang + '_' + 'train_word' + '_1', 'w', encoding = 'utf-8') as f:
			for seg in set(train_seg):
				c = train_seg.count(seg)
				seg = seg.replace(' + ', '')
				f.write(str(c) + ' ' + seg + '\n')

	with io.open(args.output + lang + '_' + 'dev_word' + '_1', 'w', encoding = 'utf-8') as f:
			for seg in set(dev_seg):
				c = dev_seg.count(seg)
				seg = seg.replace(' + ', '')
				f.write(str(c) + ' ' + seg + '\n')

	with io.open(args.output + lang + '_' + 'test_word' + '_1', 'w', encoding = 'utf-8') as f:
			for seg in set(test_seg):
				c = test_seg.count(seg)
				seg = seg.replace(' + ', '')
				f.write(str(c) + ' ' + seg + '\n')


