#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import graph_state
from graph_state import graph_state_property
from graph_state import property_lib



# from /rg-graph/packages/GraphState/graph_state/property_lib.py (l.215):
# COLORS_AND_FIELDS_CONFIG = \
#     graph_state.PropertiesConfig.create(graph_state_property.PropertyKey(name="colors",
#                                                                          is_directed=False,
#                                                                          externalizer=Rainbow.Externalizer()),
#                                         graph_state_property.PropertyKey(name="fields",
#                                                                          is_directed=True,
#                                                                          externalizer=Fields.Externalizer()))




COLORS_CONFIG = graph_state.PropertiesConfig.create(
    graph_state_property.PropertyKey(
        name="Gandalf",
        is_directed=False,
        externalizer=property_lib.Rainbow.Externalizer()))

# from /rg-graph/packages/GraphState/graph_state/graph_state_test.py (l. 13):
# new_edge = property_lib.COLORS_AND_FIELDS_CONFIG.new_edge

# from /rg-graph/packages/GraphState/graph_state/graph_state_test.py (l. 89):
# edge = new_edge((0, 1),
#                 external_node=1,
#                 fields=property_lib.Fields('ab'),
#                 colors=property_lib.Rainbow((0,)),
#                 edge_id=333)


new_edge = COLORS_CONFIG.new_edge

edges = [new_edge((-1, 1), Gandalf=property_lib.Rainbow((1,))),
         new_edge((1, 3), Gandalf=property_lib.Rainbow((0,))),
         new_edge((1, 2), Gandalf=property_lib.Rainbow((0,))),
         new_edge((2, 3), Gandalf=property_lib.Rainbow((0,))),
         new_edge((2, -1), Gandalf=property_lib.Rainbow((1,))),
         new_edge((3, -1), Gandalf=property_lib.Rainbow((1,)))]


state = graph_state.PropertiesConfig.new_graph_state(edges)

print state

print state.edges

# the following command takes the graph-state object "state", searches
# for the first edge "edges[0]" and prints the first entry in
# "Gandalf" (since Gandalf is a tuple (x, x)) and here we use only the
# first entry
# print state.edges[0].Gandalf[0]

print state.edges[0].Gandalf


print "Nodes?"
externalcount = 0
external_dot_string = "{node [shape=plaintext] "
for edge in state.edges:
    if edge.is_external():
        string = "E" + str(externalcount)
        string += " -- "
        string += str(edge.internal_node) + ";"
        print string
        external_dot_string += " E" + str(externalcount)
        externalcount += 1
    else:
        string = str(edge.nodes[0]) + " -- " + str(edge.nodes[1]) + ";"
        print string

external_dot_string += "}"
print external_dot_string


print "now all the isomorphies:"
print state.sortings
