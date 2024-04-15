import glob
import random
import bz2
import json
import numpy as np

files = list(glob.glob('/data/htrc/**/*.json.bz2', recursive=True))
random.shuffle(files)
subset_files = files[:20]

word_counts = {}
for file in subset_files:
    print(file)
    with bz2.open(file, 'rt') as f:
        data = json.load(f)
        for page in data['features']['pages']:
            if 'body' in page and page['body'] is not None and 'tokenPosCount' in page['body'] and page['body']['tokenPosCount'] is not None:
                for word in page['body']['tokenPosCount']:
                    word_counts[word] = word_counts.get(word, 0) + 1

sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Among this random set of docs, make a list of the most frequent 10k words
most_freq_words = []
for word_pair in sorted_word_counts[:10000]:
    most_freq_words.append(word_pair[0])
most_freq_words_idxs = dict(zip(most_freq_words, range(len(most_freq_words))))
print(most_freq_words_idxs)

# Now, for each document in the glob (start with just 50 or so),
# make a vector representing the % of occurrences of each word among the top 10k
# (and if that word doesn't occur, it's 0.0)

num_to_process = 50
docvecs = np.zeros((num_to_process, len(most_freq_words)))
for idx, file in enumerate(files[:num_to_process]):
    print(file)
    with bz2.open(file, 'rt') as f:
        data = json.load(f)
        for page in data['features']['pages']:
            if 'body' in page and page['body'] is not None and 'tokenPosCount' in page['body'] and page['body']['tokenPosCount'] is not None:
                for word in page['body']['tokenPosCount']:
                    if word in most_freq_words_idxs:
                        docvecs[idx][most_freq_words_idxs[word]] = 1

print(docvecs)
np.save('docvecs.npy', docvecs)


