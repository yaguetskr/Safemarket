import ssl

from market import app

#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain("cert.pem", keyfile="key.pem")
    app.run(ssl_context=context,debug=True,port=5000)