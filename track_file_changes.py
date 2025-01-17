import subprocess

def get_git_changes():
    # Get the list of added, modified, and deleted files
    added_files = subprocess.check_output(["git", "diff", "--name-only", "--diff-filter=A"]).decode().splitlines()
    modified_files = subprocess.check_output(["git", "diff", "--name-only", "--diff-filter=M"]).decode().splitlines()
    deleted_files = subprocess.check_output(["git", "diff", "--name-only", "--diff-filter=D"]).decode().splitlines()

    return added_files, modified_files, deleted_files

def main():
    added, modified, deleted = get_git_changes()

    print("Added files:")
    for file in added:
        print(f"  + {file}")

    print("\nModified files:")
    for file in modified:
        print(f"  ~ {file}")

    print("\nDeleted files:")
    for file in deleted:
        print(f"  - {file}")

if __name__ == "__main__":
    main()
