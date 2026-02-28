from streamlit_agraph import agraph, Node, Edge, Config

def render_interactive_graph(classes, relationships):
    nodes = []
    edges = []
    
    # Clean Box Nodes
    for cls in classes:
        nodes.append(Node(
            id=cls, 
            label=cls, 
            size=25, 
            shape="box", 
            borderWidth=2,
            color={"background": "#1F2937", "border": "#00E5FF"}, 
            font={"color": "white", "size": 16}
        ))
        
    # Ultra-Crisp, Readable Edge Text
    for source, rel_type, target in relationships:
        edge_color = "#10B981" if rel_type == "Inheritance" else "#3B82F6" if rel_type == "Aggregation" else "#F59E0B"
        
        edges.append(Edge(
            source=source, 
            target=target, 
            label=rel_type, 
            color=edge_color,
            width=2, 
            font={
                "color": "#FAF7F7",      # Pure white text
                "size": 12, 
                "align": "top",          # MAGIC FIX: Puts the text completely ABOVE the line
                "strokeWidth": 0,        # Strips out any ugly bold outlines
                "background": "#1F2937"  # Gives the text a nice dark background pill to pop against
            }
        ))
        
    # Graph config with Zoom Enabled
    config = Config(
        width="100%",
        height=600,
        directed=True, 
        physics=False, 
        interaction={
            "zoomView": True,  
            "dragView": True,   
            "dragNodes": True   
        },
        hierarchical={
            "enabled": True, 
            "direction": "UD", 
            "sortMethod": "directed"
        }
    )
    
    return agraph(nodes=nodes, edges=edges, config=config)