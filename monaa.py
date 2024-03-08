import os

def monaa_handler(file, regex: str):
    path = os.path.join("./temp_files/monaa_input", "log.txt")
    file.save(path)

    #call mona with input however that may be done
    command = f"../monaa/build/monaa -e '{regex}' < ./temp_files/monaa_input/log.txt > ./temp_files/monaa_output/monaa_output.txt"
    os.system(command)


    with open("./temp_files/monaa_output/monaa_output.txt", "r") as f:
        data = f.read()
        return data

