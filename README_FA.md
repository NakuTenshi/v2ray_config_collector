# v2ray config collector
<a href="https://github.com/NakuTenshi/v2ray_config_collector/">English</a>

فایل `collect.py` یک اسکریپت پایتون است که پیکربندی‌های (configs) v2ray را از منابع داده شده در `raw.githubusercontent.com` جمع‌آوری کرده و آن‌ها را از طریق TCP handshake تست می‌کند.


## نحوه استفاده
: قبل از هر چیزی شما باید این ریپو رو کلون کنید 

```bash
git clone https://github.com/NakuTenshi/v2ray_config_collector ; 
cd v2ray_config_collector
```

: سپس شما نیاز دارید کتابخانه های مورد نیاز اسکریپت را دانلود کنید

``` bash 
pip3 install -r requirements.txt
```


: بعد از همه چیز شما میتونید به راحتی این اسکریپت را اجرا کنید

```bash
python3 collect.py
```
لذت ببرید


## نوت

> فایل ``` sources.txt ``` باید کنار فایل ```collect.py``` در یک مسیر باشند

> اگه شما میخواید یک سورس دیگری را مدنظر دارید میخواید کانفیگ های ان هم تست شود, به راحتی میتوانید لینک ان را به  ``` sources.txt ``` اضافه کنید

> فایل ``` raw_sources.txt ``` سورس هایی هستن که هنوز تست نشدن
