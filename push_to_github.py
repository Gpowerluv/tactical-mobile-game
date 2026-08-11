import subprocess
print("Forcing push to github.com...")
try:
    subprocess.run(["lg2", "push", "--force"], check=True)
except Exception as e:
    print(f"Push error: {e}")
