    def evalRPN(self, tokens):
        op=['+','-','*','/']
        list_tokens=[]
        for token in tokens:
            if token not in op:
                list_tokens.append(token)
            else:
                oparand2=float(list_tokens.pop())
                oparand1=float(list_tokens.pop())
                if token == '+':
                    result=oparand1 + oparand2
                elif token == '-':
                    result=oparand1 - oparand2
                elif token == '*':
                    result=oparand1 * oparand2
                elif token == '/':
                    result=oparand1 / oparand2
                list_tokens.append(result)
        return int(list_tokens.pop())