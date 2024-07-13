def print_hex_row(offset, cols):
    r1 = " __" * cols
    r2 = "/  \\" * cols + "/"
    r3 = "\\__/" * cols + "\\"

    if offset:
        print("   " + r1)
        print("  " + r2)
        print("  " + r3)
    else:
        print(r1)
        print(r2)
        print(r3)

def hexagon(rows, cols):
    for r in range(rows):
        offset = r % 2 == 1
        print_hex_row(offset, cols)


print("Hexagon(4 rows, 7 columns):")
hexagon(4, 7)

print("\nHexagon (3 rows, 5 columns):")
hexagon(3, 5)



