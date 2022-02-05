import multiprocessing as mp #Kjøyr ale i parallelt
import tqdm.autonotebook as tqdm #Enkel progress bar
import pathlib #Filstier
import subprocess #CMD-calls fra python

def get_files(root):
    
    if isinstance(root, str):
        root = pathlib.Path(root)
    
    #Get absolute path of path
    root = root.resolve()

    files = []
    ignore=['__init__.py']
    for item in root.glob('**/*'):
        if item.is_file() & (item.suffix=='.py') & (not item.name in ignore):
            files.append(item)
    return files

def call_file(file):
    cwd=file.parent
    cmd='python '+ file.name
    subprocess.call(cmd, shell=True, cwd=cwd)
    return

def rerun(root, parallel=True, progress=True):
    files=get_files(root)
    if parallel:
        pool = mp.Pool(mp.cpu_count())
        if progress:
            for _ in tqdm.tqdm(pool.imap_unordered(call_file, files), desc='Calling scripts', total=len(files)):
                continue
        else:
            pool.map_async(call_file, files).get()
        pool.close()    
        pool.join()

    else:
        if progress:
            files = tqdm.tqdm(files, desc='Calling scripts')
        for file in files:
            call_file(file)
    return


if __name__ == '__main__':
    pass