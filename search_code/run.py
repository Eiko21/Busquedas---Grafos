# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
nt = search.GPSProblem('N', 'T', search.romania)
an = search.GPSProblem('A', 'N', search.romania)
eo = search.GPSProblem('E', 'O', search.romania)
az = search.GPSProblem('A', 'Z', search.romania)

print "//----------------- BUSQUEDAS EN LAS CARRETERAS DE RUMANIA -----------------//"

print "\n 1) Busqueda en el Trayecto AB:"
print "El resultado por Ramificacion y Acotacion es: ",  search.ram_acot_graph_search(ab).path()
print "El resultado por Ramificacion y Acotacion con Subestimacion es: ", search.ram_acot_subest_graph_search(ab).path()
print "El resultado por busqueda en anchura es: ", search.breadth_first_graph_search(ab).path()
print "El resultado por busqueda en profundidad es: ", search.depth_first_graph_search(ab).path()

print "\n 2) Busqueda en el Trayecto NT:"
print "El resultado por Ramificacion y Acotacion es: ",  search.ram_acot_graph_search(nt).path()
print "El resultado por Ramificacion y Acotacion con Subestimacion es: ", search.ram_acot_subest_graph_search(nt).path()
print "El resultado por busqueda en anchura es: ", search.breadth_first_graph_search(nt).path()
print "El resultado por busqueda en profundidad es: ", search.depth_first_graph_search(nt).path()

print "\n 3) Busqueda en el Trayecto AN:"
print "El resultado por Ramificacion y Acotacion es: ",  search.ram_acot_graph_search(an).path()
print "El resultado por Ramificacion y Acotacion con Subestimacion es: ", search.ram_acot_subest_graph_search(an).path()
print "El resultado por busqueda en anchura es: ", search.breadth_first_graph_search(an).path()
print "El resultado por busqueda en profundidad es: ", search.depth_first_graph_search(an).path()

print "\n 4) Busqueda en el Trayecto EO:"
print "El resultado por Ramificacion y Acotacion es: ",  search.ram_acot_graph_search(eo).path()
print "El resultado por Ramificacion y Acotacion con Subestimacion es: ", search.ram_acot_subest_graph_search(eo).path()
print "El resultado por busqueda en anchura es: ", search.breadth_first_graph_search(eo).path()
print "El resultado por busqueda en profundidad es: ", search.depth_first_graph_search(eo).path()

print "\n 4) Busqueda en el Trayecto AZ:"
print "El resultado por Ramificacion y Acotacion es: ",  search.ram_acot_graph_search(az).path()
print "El resultado por Ramificacion y Acotacion con Subestimacion es: ", search.ram_acot_subest_graph_search(az).path()
print "El resultado por busqueda en anchura es: ", search.breadth_first_graph_search(az).path()
print "El resultado por busqueda en profundidad es: ", search.depth_first_graph_search(az).path()

#print "El resultado por busqueda en profundidad iterativa es: ", search.iterative_deepening_search(ab).path()
#print "El resultado por busqueda en profundidad limitada es: "search.depth_limited_search(ab).path()
#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
