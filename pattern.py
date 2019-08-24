class Pattern:
    def __init__(self, pattern, wildcard = None):
        self.pattern = pattern
        self.wildcard = wildcard
        self.case_sensitive = False

    def set_case_sensitive(self, case):
        self.case_sensitive = case

    def _new_wildcard(self, pattern, wildcard, text, start = 0):
        p_index = 1
        p_mod = pattern[:pattern.index(wildcard)]
        if text.find(p_mod, start) > -1:
            x = text.find(p_mod, start)
            while x < len(text):
                x += 1
                if p_index == len(pattern):
                    return text.find(p_mod, x-len(pattern))
                    break
                elif x == len(text):
                    return -1
                elif text[x] == pattern[p_index] or pattern[p_index] == wildcard:
                    p_index += 1
                else:
                    p_index = 0
        else:
            return -1

    def findMatch(self, text, start = 0):
        if self.case_sensitive == False and not self.wildcard:
            return text.lower().find(self.pattern, start)
        elif self.case_sensitive == True and not self.wildcard:
            return text.find(self.pattern, start)
        elif self.case_sensitive == False and self.wildcard:
            return self._new_wildcard(self.pattern, self.wildcard, text.lower(), start)
        else:
            return self._new_wildcard(self.pattern, self.wildcard, text, start)

    def findMatches(self, text):
        matches = []
        x = 0
        while x < len(text):
            y = self.findMatch(text, x)
            if y == -1:
                break
            else:
                matches.append(y)
                x += y + 1
        return(matches)

    def __str__(self):
        if self.case_sensitive == False and self.wildcard == None:
            return("The pattern is " + self.pattern)
        elif self.case_sensitive == False and self.wildcard != None:
            return("The pattern is " + self.pattern + " and the wildcard is " + self.wildcard)
        elif self.case_sensitive == True and self.wildcard == None:
            return("The case sensitive pattern is " + self.pattern)
        else:
            return("The case sensitive pattern is " + self.pattern +
                    " and the wildcard is " + self.wildcard)

p = Pattern('abc')
text = 'abcabcabcabc'
print(p.findMatches(text))
