import numpy as np
### PDD-Parser (Encoder) 兼容 TIME-SEIRES

class PDD:

  def __init__(self, max_D):
    self.max_D = max_D          # maximum code depths
    self.pattern_dict = dict()  # {code_depth: patterns}
    self.code_scheme = dict()   # {code_depth: code schemes}

  def train(self, source):
    """build pattern dictionary"""
    code_depth = 1
    while code_depth <= self.max_D:
      self._train_depth(source, code_depth)
      code_depth += 1
    # print(self.pattern_dict)

  def init_alphabet(self, alphabet):
    """initialize full alphabet"""
    code_depth = 1
    if code_depth not in self.pattern_dict:
      self.pattern_dict[code_depth] = {}
    # 对于code_depth=1时，需要ALPHABET完全补足
    self.pattern_dict[code_depth] = {tuple([key]): 0 for key in alphabet}

  def build_code_scheme(self):
    """build huffman coding tree"""
    code_depth = 1
    while code_depth <= self.max_D:
      pattern_tb = self.pattern_dict[code_depth]
      codes = [code for code in pattern_tb.keys()]
      freqs = np.array([freq for freq in pattern_tb.values()])
      self.code_scheme[code_depth] = build_huffman_tree(codes, freqs)
      code_depth += 1

  def _train_depth(self, source, code_depth):
    """get pattern dict with given code_depth"""
    if code_depth not in self.pattern_dict:
      self.pattern_dict[code_depth] = {}

    pattern_dict = self.pattern_dict[code_depth]
    for start in range(len(source)-code_depth+1):
      substr = tuple(source[start:start+code_depth])  # use tuple as key
      if substr not in pattern_dict:
        pattern_dict[substr] = 1
      else:
        pattern_dict[substr] += 1
    self.pattern_dict[code_depth] = pattern_dict

  def parse(self, data):
    # print(f"input sequence: {data}")
    encoded = []
    v_c = 0
    depth = 1

    while v_c + depth - 1 < len(data):
      phrase = tuple(data[v_c:v_c+depth])
      if phrase in self.pattern_dict[depth]:
        if depth < self.max_D:
          depth += 1
        else:
          code = self.code_scheme[depth][phrase]
          encoded.append((phrase, code))

          v_c += depth
          depth = 1

      else:
        phrase = tuple(data[v_c:v_c+depth-1])
        code = self.code_scheme[depth][phrase]
        encoded.append((phrase, code))

        v_c += depth-1
        depth = 1

    # ending phrase
    if phrase and phrase in self.pattern_dict[depth]:
      code = self.code_scheme[depth][phrase]
      encoded.append((phrase, code))
    elif phrase:
      depth = 1
      code = self.code_scheme[depth][phrase]
      encoded.append((phrase, code))

    # print(f"encoded sequence: {encoded}")
    return encoded

encoder = PDD(max_D=3)
# 首先兜底完整的ALPHABET
bin_size = (max_val - min_val) / number_of_bins
alphabet = [round(min_val + bin_size*(i+0.5), 4) for i in range(number_of_bins)]
encoder.init_alphabet(alphabet)
# 对于每个序列独立调用train，生成或更新PDD，记录当前频率
encoder.train([1.65, 2.55, 3.45, 4.35, 5.25, 7.05, 7.95, 7.95, 8.85, 10.65])
encoder.train([1.65, 2.55, 3.45, 4.35, 5.25, 7.05, 7.95, 7.95, 8.85, 10.65])
encoder.train([1.65, 2.55, 3.45, 4.35, 5.25, 7.05, 7.95, 7.95, 8.85, 10.65])
# 遍历完整train data之后，基于当前频率构建code tree
encoder.build_code_scheme()
# 使用code tree完成编码，完成测试
encoder.parse([4.35, 5.25, 7.95, 7.05])