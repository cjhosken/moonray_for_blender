
RFB_FLOAT3 = ['color', 'point', 'vector', 'normal']

def is_socket_same_type(socket1, socket2):
    '''Compare two NodeSockets to see if they are of the same type. Types that
    are float3 like are considered the same.
    Arguments:
        socket1 (bpy.types.NodeSocket) - first socket to compare
        socket2 (bpy.types.NodeSocket) - second socket to compare
    Returns:
        (bool) - return True if both sockets are the same type
    '''

    return (type(socket1) == type(socket2)) or (is_socket_float_type(socket1) and is_socket_float_type(socket2)) or \
        (is_socket_float3_type(socket1) and is_socket_float3_type(socket2))

def is_socket_float_type(socket):
    '''Check if socket is of float type
    Arguments:
        socket (bpy.types.NodeSocket) - socket to check
    Returns:
        (bool) - return True if socket are float type
    '''    
    renderman_type = getattr(socket, 'renderman_type', None)

    if renderman_type:
        return renderman_type in ['int', 'float']

    else:
        return socket.type in ['INT', 'VALUE']

def is_socket_float3_type(socket):
    '''Check if socket is of float3 type
    Arguments:
        socket (bpy.types.NodeSocket) - socket to check
    Returns:
        (bool) - return True if socket is float3 type
    '''  

    renderman_type = getattr(socket, 'renderman_type', None)

    if renderman_type:
        return renderman_type in RFB_FLOAT3
    else:
        return socket.type in ['RGBA', 'VECTOR'] 