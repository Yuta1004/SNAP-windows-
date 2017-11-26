from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


def main():
    with open(cu_dir + "\\pass.txt") as f:
        file_ = f.read()
        file_ = file_.split()
        username = file_[0]
        password = file_[1]
    print("Username : {0}".format(username))
    print("Password : " + "*" * len(password))
    print("Connecting...")
    url = "https://captive-yuge.variosecure.net/captive/"
    driver = webdriver.PhantomJS()
    driver.get(url + "login")

    try:
        time.sleep(1)
        print("Logging in...")
        inp_user = driver.find_element_by_name("user")
        inp_user.send_keys(username)
        inp_pass = driver.find_element_by_name("password")
        inp_pass.send_keys(password)
        inp_pass.send_keys(Keys.RETURN)
        if driver.current_url == url + "control":
            print("Login Success!")
            print("ok!")
        else:
            print("Login Faild")
    except Exception as e:
        print("Error")

    driver.quit()


if __name__ == '__main__':
    cu_dir = os.path.dirname(os.path.abspath(__file__))
    os_env = os.environ.get("Path")
    os_env_list = os_env.split(";")
    phantom_path = cu_dir + "\\phantomjs-2.1.1-windows\\bin"
    if not phantom_path in os_env_list:
        os.environ["Path"] = os_env + ";" + phantom_path
    main()
