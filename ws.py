import glob
import random
import bz2
import json
import numpy as np
import time
import rich.progress
import faiss

num_words_to_keep = 10000

files = list(glob.glob('/data/htrc/**/*.json.bz2', recursive=True))
subset_files = random.sample(files, 50)

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
for word_pair in sorted_word_counts[:num_words_to_keep]:
    most_freq_words.append(word_pair[0])
most_freq_words_idxs = dict(zip(most_freq_words, range(len(most_freq_words))))
print(most_freq_words_idxs)

# save most frequent words to a file
with open('most_freq_words.json', 'w') as f:
    json.dump(most_freq_words_idxs, f)


num_to_process = 1000

faiss_index = faiss.IndexFlatL2(len(most_freq_words))

files_to_process = random.sample(files, num_to_process)
file_ids = {}
with rich.progress.Progress() as progress:
    task = progress.add_task("Processing files...", total=num_to_process)
    for idx, file in enumerate(files_to_process):
        print(file)
        file_ids[idx] = file
        docvec = np.zeros(len(most_freq_words))
        with bz2.open(file, 'rt') as f:
            data = json.load(f)
            for page in data['features']['pages']:
                if 'body' in page and page['body'] is not None and 'tokenPosCount' in page['body'] and page['body']['tokenPosCount'] is not None:
                    for word in page['body']['tokenPosCount']:
                        if word in most_freq_words_idxs:
                            docvec[most_freq_words_idxs[word]] = 1
        faiss_index.add(np.array([docvec]))
        progress.update(task, advance=1)

faiss.write_index(faiss_index, 'index.faiss')

# save file ids to a file
with open('file_ids.json', 'w') as f:
    json.dump(file_ids, f)

