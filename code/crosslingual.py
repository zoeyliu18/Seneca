import io, os, argparse

def read_data(input):

	src_data = []
	tgt_data = []
	nosymbol = []

	with io.open(args.input + 'mayo_src', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			nosymbol.append(' '.join(c for c in toks))
			toks.append('MA')
			src_data.append(' '.join(c for c in toks))

	with io.open(args.input + 'mayo_tgt', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			tgt_data.append(' '.join(c for c in toks))

	with io.open(args.input + 'mexicanero_src', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			nosymbol.append(' '.join(c for c in toks))
			toks.append('ME')
			src_data.append(' '.join(c for c in toks))

	with io.open(args.input + 'mexicanero_tgt', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			tgt_data.append(' '.join(c for c in toks))

	with io.open(args.input + 'nahuatl_src', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			nosymbol.append(' '.join(c for c in toks))
			toks.append('NH')
			src_data.append(' '.join(c for c in toks))

	with io.open(args.input + 'nahuatl_tgt', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			tgt_data.append(' '.join(c for c in toks))

	with io.open(args.input + 'wixarika_src', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			nosymbol.append(' '.join(c for c in toks))
			toks.append('WX')
			src_data.append(' '.join(c for c in toks))

	with io.open(args.input + 'wixarika_tgt', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			tgt_data.append(' '.join(c for c in toks))

#	with io.open(args.input + 'seneca_other_transfer_src', encoding = 'utf-8') as f:
	with io.open(args.input + 'seneca_train_src_1', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			nosymbol.append(' '.join(c for c in toks))
			toks.append('SG')
			src_data.append(' '.join(c for c in toks))

#	with io.open(args.input + 'seneca_other_transfer_tgt', encoding = 'utf-8') as f:
	with io.open(args.input + 'seneca_train_tgt_1', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			tgt_data.append(' '.join(c for c in toks))

	with io.open(args.input + 'seneca_other_src', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			nosymbol.append(' '.join(c for c in toks))
			toks.append('SI')
			src_data.append(' '.join(c for c in toks))

	with io.open(args.input + 'seneca_other_tgt', encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			tgt_data.append(' '.join(c for c in toks))


	return src_data, tgt_data, nosymbol


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type = str, help = 'original high resource file')

	args = parser.parse_args()

	src_data, tgt_data, nosymbol = read_data(args.input)

	with io.open(args.input + 'seneca_crosslingual_domain_src', 'w', encoding = 'utf-8') as f:
		for tok in src_data:
			f.write(tok + '\n')

	with io.open(args.input + 'seneca_crosslingual_domain_tgt', 'w', encoding = 'utf-8') as f:
		for tok in tgt_data:
			f.write(tok + '\n')

'''
	with io.open(args.input + 'seneca_crosslingual_src', 'w', encoding = 'utf-8') as f:
		for tok in nosymbol:
			f.write(tok + '\n')

	with io.open(args.input + 'seneca_crosslingual_tgt', 'w', encoding = 'utf-8') as f:
		for tok in tgt_data:
			f.write(tok + '\n')
'''
