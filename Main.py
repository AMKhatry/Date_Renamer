import os
from datetime import datetime

filepath = input("Enter the folder path: ").strip()

date_formats = ["%d %b %Y", "%d %B %Y"]  # "1 Jan 2025" and "2 April 2025"

for filename in os.listdir(filepath):
    full_path = os.path.join(filepath, filename)
    if os.path.isfile(full_path) and filename.lower().endswith('.pdf'):
        name_without_ext = os.path.splitext(filename)[0]
        ext = os.path.splitext(filename)[1]

        for date_format in date_formats:
            try:
                date_obj = datetime.strptime(name_without_ext, date_format)
                formatted_date = date_obj.strftime("%Y%m%d")
                new_filename = f"{formatted_date} - {name_without_ext}{ext}"
                new_full_path = os.path.join(filepath, new_filename)
                os.rename(full_path, new_full_path)
                print(f"Renamed: {filename} → {new_filename}")
                break  # success, don't try other formats
            except ValueError:
                continue
        else:
            print(f"Skipped: {filename} (invalid date format)")
