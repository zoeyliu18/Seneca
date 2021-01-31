import io, os, argparse, random


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type = str, help = '.txt file of Seneca morphology')
	parser.add_argument('--n', type = str, help = 'path to generated segmentation data')

	args = parser.parse_args()

	n = args.n

	train = []
#	with io.open(args.input + 'seneca_other_train_src_' + str(n), encoding = 'utf-8') as f:
	with io.open(args.input + 'seneca_train_src_' + str(n), encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip()
			train.append(toks)

	dev = []
#	with io.open(args.input + 'seneca_other_dev_src_' + str(n), encoding = 'utf-8') as f:
	with io.open(args.input + 'seneca_dev_src_' + str(n), encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip()
			dev.append(toks)

	test = []
#	with io.open(args.input + 'seneca_other_test_src_' + str(n), encoding = 'utf-8') as f:
	with io.open(args.input + 'seneca_test_src_' + str(n), encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip()
			test.append(toks)

	for w in train:
		print(train.count(w))
		if train.count(w) > 1:
			print(w)
	for w in dev:
		if w in train:
			print(w)

	for w in test:
		if w in train:
			print(w)

	for w in test:
		if w in dev:
			print(w)