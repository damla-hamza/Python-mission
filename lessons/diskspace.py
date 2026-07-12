disk_space = 500  # GB

print(f"Initial free space: {disk_space} GB")

# New logs consume 45 GB
disk_space -= 45

print(f"After logs: {disk_space} GB")

# Cleanup frees 20 GB
disk_space += 20

print(f"After cleanup: {disk_space} GB")