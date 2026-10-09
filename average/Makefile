TARGET = average
ASM = nasm
ASMFLAGS = -f elf64
LD = ld

all: $(TARGET)

$(TARGET): main.o
	$(LD) -o $(TARGET) main.o

main.o: main.asm
	$(ASM) $(ASMFLAGS) main.asm -o main.o

run: $(TARGET)
	./$(TARGET) data.txt

clean:
	rm -f main.o $(TARGET)

.PHONY: all run clean
