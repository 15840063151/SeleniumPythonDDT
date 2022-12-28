


# coding = utf-8


from handle.register_handle import RegisterHandle

class RegisterBusiness():
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self,email,name,password,code):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)
        self.register_h.click_register_button()
        
    # 检测是否有注册按钮 如果没有注册按钮 返回true 证明登录成功
    def register_success(self):
        if  self.register_h.get_register_text() == None:
            return True
        else:
            False


    #执行操作
    def register_function(self,email,username,password,code,assertCode,assertText):
        self.user_base(email,username,password,code)
        if self.register_h.get_user_text(assertCode,assertText) == None:
            return True
        else:
            return False
    

        
