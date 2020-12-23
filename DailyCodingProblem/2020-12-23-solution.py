# a=1, b=2, c=3 .... z=26
# How many ways a message can be decoded?

# '111'  returns 3 => 'aaa', 'ka', 'ak'
# Messages are always decodable

# '1234' -> 'abcd' ('1,2,3,4'), 'lcd' ('12,3,4'), 'axd' ('1,23,4')

encoded_message = '12452351'

possible_decoded_messages = []

def helper(data,k,memo) :
    if k==0:
        return 1
    s = len(data) - k
    if data[s] == '0':
        return 0
    if memo[k] != -1:
        return memo[k]
    result = helper(data, k-1, memo)
    if k>= 2 and int(data[s:s+2]) <= 26:
        result += helper(data, k-2, memo)
    memo[k] = result
    return result


def num_ways(data):
    memo = [-1]*(len(data)+1)
    return helper(data,len(data), memo)

print(num_ways('111'))
print(num_ways('11'))
print(num_ways('12345'))
print(num_ways('223412'))