### Example.2
import numpy as np
from collections import deque

source = "ABACADABBACCADDABABACADAB"
target_code_scheme = {
  1: set({('A', '0.4400', 1), ('B', '0.2400', 2), ('C', '0.1600', 3), ('D', '0.1600', 3)}),
  2: set({('AB', '0.2083', 2), ('BA', '0.1667', 3), ('AC', '0.1250', 3), ('CA', '0.1250', 3), ('AD', '0.1250', 3), ('DA', '0.1250', 3), ('BB', '0.0417', 4), ('CC', '0.0417', 5), ('DD', '0.0417', 5)}),
  3: set({('ABA', '0.1304', 3), ('BAC', '0.1304', 3), ('CAD', '0.1304', 3), ('DAB', '0.1304', 3), ('ACA', '0.0870', 4), ('ADA', '0.0870', 4), ('ABB', '0.0435', 4), ('BBA', '0.0435', 4), ('ACC', '0.0435', 4)})
}

def train(source, code_depth):
  """
  读取source code sequence，生成pattern dict
  max_D: int : 编码(codeword)最大长度
  """
  pattern_dict = dict()
  for start in range(len(source)-code_depth+1):
    substr = source[start:start+code_depth]
    if substr not in pattern_dict:
      pattern_dict[substr] = 1
    else:
      pattern_dict[substr] += 1
  return pattern_dict


def test_case2(code_depth=1):
  print(f"-----------code  depth: {code_depth}-----------")
  pattern_tb = train(source, code_depth)
  print(pattern_tb)
  codes = [code for code in pattern_tb.keys()]
  freqs = np.array([freq for freq in pattern_tb.values()])

  probs = freqs / np.sum(freqs)
  prob_tb = {c:p for c, p in zip(codes, probs)}

  scheme_tb = build_huffman_tree(codes, freqs)
  # print(scheme_tb)
  # formatted_scheme_set = set({(k, f"{prob_tb[k]:.4f}", len(v)) for k, v in scheme_tb.items()})
  # print(formatted_scheme_set)
  # assert formatted_scheme_set == target_code_scheme[code_depth]
  # print("PASSED")


print("-----------test example.2-----------")
test_case2(code_depth=1)

test_case2(code_depth=2)

test_case2(code_depth=3)