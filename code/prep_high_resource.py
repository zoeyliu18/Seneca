import io, os, argparse, random

def read_data(file):

	src_data = []
	tgt_data = []

	with io.open(file, encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split('\t')
		
			src = list(toks[0])
			src_data.append(src)
		
			seg = '!'.join(m for m in toks[2].split())
			tgt = list(seg)
			tgt_data.append(list(seg))

	return src_data, tgt_data


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type = str, help = 'original high resource file')
	parser.add_argument('--output', type = str, help = 'src and tgt file for high resource languages')
	parser.add_argument('--lang', type = str, help = 'language')

	args = parser.parse_args()

	src_data, tgt_data = read_data(args.input)
	print(len(src_data))
	print(len(tgt_data))

#	with io.open(args.output + 'high_resource_src', 'w', encoding = 'utf-8') as f:
#		for tok in src_data:
#			f.write(' '.join(c for c in tok) + '\n')

#	with io.open(args.output + 'high_resource_tgt', 'w', encoding = 'utf-8') as f:
#		for tok in tgt_data:
#			f.write(' '.join(c for c in tok) + '\n')

	
	index = []
	i = 0
	while i < len(src_data):
		index.append(i)
		i += 1

	random.shuffle(index)

	for i in range(5):

		select = random.sample(index, k = 6000)

		src_sample = []
		tgt_sample = []

		for idx in select:
			src_sample.append(src_data[idx])
			tgt_sample.append(tgt_data[idx])

		src_sample_train = src_sample[ : 2400]
		src_sample_dev = src_sample[2400: 3600]
		src_sample_test = src_sample[3600 : 6000]

		tgt_sample_train = tgt_sample[ : 2400]
		tgt_sample_dev = tgt_sample[2400: 3600]
		tgt_sample_test = tgt_sample[3600 : 6000]

		lang = args.lang

		with io.open(args.output + lang + '_train_src_' + str(i), 'w', encoding = 'utf-8') as f:
			for tok in src_sample_train:
				f.write(' '.join(c for c in tok) + '\n')

		with io.open(args.output + lang + '_dev_src_' + str(i), 'w', encoding = 'utf-8') as f:
			for tok in src_sample_dev:
				f.write(' '.join(c for c in tok) + '\n')

		with io.open(args.output + lang + '_test_src_' + str(i), 'w', encoding = 'utf-8') as f:
			for tok in src_sample_test:
				f.write(' '.join(c for c in tok) + '\n')

		with io.open(args.output + lang + '_train_tgt_' + str(i), 'w', encoding = 'utf-8') as f:
			for tok in tgt_sample_train:
				f.write(' '.join(c for c in tok) + '\n')

		with io.open(args.output + lang + '_dev_tgt_' + str(i), 'w', encoding = 'utf-8') as f:
			for tok in tgt_sample_dev:
				f.write(' '.join(c for c in tok) + '\n')

		with io.open(args.output + lang + '_test_tgt_' + str(i), 'w', encoding = 'utf-8') as f:
			for tok in tgt_sample_test:
				f.write(' '.join(c for c in tok) + '\n')



