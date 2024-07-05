"""
Write Python code to generate Init function of GPIO for AVR

"""

port = input("Please Enter the port number (A, B, C, or D): ")
bitMode = []
for i in range(0, 8):
    mode = input(f"Please enter Bit {i} mode (in or out): ")
    if mode == "in":
        bitMode.append("0")
    else:
        bitMode.append("1")

bitMode.reverse()
bits = "".join(bitMode)

with open("init.c", "w") as f:
    f.write(f"void Init_Port{port}_DIR (void)\n")
    f.write("{\n")
    f.write(f"  DDR{port} = 0b{bits}\n")
    f.write("}")


