from app import app as application


#run app
if __name__ =="__main__":
    # application.debug=True
    application.run(debug=True, host='0.0.0.0')
    