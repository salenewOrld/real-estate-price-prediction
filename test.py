import sys
if __name__ == '__main__':
    #print(sys.argv)
    if len(sys.argv) == 1:
        raise ValueError('No experiment name arg passed.')
    else :
        print('Got experiment name')