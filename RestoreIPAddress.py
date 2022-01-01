from typing import List, Dict, Tuple, Optional
from collections import defaultdict

def restoreIpAddresses(s: str) -> List[str]:
    """ Find all possible IP addresses that can be represented by s"""
    dp = defaultdict(lambda: defaultdict(lambda: None))
    # create a two-leve dictionary: str -> int -> result that stores computed addresses 
    # for each query with suffix s and number of fields n 
    result = restoreIpAddressesAux(s, 4, dp)
    return result

def restoreIpAddressesAux(s: str, n: int, dp) -> List[str]:
    """ Find all possible addresses with n fields that can be represented by s"""
    if dp[s][n] is not None:
        return dp[s][n] 
        # check if this query has been computed
    if s == "" and n == 0:
        return [""]
    elif len(s) > 0 and n == 0:
        return []
    elif len(s) > n*3 or len(s) < n:
        return []

    def is_valid_prefix(p: str):
        # check if p is a valid prefix
        if p == '0':
            return True
        elif p[0] == '0':
            return False
        else:
            return int(p) >= 0 and int(p) <= 255

    result = []
    for i in range(1, min(3,len(s))+1):
        prefix, s2 = s[:i], s[i:]
        result2 = restoreIpAddressesAux(s2, n-1, dp)
        if not is_valid_prefix(prefix):
            continue
        for addr in result2:
            if addr == "":
                addr = prefix
            else:
                addr = prefix + "." + addr
            result.append(addr)

    dp[s][n] = result
    return result


if __name__ == '__main__':
    s = "25525511135"
    result = restoreIpAddresses(s)
    print("Result: {}".format(result))
    s2 = "101023"
    result = restoreIpAddresses(s2)
    print("Result: {}".format(result))


    