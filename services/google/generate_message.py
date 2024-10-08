def generate_message(first_name, status):
    recipient_name = f"{first_name} جان   "
    if status == "task":
        email_body_html = f"""
          <!DOCTYPE html>
          <html>
             <head>
                <style>
                   body {{
                   font-family: Sans-serif;
                   font-size: 20px;
                   text-align: right;
                   direction: rtl;
                   }}
                   .id{{
                   text-align: left;
                   direction: ltr;
                   }}
                </style>
             </head>
             <body>
                <h3>سلام {recipient_name} </h3>
        <p>امیدواریم حالت خوب باشه</p>
        <p>به کارخونه هیولاسازی فرانت اند خوش اومدی</p>
        <p>توی مرحله اول</p>
        <p>برای اینکه مطمئن بشیم پیش نیازهای کلاس رو بهش مسلط هستی</p>
        <p>باید ازت یه تست فنی بگیریم</p>
        <p>اصلا هم سخت نیست خیالت راحت می دونیم از پس ش برمیای</p>
        <p>از لحظه دریافت این ایمیل چهار روز وقت داری چالش رو برامون ارسال کنی</p>
        <p>حواست به زمان خیلی باشه</p>
        <p>بترکونی بچه هیولا....:)</p>
        <p>لینک آپلود تسک </p>
        <a href="https://www.istaacademy.com/upload_task"></<p>
            <div class="id">
              <h3>اگر به مشکل برخوردی به آیدی زیر در تلگرام پیام بده</h3>
               @ista_support
            </div>
             </body>
          </html>
          """
        return email_body_html

    elif status == "accept-task":
        email_body_html = f"""
              <!DOCTYPE html>
              <html>
                 <head>
                    <style>
                       body {{
                       font-family: Sans-serif;
                       font-size: 20px;
                       text-align: right;
                       direction: rtl;
                       }}
                       .id{{
                       text-align: left;
                       direction: ltr;
                       }}
                    </style>
                 </head>
                 <body>
                    <h4>سلام {recipient_name}</h4>
         <p>دمت گرم بابت ارسال چالش</p>
        <p>می دونستیم از پسش برمیای</p>
        <p>توی مرحله دوم</p>
        <p>چون توی کلاس قراره پروژه رو بصورت گروهی با هم پیش ببریم و تعامل خیلی برامون مهمه</p>
        <p>باید ازت یه تست Soft Skill بگیریم</p>
        <p>چیز عجیب و غریبی هم نیست با یک HR به مدت نیم ساعت باید مصاحبه داشته باشی</p>
        <p>زمان مصاحبه رو از طریق لینک زیر برامون تعیین کن...</p>
        <p>تا اینجاشو که اومدی...می دونیم از پس این چالش هم برمیای</p>
        <p>بترکونی بچه هیولا....:)</p>
        <p>لینک تعیین زمان مصاحبه</p>
        <a href="https://www.istaacademy.com/reservation"></a>
                    <div class="id">
                      <h3>اگر به مشکل برخوردی به آیدی زیر در تلگرام پیام بده</h3>
                       @ista_support
                    </div>
                 </body>
              </html>
              """
        return email_body_html

    elif status == "accept-hr":
        email_body_html = f"""
              <!DOCTYPE html>
              <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Front-End Monster Factory - Final Step</title>
            </head>
                 <body>    
            <div style="text-align: justify;">
                <h4>سلام {recipient_name}</h4>
                <h3>مرحله دوم رو هم تایید شدی</h3>
                <p>دمت گرم</p>
                <p>می دونستیم از پس HR جماعت برمیای 😉</p>
                <p>برای مرحله آخر فقط باید وارد لینک زیر بشی و قسط اول دوره رو پرداخت کنی</p>
                <!-- Replace the following line with the actual payment link -->
                <a href="YOUR-PAYMENT-LINK-HERE">Click here to make your payment</a>
                <p>خیلی زود می بینیمت بچه هیولا....</p>
            </div>
            <div class="id">
            <h3>اگر به مشکل برخوردی به آیدی زیر در تلگرام پیام بده</h3>
            @ista_support
            </div>
        </body>
              </html>
              """
        return email_body_html

    elif status == "reject-hr":
        email_body_html = f"""
              <!DOCTYPE html>
              <html>
                 <head>
                    <style>
                       body {{
                       font-family: Sans-serif;
                       font-size: 20px;
                       text-align: right;
                       direction: rtl;
                       }}
                       .id{{
                       text-align: left;
                       direction: ltr;
                       }}
                    </style>
                 </head>
                 <body>
                    <h4>سلام {recipient_name}</h4>
                <p class="persian-text">امیدواریم حالت خوب باشه</p>
                <p class="persian-text">متاسفانه تایید کارشناس HR رو نتونستی بگیری</p>
                <p class="persian-text">همه ما می دونیم که یه بخشی از مسائل مربوط به HR سلیقه ای هست و صرفا به این معنا نیست که توی بخش Soft Skill ضعف داری</p>
                <p class="persian-text">در کل فدای سرت</p>
                <p class="persian-text">بهترین ها رو برات آرزو می کنیم</p>
                 </body>
              </html>
              """
        return email_body_html

    elif status == "reject-task":
        email_body_html = f"""
              <!DOCTYPE html>
              <html>
                 <head>
                    <style>
                       body {{
                       font-family: Sans-serif;
                       font-size: 20px;
                       text-align: right;
                       direction: rtl;
                       }}
                       .id{{
                       text-align: left;
                       direction: ltr;
                       }}
                    </style>
                 </head>
                 <body>
                    <h4>سلام {recipient_name}</h4>
                    <p>امیدواریم حالت خوب باشه</p>
                    <p>متاسفانه توی چالش فنی نتوسنتی تایید بگیری</p>
                    <p>فدای سرت</p>
                    <p>بهترین ها رو برات آرزو می کنیم</p>
                 </body>
              </html>
              """
        return email_body_html

