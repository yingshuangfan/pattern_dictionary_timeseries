# A Huffman Tree Node
import heapq


class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        # tree direction (0/1)
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq


def tree2dict(node, val='', result=dict()):
    newVal = val + str(node.huff)

    if(node.left):
        tree2dict(node.left, newVal, result)
    if(node.right):
        tree2dict(node.right, newVal, result)

    if(not node.left and not node.right):
        # print(f"{node.symbol} -> {newVal}")
        result[node.symbol] = newVal

    return result


def build_huffman_tree(chars, freq):
  """
  # converting characters and frequencies into huffman tree nodes
  chars: symbols
  freqs: frequencies
  """
  nodes = []

  for x in range(len(chars)):
      heapq.heappush(nodes, node(freq[x], chars[x]))

  while len(nodes) > 1:
      left = heapq.heappop(nodes)
      right = heapq.heappop(nodes)

      # assign directional value to these nodes
      left.huff = 0
      right.huff = 1

      new_node = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
      heapq.heappush(nodes, new_node)

  return tree2dict(nodes[0])
