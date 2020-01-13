import os, glob, parahumanos

d = {os.path.splitext(f)[0] : parahumanos.tamanyo_aproximado(os.stat(f).st_size) \
    for f in glob.glob('*') if os.stat(f).st_size > 500 }
print(d)