
def monaa_handler(file_content, regex: str):
    #file_content will be:
    # A    1
    # B    8
    # A    15
    # B    20
    # A    23
    # B    27
    # A    30
    # B    34
    # A    40
    
    
    #call mona with input however that may be done

    #return monaa result
    return """
        0.300000       <= t <   0.500000
        0.700000        < t' <   1.500000
        0.200000        < t' - t <   1.000000
        =============================
        0.300000       <= t <   0.500000
        0.700000        < t' <   1.500000
        0.200000        < t' - t <   1.000000
        =============================
    """