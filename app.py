import streamlit as st
import yaml
from yaml.loader import SafeLoader
from streamlit_cookies_controller import CookieController


st.set_page_config(page_title="Forecast+ ", layout="wide")

controller = CookieController()


with open('auth_config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)




def check_credentials(username, password):
    
    if username in config['credentials']['usernames']:
        
        if config['credentials']['usernames'][username]["password"] == password:
            
            return True
    return False

def authentication_ui():

    placeholder = st.empty()

    with placeholder.form("login"):
        st.markdown("#### Enter your credentials")
        username = st.text_input("User")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
    
    if submit and check_credentials(username, password):
        placeholder.empty()
        controller.set('login_status', True)
        st.success("Login successful")
    
    elif submit:
        st.error("Either username or password is incorrect")



def i_am_in():
    st.write("WELCOME USER")
    if st.button("Log out"):
        controller.remove('login_status')


def check_password():
    if not controller.get('login_status'):
        authentication_ui()

    if controller.get("login_status"): 
        st.write("We are logged in ;)")
        return True
        
    

if __name__ == '__main__':
    check_password()
    

