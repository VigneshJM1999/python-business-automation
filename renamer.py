import os

def main():
    folder_path = "test_files"

    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    print(f"Renaming files in: {folder_path}...")

    for count, filename in enumerate(os.listdir(folder_path), 1):
        file_extension = os.path.splitext(filename)[1]
        new_name = f"Report_{count}{file_extension}"

        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)

        os.rename(old_file, new_file)
        print(f"Renamed: {filename} -> {new_name}")

    print("All files renamed successfully.")

if __name__ == "__main__":
    main()