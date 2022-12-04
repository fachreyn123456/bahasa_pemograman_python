def hitung():
    sub_total = int(input("Sub Total : "))
    ppn = 0.1 #10%
    total_ppn = sub_total * ppn
    grand_total = float(sub_total + total_ppn)
    return sub_total,ppn,grand_total,total_ppn

sub_total,ppn,grand_total,total_ppn = hitung()
def printDat():
    print("======================")
    print("Total PPN : ",total_ppn)
    print("Grand Total : ",grand_total)
    

printDat()
 