import os

def clean_repository():
    # Files and extensions to remove
    to_delete = ["'", "0", ".ai_test.py.swp", ".viminfo"]
    
    print("🧹 Cleaning up stray and temporary files...")
    for item in to_delete:
        if os.path.exists(item):
            os.remove(item)
            print(f"Removed: {item}")
            
    # Clean up any other .swp files in directories
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".swp") or file == ".viminfo":
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Removed temp file: {file_path}")

def update_gitignore():
    gitignore_content = """
# Editor temporary and swap files
*.swp
*.swo
.viminfo
.DS_Store

# Stray artifacts
'
0
"""
    print("📝 Updating .gitignore...")
    with open(".gitignore", "a") as f:
        f.write(gitignore_content)
    print(".gitignore updated successfully.")

def create_readme():
    readme_content = """# Arma Game Project (AGP)

Welcome to the official repository for the Arma Game Project—an open-source tactical 3D mobile game environment built collaboratively.

## 📁 Repository Structure
* `/scripts` - Core game logic and system automation scripts.
* `/bin` - Executables and build outputs.
* `/pkg` - Packages and external dependencies.
* `game_engine.py` - Core engine handling initialization and loops.
* `onboard.py` - Onboarding and setup utilities.

## 🚀 Getting Started for Developers
1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YourUsername/Arma-Game-Project.git](https://github.com/YourUsername/Arma-Game-Project.git)
