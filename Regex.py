from Token import Token
from TokenType import TokenType

class Regex:
    @staticmethod
    def isNum(token: str) -> bool:
        if token == TokenType.NUM:
            return True;
        else:
            return False;

    @staticmethod
    def isOP(token: str) -> bool:
        if(token == TokenType.MINUS or token == TokenType.PLUS or token == TokenType.SLASH or token == TokenType.STAR):
            return True;      
        else:
            return False;
