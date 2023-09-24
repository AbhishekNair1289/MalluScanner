import os
import hashlib
from termcolor import colored

# Define a list of supported file extensions
allowed_extensions = [
    ".txt", ".pdf", ".doc", ".docx", ".jpg", ".png", ".mp3", ".mp4", ".zip", ".rar",
    ".xlsx", ".pptx", ".csv", ".html", ".css", ".js", ".json", ".xml", ".log", ".java", ".py",
    ".php", ".cpp", ".h", ".c", ".rb", ".pl", ".sh", ".bat", ".exe", ".dll", ".msi",
    ".conf", ".yaml", ".toml", ".ini", ".cfg", ".xml", ".yml", ".csv", ".json", ".ts", ".tsx",
    ".cpp", ".cs", ".c", ".coffee", ".sql", ".swift", ".vb", ".scala", ".r", ".lua", ".go", ".kotlin",
    ".perl", ".rust", ".dart", ".groovy", ".jsx", ".rkt", ".scm", ".bash", ".zsh", ".m", ".vbs",
    ".asm", ".class", ".jar", ".war", ".ear", ".so", ".lib", ".obj", ".pdb", ".a", ".out", ".elf",
    ".txt", ".rtf", ".ppt", ".odt", ".odp", ".ods", ".xls", ".epub", ".wma", ".ogg", ".wav", ".flac",
    ".avi", ".mkv", ".mov", ".wmv", ".flv", ".gif", ".bmp", ".tif", ".tiff", ".ico", ".svg", ".eps",
    ".psd", ".ai", ".indd", ".cdr", ".mpg", ".mpeg", ".m4a", ".aac", ".ac3", ".flv", ".m3u", ".pls",
    ".fla", ".swf", ".pdf", ".doc", ".xls", ".ppt", ".docx", ".xlsx", ".pptx", ".accdb", ".mdb",
    ".sql", ".db", ".bak", ".sqlite", ".dbf", ".dat", ".dbx", ".dbf", ".ini", ".json", ".xml", ".csv",
    ".3gp", ".asf", ".asx", ".avi", ".flv", ".m4v", ".mkv", ".mov", ".mp4", ".mpg", ".rm", ".srt", ".swf",
    ".vob", ".webm", ".wmv", ".wpl", ".jpg", ".jpeg", ".gif", ".bmp", ".png", ".tiff", ".svg", ".eps", ".ico",
    ".tga", ".ps", ".ai", ".eps", ".nef", ".crw", ".orf", ".raw", ".dng", ".arw", ".sr2", ".rw2", ".mrw", ".pef",
    ".pdf", ".djvu", ".epub", ".azw", ".mobi", ".pdb", ".cbr", ".cbz", ".xps", ".oxps", ".djv", ".fb2", ".lit", ".pdb",
    ".chm", ".hlp", ".txt", ".asc", ".nfo", ".md", ".markdown", ".html", ".htm", ".xml", ".css", ".js", ".php", ".pl", ".py",
    ".rb", ".java", ".c", ".cpp", ".h", ".cs", ".vb", ".go", ".swift", ".r", ".lua", ".perl", ".rust", ".dart", ".coffee", ".sql",
    ".ts", ".jsx", ".tsx", ".sh", ".bash", ".zsh", ".fish", ".cmd", ".ps1", ".psm1", ".bat", ".vbs", ".js", ".html", ".htm", ".css",
    ".scss", ".less", ".sass", ".json", ".xml", ".yml", ".yaml", ".toml", ".ini", ".cfg", ".conf", ".properties", ".ini", ".reg", ".inf",
    ".manifest", ".vhd", ".vhdx", ".vmdk", ".qcow", ".qcow2", ".iso", ".bin", ".img", ".vdi", ".nrg", ".mdf", ".mdb", ".db", ".dbf", ".sqlite", ".sql",
    ".bak", ".log", ".txt", ".csv", ".xml", ".json", ".yaml", ".tsv", ".lst", ".m3u", ".pls", ".wpl", ".kml", ".kmz", ".gpx", ".vtt", ".srt", ".sub", ".sami",
    ".sbv", ".ass", ".ssa", ".dxf", ".dwg", ".stp", ".igs", ".stl", ".obj", ".ply", ".fbx", ".dxf", ".dwg", ".stl", ".3ds", ".dae", ".u3d", ".ifc", ".x3d", ".collada",
    ".glb", ".gltf", ".fbx", ".blend", ".3dm", ".wrl", ".x3dv", ".csv", ".tsv", ".ps", ".eps", ".pdf", ".doc", ".docx", ".odt", ".rtf", ".txt", ".xml", ".json", ".yaml",
    ".html", ".htm", ".mht", ".mhtml", ".xhtml", ".xht", ".shtml", ".asp", ".aspx", ".php", ".jsp", ".htm", ".html", ".cgi", ".cfm", ".css", ".js", ".ts", ".tsx",
    ".c", ".cpp", ".h", ".cs", ".java", ".py", ".rb", ".pl", ".php", ".swift", ".go", ".r", ".lua", ".perl", ".rust", ".dart", ".coffee", ".sql", ".ts", ".jsx",
    ".tsx", ".sh", ".bash", ".zsh", ".fish", ".cmd", ".ps1", ".psm1", ".bat", ".vbs", ".js", ".ts", ".jsx", ".tsx", ".php", ".xml", ".json", ".yaml", ".yml", ".toml",
    ".ini", ".cfg", ".conf", ".properties", ".ini", ".reg", ".inf", ".manifest", ".ini", ".conf", ".yaml", ".toml", ".properties", ".desktop", ".cfg", ".config", ".prefs",
    ".xml", ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf", ".properties", ".ini", ".reg", ".inf", ".manifest", ".ini", ".conf", ".yaml", ".toml", ".properties", ".desktop",
    ".cfg", ".config", ".prefs", ".html", ".htm", ".mht", ".mhtml", ".xhtml", ".xht", ".shtml", ".asp", ".aspx", ".php", ".jsp", ".htm", ".html", ".cgi", ".cfm", ".css", ".js", ".ts", ".tsx",
    ".c", ".cpp", ".h", ".cs", ".java", ".py", ".rb", ".pl", ".php", ".swift", ".go", ".r", ".lua", ".perl", ".rust", ".dart", ".coffee", ".sql", ".ts", ".jsx", ".tsx", ".sh", ".bash",
    ".zsh", ".fish", ".cmd", ".ps1", ".psm1", ".bat", ".vbs", ".js", ".ts", ".jsx", ".tsx", ".php", ".xml", ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf", ".properties", ".ini",
    ".reg", ".inf", ".manifest", ".ini", ".conf", ".yaml", ".toml", ".properties", ".desktop", ".cfg", ".config", ".prefs", ".ini", ".reg", ".inf", ".manifest", ".ini", ".conf", ".yaml", ".toml",
    ".properties", ".desktop", ".cfg", ".config", ".prefs", ".dll", ".so", ".dylib", ".a", ".lib", ".obj", ".pdb", ".dll", ".so", ".dylib", ".a", ".lib", ".obj", ".pdb", ".res", ".def", ".exp", ".mod", 
    ".sym", ".dbg", ".map", ".diz", ".bin", ".dat", ".ini", ".reg", ".inf", ".manifest", ".config", ".prefs", ".log", ".tmp", ".bak", ".swp", ".swo", ".swn"
]

# Define a function to calculate the hash of a file
def calculate_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(65536), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except Exception as e:
        return None

# Define a function to scan a file
def scan_file(file_path):
    file_extension = os.path.splitext(file_path)[-1].lower()
    if file_extension not in allowed_extensions:
        return colored("Skipped (Unsupported file type)", "yellow")

    file_hash = calculate_file_hash(file_path)

    # You would typically compare the file_hash with a database of known malware hashes
    # For this basic example, let's assume a fake database of known malicious file hashes
    fake_malware_db = set(["fake_malware_hash1", "fake_malware_hash2"])
    
    if file_hash in fake_malware_db:
        return colored("Malware Detected", "red")
    
    return colored("No Threats Found", "green")

# Define a function to scan a directory
def scan_directory(directory_path):
    scanned_files = 0
    threats_found = 0

    print(colored("  |\    /|        | |         _____                      ", "blue"))
    print(colored("  | \  / |        | |        / ____|                     ", "blue"))
    print(colored("  |  \/  |  __ _  | |       | (___    ___  __ _  _ __    ", "blue"))
    print(colored("  |      | / _` | | || | | | \___ \  / _  / _` || '_ \   ", "blue"))
    print(colored("  |      || (_| | | || |_| | ____) || (_ | (_| || | | |  ", "blue"))
    print(colored("  |      | \__,_| | | \__,_||_____/  \___ \__,_||_| |_|  ", "blue"))
    print("\n")
        
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            result = scan_file(file_path)
            scanned_files += 1
            if result == colored("Malware Detected", "red"):
                threats_found += 1
            print(f"Scanning {file_path}: {result}")

    print("\nScan completed.")
    print(f"Scanned files: {scanned_files}")
    print(f"Threats found: {threats_found}")

# Main function to initiate the scan
if __name__ == "__main__":
    try:
        target_directory = input("Enter the directory to scan: ")
        if os.path.isdir(target_directory):
            scan_directory(target_directory)
        else:
            print(colored("Invalid directory path. Please provide a valid directory path.", "yellow"))
    except KeyboardInterrupt:
        print(colored("\nScan interrupted by the user.", "yellow"))
    except Exception as e:
        print(colored(f"An error occurred: {e}", "red"))
