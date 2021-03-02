import io, os, argparse


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type = str, help = 'original file')
	parser.add_argument('--output', type = str, help = 'output file')

	args = parser.parse_args()

	src_data = []

	with io.open(args.input, encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			toks.append('Y')
			src_data.append(' '.join(c for c in toks))

	with io.open(args.output, 'w', encoding = 'utf-8') as f:
		for tok in src_data:
			f.write(tok + '\n')
