
def generate_message(status, name,  *args, **kwargs):
    """
    Generate a message to send via SMS
    """
    if status == "Accept-TEC":
        pass

    elif status == "Accept-HR":
        pass

    elif status == "Task":
        message = (f"آکادامی ایستا"
                   f"سلام {name} جان به کارخونه هیولاسازی فرانت اند خوش اومدی برات چالش فنی رو ارسال کردیم برو ایمیل ات چک کن"
                   f" بترکونی بچه هیولا...)")
        return message

