# 20170709
# Flora Tsai

import graphviz as gv

filename = 'Our destinations'


g = gv.Digraph(name=filename, filename=filename + '.gv')
g.attr(label=filename, rankdir='LR')

# cluster name should be named in the format cluster_*
cluster_source = gv.Digraph(name='cluster_source')
cluster_source.attr(label='Current Location')
cluster_source.node('source_tag1', 'Home')
cluster_source.node('source_tag2', 'CVS')

cluster_dest = gv.Digraph(name='cluster_dest')
cluster_dest.attr(label='Destination')

cluster_dest.node('dest_tag1', 'School')
cluster_dest.node('dest_tag2', 'Home')

# Add clusters as subgraphs of g
g.subgraph(cluster_source)
g.subgraph(cluster_dest)

# Make edges
g.edge('source_tag1', 'dest_tag1', label='On foot')
g.edge('source_tag2', 'dest_tag2', label='By car')

# View the graph, pdf file by default
g.view()

# Print in Dot format
print(g.source)

