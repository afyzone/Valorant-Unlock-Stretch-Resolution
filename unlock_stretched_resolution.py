import os, requests, shutil, tempfile

GITHUB_RAW_URL = "https://raw.githubusercontent.com/afyzone/Valorant-Unlock-Stretched-Resolution/refs/heads/main/Resources/GameUserSettings.ini"
FILENAME = "GameUserSettings.ini"
BASE_DIR = os.path.expandvars(r"%localappdata%\VALORANT\Saved\Config")

def download_file(url, save_path):
    print(f"Downloading {url}")

    response = requests.get(url)
    response.raise_for_status()

    with open(save_path, "wb") as f:
        f.write(response.content)

    print(f"Downloaded to {save_path}")

def copy_to_dirs(base_dir, file_path):
    for root, dirs, files in os.walk(base_dir):
        if not dirs:
            dest_path = os.path.join(root, os.path.basename(file_path))
            shutil.copy2(file_path, dest_path)
            print(f"Copied to {dest_path}")

def main():
    os.makedirs(BASE_DIR, exist_ok=True)

    temp_file = os.path.join(tempfile.gettempdir(), FILENAME)

    download_file(GITHUB_RAW_URL, temp_file)
    copy_to_dirs(BASE_DIR, temp_file)
    os.remove(temp_file)

if __name__ == "__main__":
    main()
