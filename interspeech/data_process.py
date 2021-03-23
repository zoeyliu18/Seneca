import io, os, argparse, random, statistics


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type = str, help = 'input .txt file from Robbie')
	parser.add_argument('--output', type = str, help = 'output src and tgt file')

	args = parser.parse_args()

	src_data = []
	tgt_data = []

	with io.open(args.input, encoding = 'utf-8') as f:
		for line in f:
		
			toks = line.split()
		
			seg = (' '.join(m for m in toks[1 : ])).replace(' + ', '!')
		
			tgt = list(seg)

			src = list(seg.replace('!', ''))

			src_data.append(src)
			tgt_data.append(tgt)

	with io.open(args.output + 'interspeech_src.txt', 'w', encoding = 'utf-8') as f:
		for tok in src_data:
			f.write(' '.join(c for c in tok) + '\n')

	with io.open(args.output + 'interspeech_tgt.txt', 'w', encoding = 'utf-8') as f:
		for tok in tgt_data:
			f.write(' '.join(c for c in tok) + '\n')

