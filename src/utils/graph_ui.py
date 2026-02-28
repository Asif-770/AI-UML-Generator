from streamlit_agraph import agraph, Node, Edge, Config

def render_interactive_graph(classes, relationships):
    nodes = []
    edges = []
    
    # Restored high-tech node colors
    for cls in classes:
        nodes.append(Node(
            id=cls, 
            label=cls, 
            size=25, 
            shape="box", 
            borderWidth=2,
            color={"background": "#1F2937", "border": "#00E5FF"}, # Modern dark bg with Cyan border
            font={"color": "white", "size": 16, "face": "sans-serif"}
        ))
        
    # Restored relationship colors
    for source, rel_type, target in relationships:
        edge_color = "#00FF00" if rel_type == "Inheritance" else "#00E5FF"
        edges.append(Edge(
            source=source, 
            target=target, 
            label=rel_type, 
            color=edge_color,
            width=2,
            font={"color": "#E5E7EB", "size": 12, "align": "middle", "vadjust": -10}
        ))
        
    # STABILIZED CONFIGURATION
    config = Config(
        width="100%",
        height=500,
        directed=True, 
        physics=False, # Stops bouncy physics
        interaction={
            "zoomView": False,  # STOPS the graph from zooming out/disappearing on click
            "dragView": True,   # Allows you to pan the camera safely
            "dragNodes": True   # Allows you to move boxes around safely
        },
        hierarchical={
            "enabled": True, 
            "direction": "UD", 
            "sortMethod": "directed"
        }
    )
    
    return agraph(nodes=nodes, edges=edges, config=config)