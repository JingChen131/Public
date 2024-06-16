import os
libs = {"numpy","matolotlib","pillow","sklearn","requess",\
        "jieba","beautifulsoup4","wheel","networkx","sympy",\
        "pandas","pyopengl","pypdf2","docopt"}
try:
    for lib in libs:
        os.system("pip install"+ lib)
    print("Successful")
except:
    print("Failed Somehow")    