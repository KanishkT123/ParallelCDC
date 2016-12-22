
import sys

def main():
    new_f = open('allhomes', 'w+')
    for i in range(1, 17):
        print("Currently reading file {0}".format(i))
        try:
            with open('homes' + str(i), 'r') as f:
                for line in f:
                    new_f.write(line)
        except:
            continue

if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    else:
        print("Usage: fastcdc.py <databuffer>")