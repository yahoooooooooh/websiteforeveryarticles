import os
import re
import unicodedata

def generate_safe_filename(original_full_filename):
    """
    Converts a filename to a more URL-friendly (ASCII-like) version.
    Example: "《你好 World》“测试”.md" -> "ni-hao-world-ce-shi.md" (actual output may vary)
    """
    name_part, ext = os.path.splitext(original_full_filename)

    # 1. Normalize Unicode to its closest ASCII representation (best effort)
    # NFKD decomposes characters, encode to ASCII ignoring errors, then decode.
    safe_name = unicodedata.normalize('NFKD', name_part).encode('ascii', 'ignore').decode('ascii')

    # 2. Convert to lowercase
    safe_name = safe_name.lower()

    # 3. Replace any character that is not a letter (a-z), number (0-9), 
    #    or hyphen (-) with a hyphen.
    #    This step makes it very URL-safe.
    safe_name = re.sub(r'[^a-z0-9-]+', '-', safe_name)

    # 4. Replace multiple consecutive hyphens with a single hyphen
    safe_name = re.sub(r'-+', '-', safe_name)

    # 5. Remove leading or trailing hyphens
    safe_name = safe_name.strip('-')

    # 6. If the name becomes empty after sanitization, use a default name.
    if not safe_name:
        safe_name = 'untitled'
    
    return safe_name + ext

def rename_markdown_files(base_articles_dir="articles"):
    """
    Renames .md files within the subdirectories of base_articles_dir
    to be more URL-friendly.
    """
    print(f"Starting file renaming process in directory: '{base_articles_dir}'")
    total_renamed_count = 0
    
    if not os.path.isdir(base_articles_dir):
        print(f"Error: Base articles directory '{base_articles_dir}' not found.")
        return

    for theme_name in os.listdir(base_articles_dir):
        theme_path = os.path.join(base_articles_dir, theme_name)
        
        if os.path.isdir(theme_path):
            print(f"\nProcessing theme directory: '{theme_name}'")
            files_in_theme = 0
            renamed_in_theme = 0
            for filename in os.listdir(theme_path):
                if filename.lower().endswith(".md"):
                    files_in_theme += 1
                    original_filepath = os.path.join(theme_path, filename)
                    
                    new_safe_filename = generate_safe_filename(filename)

                    # Only proceed if the new name is actually different
                    if new_safe_filename.lower() != filename.lower():
                        actual_new_filename_to_use = new_safe_filename
                        prospective_new_filepath = os.path.join(theme_path, actual_new_filename_to_use)
                        
                        # Handle potential filename collisions for the new name
                        collision_counter = 1
                        while os.path.exists(prospective_new_filepath) and \
                              prospective_new_filepath.lower() != original_filepath.lower():
                            name_base, name_ext = os.path.splitext(new_safe_filename)
                            actual_new_filename_to_use = f"{name_base}_{collision_counter}{name_ext}"
                            prospective_new_filepath = os.path.join(theme_path, actual_new_filename_to_use)
                            collision_counter += 1
                        
                        # Final check if the name to use (after collision handling) is still different
                        if actual_new_filename_to_use.lower() != filename.lower():
                            try:
                                os.rename(original_filepath, prospective_new_filepath)
                                print(f"  SUCCESS: Renamed '{filename}' -> '{actual_new_filename_to_use}'")
                                renamed_in_theme += 1
                                total_renamed_count +=1
                            except OSError as e:
                                print(f"  ERROR: Could not rename '{filename}' to '{actual_new_filename_to_use}'. Reason: {e}")
                        else:
                            print(f"  SKIPPED: Proposed new name for '{filename}' resolved to original after collision check.")
                    else:
                        print(f"  SKIPPED: Name '{filename}' is already URL-friendly or generated safe name is identical.")
            
            if files_in_theme == 0:
                print(f"  No .md files found in '{theme_name}'.")
            elif renamed_in_theme == 0 and files_in_theme > 0:
                print(f"  No files needed renaming in '{theme_name}'.")

    if total_renamed_count > 0:
        print(f"\nFinished renaming. Total files renamed: {total_renamed_count}.")
    else:
        print("\nNo files were renamed across all themes.")
    
    print("\nIMPORTANT: Remember to re-run 'python generate_navigation.py' to update your navigation data.")
    print("After that, commit and push the changes (renamed files and updated navigation.json) to GitHub.")

if __name__ == "__main__":
    print("--------------------------------------------------------------------")
    print("WARNING: Markdown File Renamer")
    print("--------------------------------------------------------------------")
    print("This script will attempt to rename .md files in the 'articles'")
    print("directory and its subdirectories to make their names more URL-friendly.")
    print("This operation directly modifies your files.")
    print("\n>>> IT IS STRONGLY RECOMMENDED TO BACK UP YOUR 'articles' DIRECTORY")
    print(">>> BEFORE PROCEEDING! <<<\n")

    # confirm = input("Are you sure you want to proceed with renaming? (yes/no): ")
    # if confirm.lower() == 'yes':
    #     rename_markdown_files()
    # else:
    #     print("Operation cancelled by the user.")

    # For non-interactive execution in this environment,
    # I will call the function directly.
    # WHEN YOU RUN THIS LOCALLY, CONSIDER UNCOMMENTING THE CONFIRMATION ABOVE.
    rename_markdown_files()