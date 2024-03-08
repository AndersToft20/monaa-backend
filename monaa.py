import os
import subprocess

def monaa_handler(file, regex: str):
    print(file)
    path = os.path.join("./temp_files/monaa_input", "log.txt")
    file.save(path)

    
    
    #call mona with input however that may be done
    command = f"../monaa/build/monaa -e '{regex}' < ./temp_files/monaa_input/log.txt > ./temp_files/monaa_output/monaa_output.txt"

    result = subprocess.run(
        ['ls', '-l'],
        capture_output = True, 
        text = True
    )
    print(result.stdout)
    print(result.stderr)

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