# algorithm to calculate disk usage
import os

import os

def cumulative_disk_space(entry_path):
    # Base case: if the entry is a file, return its size
    if os.path.isfile(entry_path):
        return os.path.getsize(entry_path)
    
    # If the entry is a directory, recursively compute the cumulative size of its contents
    elif os.path.isdir(entry_path):
        total_size = 0
        entries = os.listdir(entry_path)
        
        for entry in entries:
            # Recursively calculate the size of each nested entry
            nested_path = os.path.join(entry_path, entry)
            total_size += cumulative_disk_space(nested_path)
        
        return total_size

# Example usage:
entry_path = r"C:\Users\ADMIN\Videos\Tyler.Perrys.The.Oval.S02.COMPLETE.720p.AMZN.WEBRip.x264-GalaxyTV[TGx]"
total_disk_space = cumulative_disk_space(entry_path)
print(f"Cumulative Disk Space Usage at {entry_path}: {total_disk_space} bytes")
