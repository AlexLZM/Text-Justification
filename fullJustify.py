class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        current = []
        current_len = 0
        current_end = 0
        
        
        def add_line():
            '''
            Finish current line and add to result
            '''
            extra_space = (maxWidth - current_len)
            if (n:=len(current)) == 1: # single word line
                line = current[0] + ' ' * extra_space
                res.append(line)
                return
            
            if current_end: # handle last wordhttps://github.com/AlexLZM/Text-Justification
                add_to_end = (extra_space - n + 1)
                extra_space = n - 1
                current[-1] += ' ' * add_to_end
            
            each_add_up = extra_space // (n - 1)
            remain = extra_space % (n - 1)
            line = ''
            for i in range(n - 1):
                line += current[i] + ' ' * (each_add_up + (remain >0))
                remain -= 1
            line += current[-1]
            res.append(line)
            
            
        for word in words:
            if current_len + len(current) + (n:=len(word)) > maxWidth: 
                # condition to end line
                add_line()
                current = []
                current_len = 0
                
            current.append(word)
            current_len += n
                        
        current_end = 1  
        add_line()
        return res
                
            
            
