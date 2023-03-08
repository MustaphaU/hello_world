#Steps
#import the necessary libraries
import pandas as pd
import numpy as np
#Step 1: read the node and edge files
import os
print(os.getcwd())
node_df = pd.read_csv("C:/Users/musta/OneDrive/Desktop/VD3_node/public/jean-complete-node.csv")
edge_df = pd.read_csv("C:/Users/musta/OneDrive/Desktop/VD3_node/public/jean-complete-edge.csv")

#Step 2:rename the columns names to lower case
node_df = node_df.rename(columns={'Id': 'id', 'Label': 'label', 'Description': 'description'})
edge_df = edge_df.rename(columns={'Source': 'source', 'Target': 'target', 'Type': 'type', 'Id': 'id', 'Label': 'label'})

node_df['id']=node_df['id'].replace(np.nan, 'NA')
edge_df['target']=edge_df['target'].replace(np.nan, 'NA')

#Step 3: replace the source and target nodes with their indices
id_dic = {}
for i in node_df['id']:
   id_dic[i] = node_df.index[node_df['id'] == i].tolist()[0] #dictionary of node and index
new_edge_df=edge_df.copy()
for i in new_edge_df['source']:
    new_edge_df['source']=new_edge_df['source'].replace(i, id_dic[i])
for k in new_edge_df['target']:
    new_edge_df['target']=new_edge_df['target'].replace(k, id_dic[k])
#rename the 'id' column of node_df to 'name'
node_df.rename(columns={'id':'name'}, inplace=True)

#step 4: use a community detection algorithm ton find the communities of the nodes
#pip install networkx in the terminal
import networkx as nx
import community

# Load the nodes and edges data 
nodes = node_df.copy()
edges = edge_df.copy()

# Create a networkx graph object from the edges DataFrame
G = nx.from_pandas_edgelist(edges, source='source', target='target')

# Use the Louvain method to detect communities in the graph
partition = community.best_partition(G)

# Print the number of communities and the number of nodes in each community
num_communities = len(set(partition.values()))
print(f'Number of communities: {num_communities}')
for i in range(num_communities):
    num_nodes = len([n for n in partition.keys() if partition[n] == i])
    print(f'Community {i}: {num_nodes} nodes')

# Initialize a new column called 'community' in node_df with default value of 0
node_df['community'] = 0
for i in range(node_df.shape[0]):
    node_df['community'][i] = partition[node_df['name'][i]]
    

node_df.rename(columns={'community': 'group'}, inplace=True)
#node_df.rename(columns={'name':'id'}, inplace=True)
#node_df.to_csv('node_final.csv')

#replace id column in node_df by the row number
node_df_final_df = node_df.copy()
node_df_final_df['name'] = node_df_final_df.reset_index().index
node_df_final_df.rename(columns={'name':'id'}, inplace=True)

#combine nodes and edges to a JSON
combined_data = {'nodes': node_df_final_df.to_dict('records'), 'links': new_edge_df.to_dict('records')}

#Write the combined_data dictionary to a JSON file named 'combined_data.json'.
import json
with open('combined_data_new_finall.json', 'w') as f:
    json.dump(combined_data, f)