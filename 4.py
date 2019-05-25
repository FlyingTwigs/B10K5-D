import math


def cetak_gambar(number_of_coloumn_and_rows):
    result = ""

    for baris in range(number_of_coloumn_and_rows):
        for kolom in range(number_of_coloumn_and_rows):
            if (baris == 0 or baris == number_of_coloumn_and_rows-1 or kolom == math.floor(number_of_coloumn_and_rows/2)):
                result += "X "
            else:
                result += "= "
        result += "\n"

    return result


# contoh
print(cetak_gambar(7))
