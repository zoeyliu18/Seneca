import io, os, argparse, string

punct = list(string.punctuation)


def read_data(file, path):

	data = []

	with io.open(path + file, encoding = 'utf-8') as f:
		for line in f:
			toks = line.strip().split()
			for w in toks:
				try:
					int(w)
				except:
					if w[0].isupper() is False and len(w) != 1:
						if '(' in w and ')' not in w:
							w = w.replace('(', '')
						if ')' in w and '(' not in w:
							w = w.replace(')', '')
						w = w.replace("'", "’")
						w = w.replace("’", "’")
						w = w.replace("‘", "’")
						w = w.replace("´", "’")
						w = w.replace("Ë", "ë")
						w = w.replace("I", "i")
						w = w.replace("b", "h")
						w = w.replace("W", "w")
						w = w.replace("T", "t")

						w = w.lower()

				data.append(w)

	return data

def has_punct(w):

	n = 0

	for c in w:
		if c in punct:
			n += 1

	return n

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type = str, help = 'original high resource file')
	parser.add_argument('--v', type = str, help = 'seneca vocab file')
	parser.add_argument('--output', type = str, help = 'original high resource file')

	args = parser.parse_args()

	### get punctuation that is within the vocabulary of grammar book and informal sources ###

	vocab = []

	with io.open(args.v, encoding = 'utf-8') as f:
		for line in f:
			c = line.strip().split()
			vocab.append(c[0])
	print(len(vocab))
	outfile = io.open(args.output, 'w', encoding = 'utf-8')

	upper = []

	for file in os.listdir(args.input):
		if file.startswith('Matthew'):

			for w in read_data(file, args.input):

				if w[0].isupper() is False:
					count = 0

					for c in w:
						if c not in vocab:
							count += 1

					if count == 0:
						outfile.write(' '.join(c for c in w) + '\n')

'''
			
				try:
					int(w)
			
				except:
					new_w = []
					for c in w:

					### if the character is not a punctuation or it is from the punctuation in the vocabulary ###

						if c not in punct or c in vocab:
							new_w.append(c)

					if len(new_w) != 0:

						### remove names ###

						if new_w[0].isupper() is False:

							outfile.write(' '.join(c for c in new_w) + '\n')

'''
