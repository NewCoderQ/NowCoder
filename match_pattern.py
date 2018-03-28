class Solution(object):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    """
        p: 表示正则字符串
            '.' 表示可以匹配任意单个字符
            '*' 表示 * 之前的字符可以出现0,1或者多次
    """
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        # 第一个字符不会是 *
        first_match = bool(text) and pattern[0] in {text[0], '.'}

        # 需要考虑 * 在第二个元素的位置上
        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or                  # 处理 * 代表 0 的情况
                    first_match and self.isMatch(text[1:], pattern))
        else:       # 此处处理 pattern 第二个字符不是 * 的情况
            return first_match and self.isMatch(text[1:], pattern[1:])

if __name__ == '__main__':
    sol = Solution()
    print(sol.isMatch('abcdeefg', 'abcd.*fg'))