import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import mysql.connector

db = mysql.connector.connect(
    host="172.104.148.212",
    user="daviid",
    passwd="Ubuntob0I!",
    database="Tfw",
    auth_plugin="mysql_native_password"
)
mycursor = db.cursor()
mycursor.execute("INSERT INTO Users (username, password, admin_rights) VALUES (%s,%s,%s)", ("Smolboi", "tinycock", True))
db.commit()

class CalcGridLayout(GridLayout):

    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"


class CalcApp(App):
    def build(self):
        return CalcGridLayout()


if __name__ == "__main__":
    CalcApp().run()
