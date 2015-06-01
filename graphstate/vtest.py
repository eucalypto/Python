#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import graph_state
sys.path.append('~/Documents/mycode/')
import graph_state_property


# from /rg-graph/packages/GraphState/graph_state/property_lib.py (l.215):
# COLORS_AND_FIELDS_CONFIG = \
#     graph_state.PropertiesConfig.create(graph_state_property.PropertyKey(name="colors",
#                                                                          is_directed=False,
#                                                                          externalizer=Rainbow.Externalizer()),
#                                         graph_state_property.PropertyKey(name="fields",
#                                                                          is_directed=True,
#                                                                          externalizer=Fields.Externalizer()))




COLORS_CONFIG = graph_state.PropertiesConfig.create(graph_state_property.PropertyKey(name="colors", is_directed=False, externalizer=Rainbow.Externalizer()))

# from /rg-graph/packages/GraphState/graph_state/graph_state_test.py (l. 13):
# new_edge = property_lib.COLORS_AND_FIELDS_CONFIG.new_edge

# from /rg-graph/packages/GraphState/graph_state/graph_state_test.py (l. 89):
# edge = new_edge((0, 1),
#                 external_node=1,
#                 fields=property_lib.Fields('ab'),
#                 colors=property_lib.Rainbow((0,)),
#                 edge_id=333)


new_edge = property_lib.COLORS_CONFIG.new_edge

edges = [new_edge((-1, 1)),
         new_edge((1, 3)),
         new_edge((1, 3)),
         new_edge((3, -1))]

state = graph_state.GraphState(edges)

print state
