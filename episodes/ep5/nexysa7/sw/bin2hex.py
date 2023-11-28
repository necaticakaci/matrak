# Based on: https://github.com/sifive/freedom-elf2hex/blob/master/util/freedom-bin2hex.c

import sys

def help():
    print("Convert a binary file to a format that can be read in verilog via $readmemh().")
    print("By default read from stdin and write to stdout using a bit width of 8.")
    print("\n")
    print("python bin2hex.py [--help|-h] [--bit-width|-w INT] [--input|-i BIN] [--output|-o HEX]")

def dump(output_stream, byte_width, byte_array):
    byte_width = int(byte_width)
    for i in range(byte_width - 1, -1, -1):
        output_stream.write(f'{byte_array[i]:02x}')
    output_stream.write('\n')

def main():
    ARRAY_SIZE = 1024
    bit_width = 32
    input_stream = sys.stdin.buffer
    output_stream = sys.stdout

    for i in range(len(sys.argv)):
        if sys.argv[i] in ["--help", "-h"]:
            help()
            return
        if sys.argv[i] in ["--bit-width", "-w"]:
            if i + 1 == len(sys.argv):
                sys.stderr.write("No arg for --bit-width|-w option.\n")
                return 1
            bit_width = int(sys.argv[i + 1])
        if sys.argv[i] in ["--input", "-i"]:
            if i + 1 == len(sys.argv):
                sys.stderr.write("No arg for --input|-i option.\n")
                return 1
            input_stream = open(sys.argv[i + 1], 'rb')
        if sys.argv[i] in ["--output", "-o"]:
            if i + 1 == len(sys.argv):
                sys.stderr.write("No arg for --output|-o option.\n")
                return 1
            output_stream = open(sys.argv[i + 1], 'w')

    if bit_width < 8:
        sys.stderr.write("Bit width cannot be negative or less than 8.\n")
        return 2
    if bit_width % 8 != 0:
        sys.stderr.write("Cannot handle non-multiple-of-8 bit width yet.\n")
        return 2
    if bit_width > (ARRAY_SIZE * 8):
        sys.stderr.write("Bit width is out of range (max supported is 8192).\n")
        return 3

    byte_width = bit_width / 8
    byte_value = 0
    byte_count = 0
    byte_array = bytearray([0] * ARRAY_SIZE)

    while True:
        byte_value = input_stream.read(1)
        if not byte_value:
            break
        byte_array[byte_count] = ord(byte_value)
        byte_count += 1
        if byte_count == byte_width:
            byte_count = 0
            dump(output_stream, byte_width, byte_array)
            byte_array = bytearray([0] * ARRAY_SIZE)

    if byte_count > 0:
        dump(output_stream, byte_width, byte_array)

if __name__ == "__main__":
    main()
