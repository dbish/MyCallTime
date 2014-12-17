"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from MyCallTime import app
from MyCallTime.forms import ContactForm
import pypyodbc as pyodbc


def getConn():
    conn = pyodbc.connect('Driver={SQL Server};Server=tcp:.database.windows.net,1433;Database=MyCallTimeDB;Uid=;Pwd={};Encrypt=yes;Connection Timeout=30;')
    return conn

def insertDB(conn):
    cursor = conn.cursor()
    cursor.execute("insert into Shoots(ID, UserName, Name) values (3,'test', 'Example Shoot')")
    conn.commit()



@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    


  
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year
        
    )

@app.route('/contact') 
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/newSheet')
def newSheet():
    """Renders the about page."""
    conn = getConn()

    try:
        insertDB(conn)
    except:
        pass

    conn.close()

    return render_template(
        'newSheet.html',
        title='New Sheet',
        year=datetime.now().year,
        message='Your application description page.',
       
    )
