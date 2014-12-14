class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        op=['+','-','*','/']
        list_tokens=[]
        for token in tokens:
            if token not in op:
                list_tokens.append(int(token))
            else:
                oparand2=int(list_tokens.pop())
                oparand1=int(list_tokens.pop())
                         
                if token == '+':
                    result=oparand1 + oparand2
                elif token == '-':
                    result=oparand1 - oparand2
                elif token == '*':
                    result=oparand1 * oparand2
                elif token == '/':
                    if oparand1 * oparand2 < 0 and oparand1 % oparand2:
                        result=(oparand1 / oparand2 + 1)
                    else:
                        result=(oparand1) / oparand2
                
                list_tokens.append(result)
        return ((list_tokens.pop()))