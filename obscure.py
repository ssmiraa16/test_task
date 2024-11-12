class EmailObscurer:
    def __init__(self, obscuring_char='x'):
        self.obscuring_char = obscuring_char
    def obscure(self, email):
        if '@' not in email:
            raise ValueError("Invalid email format")
        parts = email.split('@')
        local_part = parts[0]
        domain = parts[1]
        obscured_local_part = self.obscuring_char * len(local_part)
        return f"{obscured_local_part}@{domain}"
class PhoneNumberObscurer:
    def __init__(self, obscuring_char='x', num_chars_to_obscure=3):
        self.obscuring_char = obscuring_char
        self.num_chars_to_obscure = num_chars_to_obscure
    def obscure(self, phone_number):
        clean_phone_number = ' '.join(phone_number.split())

        obscured_part = self.obscuring_char * self.num_chars_to_obscure
        length_to_keep = max(len(clean_phone_number) - self.num_chars_to_obscure, 0)
        visible_part = clean_phone_number[:length_to_keep].strip()

        return f"{visible_part} {obscured_part}".strip()

class SkypeObscurer:
    def __init__(self, obscuring_char='xxx'):
        self.obscuring_char = obscuring_char
    def obscure(self, skype):
        if "skype:" in skype:
            start_index = skype.find("skype:")
            end_index = skype.find("?", start_index)
            if end_index == -1:
                end_index = len(skype)
            obscure = "skype:" + "xxx"
            skype = skype[:start_index] + obscure + skype[end_index:]
        return skype

email_obscurer = EmailObscurer()
print(email_obscurer.obscure('example@example.com'))

phone_obscurer = PhoneNumberObscurer()
print(phone_obscurer.obscure('+7 123 456 7890'))
print(phone_obscurer.obscure('+7 123   456 7890'))

skype_masker = SkypeObscurer()

simple_skype_link = "skype:alex.max"
result_simple = skype_masker.obscure(simple_skype_link)
print(result_simple)

html_skype_link = '<a href="skype:alex.max?call">skype</a>'
result_html = skype_masker.obscure(html_skype_link)
print(result_html)