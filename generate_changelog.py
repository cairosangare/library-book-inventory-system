
import difflib
from datetime import datetime

# Load the baseline JSON file as raw text
with open('library-book-inventory-system_-dfe81792-ba58-40ee--export-1749131420576.json', 'r', errors='ignore') as file:
    baseline_text = file.read()

# Load the new JSON file as raw text
with open('tooljet_exports/new_tooljet_export.json', 'r', errors='ignore') as file:
    new_text = file.read()

# Function to generate a summary of differences
def generate_diff_summary(baseline, new):
    diff = difflib.unified_diff(
        baseline.splitlines(),
        new.splitlines(),
        fromfile='baseline',
        tofile='new',
        lineterm=''
    )
    return '\n'.join(diff)

# Generate the diff summary
diff_summary = generate_diff_summary(baseline_text, new_text)

# Prepare the changelog entry
changelog_entry = f"## {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
changelog_entry += "### Changes:\n\n"
changelog_entry += f"{diff_summary}\n"

# Append the changelog entry to CHANGELOG.md
with open('CHANGELOG.md', 'a') as changelog_file:
    changelog_file.write(changelog_entry)

print("Changelog updated successfully.")
