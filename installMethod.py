def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
