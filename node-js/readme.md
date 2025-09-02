# Docker has specific installation instructions for each operating system.
# Please refer to the official documentation at https://docker.com/get-started/

# Pull the Node.js Docker image:
docker pull node:22-alpine

# Create a Node.js container and start a Shell session:
docker run -it --rm --entrypoint sh node:22-alpine

# Verify the Node.js version:
node -v # Should print "v22.19.0".

# Verify npm version:
npm -v # Should print "10.9.3".





چرا باید Node.js و React یاد بگیریم؟
🔹 Node.js

چی هست؟
یک محیط اجرایی (Runtime) برای جاوااسکریپت سمت سرور.

کاربرد اصلی:
ساخت API، بک‌اند برای اپلیکیشن‌های وب و موبایل، سیستم‌های real-time مثل چت و استریم.

مزایا:

سرعت بالا (استفاده از موتور V8 گوگل کروم).

جامعه کاربری بزرگ و پکیج‌های زیاد در NPM.

یک زبان (JavaScript) برای فرانت‌اند و بک‌اند.

مثال:
ساخت یک API ساده برای مدیریت کارها (Todo App).

🔹 React

چی هست؟
یک کتابخانه جاوااسکریپت برای ساخت رابط کاربری (UI).

کاربرد اصلی:
توسعه اپلیکیشن‌های وب SPA (Single Page Applications) و حتی موبایل با React Native.

مزایا:

سرعت و بهینه بودن (Virtual DOM).

کامپوننت‌محور بودن (قابل استفاده مجدد).

محبوب‌ترین انتخاب در فرانت‌اند طبق آمار.

مثال:
نمایش لیست کارها (Todos) و مدیریت وضعیت با React Hooks.

🚀 ترکیب Node.js + React

وقتی این دو رو با هم استفاده کنی:

Node.js ⇒ بک‌اند و API (مدیریت دیتابیس، احراز هویت، منطق اصلی برنامه).

React ⇒ فرانت‌اند برای نمایش داده‌ها و تعامل با کاربر.

یعنی می‌تونی یک اپلیکیشن کامل Full-Stack بسازی.
مثلاً یک Todo App پیشرفته که:

فرانت‌اند (React) → لیست کارها رو نشون میده.

بک‌اند (Node.js + Express + MongoDB) → کارها رو ذخیره و مدیریت می‌کنه.


===================================================================


