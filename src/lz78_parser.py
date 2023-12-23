def get_num_bit(value):
    num_bits = 0
    upper_bits = 1
    while upper_bits < value:
      upper_bits *= 2
      num_bits += 1
    return num_bits

def encode_LZ78(alphabet, data):
    print(f"input sequence: {data}")

    alphabet_tree = {chr: i for (i, chr) in enumerate(alphabet)}
    patterns = {tuple([c]): 0 for c in list(alphabet)}

    w = []
    phrases = []
    for c in data:
        wc = w + [c]
        if tuple(wc) in patterns:
            w = wc
        else:
            phrases.append(tuple(w))
            patterns[tuple(w)] += 1
            patterns[tuple(wc)] = 0
            w = [c]

    if w:
        phrases.append(tuple(w))
        patterns[tuple(w)] += 1

    prefix_tree = {phrase: i for (i, phrase) in enumerate(phrases)}

    alphabet_n_bits = get_num_bit(len(alphabet_tree))
    phrase_n_bits = get_num_bit(len(phrases))
    print(alphabet_n_bits, phrase_n_bits)

    encoded = []
    for phrase in phrases:
      prefix = phrase
      chr_index = 0
      if len(phrase) > 1:
        prefix = phrase[:-1]
        next_chr = phrase[-1]
        chr_index = alphabet_tree[next_chr]

      index = prefix_tree[prefix]
      encoded.append((phrase, format(index, "0"+str(phrase_n_bits)+"b") + format(index, "0"+str(alphabet_n_bits)+"b")))

    # encoded = [(phrase, code_tree[phrase]) for phrase in phrases]
    print(f"output sequence: {encoded}")
    return encoded

# 预处理
min_val = min(x)
max_val = max(x)
number_of_bins = 100
print(f"preprocess: min={min(x)}, max={max(x)}, #bins={number_of_bins}")

# Discretize the samples
d_x = uniform_quantization(x, min_val, max_val, number_of_bins)

# 初始化完整ALHABET
bin_size = (max_val - min_val) / number_of_bins
alphabet = [round(min_val + bin_size*(i+0.5), 4) for i in range(number_of_bins+1)]
print(alphabet)

# 使用LZ78完成编码，注意每个序列会独立构建code tree
c_x = encode_LZ78(alphabet, d_x)

# 计算压缩比
num_bits = sum([len(code) for (_, code) in c_x])
num_samples = sum([len(phrase) for (phrase, _) in c_x])
print(f"original: {64*N} bits, compressed: {num_bits} bits, compress ratio: {(1-float(num_bits)/(64*N))*100:.2f}")
print(num_samples, c_x[:5])