import hou

def add_bound_to_copy_chain(obj_node):
    # Iterate over all nodes inside the obj_node
    for node in obj_node.allSubChildren():
        if node.type().name() == 'copytopoints::2.0':
            # Check if the first input is connected to a node
            first_input = node.input(0)
            if first_input:
                # Get the node connected to the first input
                connected_node = first_input.inputs()[0]
                # Check if the connected node is not a bound SOP
                if connected_node and connected_node.type().name() != 'bound':
                    # Create a Bound SOP
                    bound_node = obj_node.createNode('bound')
                    # Connect it to the connected node
                    bound_node.setInput(0, connected_node)
                    # Connect the Bound SOP to the first input of the Copy SOP
                    node.setInput(0, bound_node)
                    print(f"Connected Bound to {node.path()} and linked to {connected_node.path()}")

# Get the selected nodes
selected_nodes = hou.selectedNodes()

# Iterate over selected nodes
for selected_node in selected_nodes:
    add_bound_to_copy_chain(selected_node)
