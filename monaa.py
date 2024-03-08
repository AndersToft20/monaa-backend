import os

def monaa_handler(file, regex: str):
    print(file)
    path = os.path.join("temp_files", "log.txt")
    file.save(path)

    
    
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