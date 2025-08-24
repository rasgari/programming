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

# ذخیره در فایل خروجی
with open("result_urls.txt", "w", encoding="utf-8") as out:
    out.write("🔹 URL های جدید:\n")
    for url in sorted(newly_added):
        out.write(url + "\n")
    
    out.write("\n🔹 URL های حذف‌شده:\n")
    for url in sorted(removed):
        out.write(url + "\n")
    
    out.write("\n🔹 URL های مشترک:\n")
    for url in sorted(common):
        out.write(url + "\n")

print("✅ مقایسه انجام شد! نتیجه در فایل result_urls.txt ذخیره شد.")
