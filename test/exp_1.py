### Example.1

source = "ABACADABBACCADDABABACADAB"
target_alphabet = set({"A","B","C","D","AB","BA","AC","CA","AD","DA","BB","CC","DD"})

def train(source, max_D=3):
  """
  读取source code sequence，生成pattern dict
  max_D: int : 编码(codeword)最大长度
  """
  pattern_dict = dict()
  for step in range(1, max_D+1):
    # print(f"current step: {step}")
    for shift in range(step):
      # print(f"current shift: {shift}")
      for start in range(shift, len(source), step):
        substr = source[start:start+step]
        if substr not in pattern_dict:
          pattern_dict[substr] = 1
        else:
          pattern_dict[substr] += 1
  return pattern_dict

model = train(source, max_D=2)
print(model)
print("-----------test example.1-----------")
assert set(model.keys()) == target_alphabet
print("PASS")