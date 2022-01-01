
from typing import List
import numpy as np

def is_predecessor(x: str, y: str) -> bool:
    """ Return true if x is a predecessor of y"""
    if len(y) != len(x) + 1:
        return False

    idx = 0
    for idx in range(len(x)+1):
        if idx == len(x) or x[idx] != y[idx]:
            break 
    return x[idx:] == y[idx+1:]

def longestStrChain(words: List[str]) -> int:
    """ Find the longest possible word chain from words. 
        Word chain is an array of words where w[i+1] can be obtained from w[i] 
        by inserting one letter 
    """
    words_sorted = sorted(words, key=len) # sort words by length
    dp = [-1]*len(words_sorted) # store length of lonstest word chain starting from word i
    for i in range(len(words_sorted)):
        longestStrChainRec(words_sorted, i, dp)

    max_length = -1
    for lenth in dp:
        if lenth > max_length:
            max_length = lenth
    
    print("results: {}".format(dp))
    return max_length
    
def longestStrChainRec(words: List[str], idx: int, dp: List[int]) -> int:
    """ Find the longest word chain starting from word[idx] """
    if dp[idx] > 0:
        return dp[idx] # check if dp[idx] has been precomputed
        
    word = words[idx]
    sucessors = [] 
    # find all possible successors for w[idx]
    for i in range(idx+1, len(words)):
        word2 = words[i]
        if len(word2) == len(word):
            pass
        elif len(word2) == len(word)+1 and is_predecessor(word, word2):
            # word2 is a successor
            sucessors.append(i) 
        elif len(word2) > len(word)+1:
            break

    if not sucessors:
        dp[idx] = 1
        return 1

    candidate_lengths = list(map(lambda x:longestStrChainRec(words,x,dp), sucessors))
    max_length = max(candidate_lengths) + 1
    dp[idx] = max_length
    return max_length



if __name__ == '__main__':
    words = ["a","b","bda","bdca","ba","bca"]
    result = longestStrChain(words)
    print("words: {}".format(words))
    print("length: {}".format(result))
    words2 = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
    result2 = longestStrChain(words2)
    print("words2: {}".format(words2))
    print("length2: {}".format(result2))

    

    



    








    


    


    
    



    
        
