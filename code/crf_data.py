import io, os, argparse, random, statistics


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type = str, help = '.txt file of Seneca morphology')
	parser.add_argument('--output', type = str, help = 'path to generated segmentation data')
	parser.add_argument('--lang', type = str, help = 'languages')

	args = parser.parse_args()

	lang = args.lang

	train = []
	dev = []
	test = []

	with io.open(args.input + lang + '_train_tgt_1', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			form = ''.join(c for c in toks)
			temp = ''.join(c for c in toks).split('!')
			
			form = form.replace('!', '')			
			seg = '/'.join(m for m in temp)

			train.append([form, seg])

	with io.open(args.input + lang + '_dev_tgt_1', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			form = ''.join(c for c in toks)
			temp = ''.join(c for c in toks).split('!')
			
			form = form.replace('!', '')			
			seg = '/'.join(m for m in temp)

			dev.append([form, seg])

	with io.open(args.input + lang + '_test_tgt_1', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			form = ''.join(c for c in toks)
			temp = ''.join(c for c in toks).split('!')
			
			form = form.replace('!', '')			
			seg = '/'.join(m for m in temp)

			test.append([form, seg])

	with io.open(args.output + lang + '_' + 'train' + '_1', 'w', encoding = 'utf-8') as f:
			for tok in train:
				f.write('\t'.join(w for w in tok) + '\n')

	with io.open(args.output + lang + '_' + 'dev' + '_1', 'w', encoding = 'utf-8') as f:
			for seg in dev:
				f.write('\t'.join(w for w in tok) + '\n')

	with io.open(args.output + lang + '_' + 'test' + '_1', 'w', encoding = 'utf-8') as f:
			for seg in test:
				f.write('\t'.join(w for w in tok) + '\n')



