#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.



#num = input()

def reverseNum(num):
    if -2**31 < reversedNum & reversedNum > 2**31: return 0
    else:
        if num <0:
            num = -1*num
            positiveNegative = -1
        else:
            positiveNegative = 1

        reversedNum = 0
        while num !=0:
            lastDigit = num % 10
            num = (num - lastDigit)/10
            reversedNum = reversedNum*10 + lastDigit

        return reversedNum * positiveNegative


