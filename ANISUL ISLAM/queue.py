# FIFO: First In Last Out
from collections import deque

bank = deque(['x', 'y', 'z'])
bank.popleft()
print(bank)
bank.popleft()
bank.popleft()

if not bank:
    print('No persons left')