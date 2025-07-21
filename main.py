import octagon_module as oct
side_size = float(input("Введите длину стороны 8-угольника: "))
new_figura = oct.Octagon(side_size)
new_figura.print_flush()