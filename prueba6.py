from requests_html import HTMLSession, AsyncHTMLSession
from selenium import webdriver


def main():
    url = "https://eclass.unida.edu.py/infou/loginalumnos.asp"
    session = HTMLSession()
    r = session.get(url)
    driver = webdriver.Firefox(executable_path=r'D:\CursoPython\geckodriver.exe')


if __name__ == "__main__":
    main()
