
<!DOCTYPE html>
<html>
<body>
	<ol>
		<li>Once the csv files containing the node and links (or edges) data were loaded, the columns names were renamed to their respective lower cases.</li>
		<li>The character “NA” representing Naveet was erroneously treated as a missing value by pandas, this was reversed by replacing it with “NA” both in the node and edges dataframes.</li>
		<li>The source and target nodes were replaced with their indices.</li>
		<li>The nodes were grouped using a community detection algorithm: Louvain method. First Networkx function is used to create a Graph object from the edges data, which represents the network. The Graph object is used as input for the community detection algorithm. Make sure to install networkx in the terminal before running the python file (preprocessing.py). Seven(7) groups or communities were obtained </li>
		<li>A community column was inserted in the  nodes data and renamed to "group" (which will later determine the color coding of the nodes).</li>
		<li>The final edges and nodes data were exported to json named combined_data_new_finall.json and could be found in the public directory.</li>
		<li>The node js application that starts the server is located in the root project directory VD3_node</li>
	</ol>
    <h2>How to run the application</h2>
<ol>
	<li>Navigate the project directory “VD3_node”</li>
	<li>Type and run the command “npm start”. This will start the server.</li>
	<li>Open a browser tab, type “localhost:3000” and hit enter.</li>
	<li>The node link diagram will be the first view. You should be able to toggle between the node link and adjacency matrix.</li>
</ol>

<h2>Interactions and animated transition between the node-link and adjacency matrix</h2>

<p>The visualizations are of two kinds: the node-link diagram and the adjacency matrix. The default visualization that is displayed is the node link diagram. These are the interactions that are possible with the node-link diagram prior to starting the animated transition:</p>

<ul>
	<li>Hovering over a node increases the node size and highlights the links directly, attached to the node. It also displays the character name and a description of the character.</li>
	<li>You can also click on a node to drag it to a new position. Dragging a node close to another node repels the node causing the entire diagram to move. Essentially, the common interactions that are possible with most force directed graphs.</li>
	<li>Once the toggle button is clicked, the interactions with the node-link diagram will be limited to hovering over the node. Hovering over the node will only display the character name and description of the character.</li>
	<li>Why is that? The node clones allow only one mouse over interaction and are not intricately linked to the edges. Hence, in the animation phase (during which the clones are made) once these clones overlap the original nodes, the other actions such as link highlighting, dragging, repulsion are overridden.</li>
</ul>

<p>The adjacency matrix: The cells of the adjacency matrix represent the links. Only cells formed by nodes or characters that actually co-occurred (or were connected in the node link diagram) are colored. Hovering over any of the colored cells highlights the cell and the corresponding nodes. You can also reorder the cells based on label (alphabetically), the cluster (community), or the count (the number of cooccurrence)</p>

<p>You can repeatedly toggle between the node link and the adjacency matrix. However, if you decide to change the ordering of the nodes of the adjacency matrix during a matrix view, ensure the reordering is complete before toggling to the node view. Otherwise, reordering is paused is not complete and character names (row and column names) may overlap each other on your next view. You can always remove the overlap by selecting an reordering and allowing it to complete.  
</p>

</body>
</html>
