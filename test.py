import time

status = None
symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
i = 0
while status is (None):
    i = (i + 1) % len(symbols) #disabled
    print('\r\033[K%s Uploading' % symbols[i], flush=True, end='')
    time.sleep(0.08)