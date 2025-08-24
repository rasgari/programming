import os

# مسیر پوشه‌ها
old_folder = "old"
new_folder = "new"

# تابع برای خواندن همه URLها از یک پوشه
def read_urls_from_folder(folder):
    urls = set()
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                for line in f:
                    url = line.strip()
                    if url:
                        urls.add(url)
    return urls

# خواندن URLهای قدیمی و جدید
old_urls = read_urls_from_folder(old_folder)
new_urls = read_urls_from_folder(new_folder)

# تفکیک
newly_added = new_urls - old_urls
removed = old_urls - new_urls
common = old_urls & new_urls

# ذخیره در فایل‌ها
with open("new_urls.txt", "w", encoding="utf-8") as f:
    for url in sorted(newly_added):
        f.write(url + "\n")

with open("removed_urls.txt", "w", encoding="utf-8") as f:
    for url in sorted(removed):
        f.write(url + "\n")

with open("common_urls.txt", "w", encoding="utf-8") as f:
    for url in sorted(common):
        f.write(url + "\n")

print("✅ مقایسه انجام شد! نتیجه در فایل‌های new_urls.txt, removed_urls.txt, common_urls.txt ذخیره شد.")
