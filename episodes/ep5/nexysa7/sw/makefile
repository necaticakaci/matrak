CC = riscv32-unknown-elf-gcc
OBJCOPY = riscv32-unknown-elf-objcopy
CFLAGS = -march=rv32i -mabi=ilp32 -nostdlib -Wl,-T,mem.ld

all: blink.hex knight.hex uart.hex

crt0.o: crt0.s
	$(CC) $(CFLAGS) -c crt0.s -o crt0.o

blink.elf: crt0.o blink.c
	$(CC) $(CFLAGS) crt0.o blink.c -o blink.elf

blink.bin: blink.elf
	$(OBJCOPY) -O binary blink.elf blink.bin

blink.hex: blink.bin
	python3 bin2hex.py -i blink.bin -o blink.hex

knight.elf: crt0.o knight.c
	$(CC) $(CFLAGS) crt0.o knight.c -o knight.elf

knight.bin: knight.elf
	$(OBJCOPY) -O binary knight.elf knight.bin

knight.hex: knight.bin
	python3 bin2hex.py -i knight.bin -o knight.hex

uart.elf: crt0.o uart.c
	$(CC) $(CFLAGS) crt0.o uart.c -o uart.elf

uart.bin: uart.elf
	$(OBJCOPY) -O binary uart.elf uart.bin

uart.hex: uart.bin
	python3 bin2hex.py -i uart.bin -o uart.hex

clean:
	rm -f crt0.o blink.elf blink.bin blink.hex knight.elf knight.bin knight.hex uart.elf uart.bin uart.hex
