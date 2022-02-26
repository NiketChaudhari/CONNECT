
import sys
import sqlite3,os
from flask import Flask, request, session, send_file,jsonify,Response
import socket
from werkzeug.utils import secure_filename

working_dir = os.getcwd()
# working_dir = working_dir.replace(r"/Connection","")


MY_HOST_NAME = socket.gethostname()
MY_IP_ADDRESS = socket.gethostbyname(MY_HOST_NAME)



app = Flask(__name__)



@app.route('/')
def Connect():
    return "Connect !"


@app.route('/host_check/<string:send_hostname>/<string:send_username>/<string:send_password>')
def host_check(send_hostname,send_username,send_password):

    try :
        conn = sqlite3.connect(os.path.join(working_dir,'Log','Connect.db'))
        cur = conn.cursor()
        cur.execute("SELECT * FROM CONNECT")
        rows = cur.fetchall()
        conn.commit()
        conn.close()
    except Exception as e :
        rows = []
        print("Connection.db Exception : ",e)

    try :
        if((send_hostname==rows[0][1]) and (send_username==rows[1][1]) and (send_password==rows[2][1])) :
            return "Connected"
        else :
            return "Not Connected"
    except :
        return "Not Connected"


@app.route('/file_structure_start')
def file_structure_start() :
    send_json = {}
    send_json["fold_path"] = working_dir

    file_fold_dict = {}

    files = os.listdir(working_dir)

    try :
        for f in files:
            if os.path.isdir(os.path.join(working_dir,f)) :  
                file_fold_dict[f] = "1" 
            elif os.path.isfile(os.path.join(working_dir,f)) : 
                file_fold_dict[f] = "0"   
            else:  
                pass
    except :
        pass

    send_json["fold_struct"] = file_fold_dict

    return jsonify(send_json)







@app.route('/file_structure/<string:send_path>')
def file_structure(send_path) :

    send_json = {}
    send_json["fold_path"] = send_path


    file_fold_dict = {}

    files = os.listdir(send_path)

    try :
        for f in files:
            if os.path.isdir(os.path.join(send_path,f)) :  
                file_fold_dict[f] = "1" 
            elif os.path.isfile(os.path.join(send_path,f)) : 
                file_fold_dict[f] = "0"   
            else:  
                pass
    except :
        pass

    send_json["fold_struct"] = file_fold_dict

    return jsonify(send_json)



 
@app.route('/file_upload/<path:upload_folder>', methods=['GET', 'POST'])
def file_upload(upload_folder):
    try:
        file_received = request.files['file']
        upload_file = secure_filename(file_received.filename)

        file_upload_path = os.path.join(upload_folder,upload_file)

        file_received.save(file_upload_path)

        return "200"

    except Exception as e :
        print(e)
        return "404"



@app.route('/file_download/<path:download_file>', methods=['GET', 'POST'])
def file_download(download_file):
    try :

        if (os.path.exists(download_file)) :
            return send_file(download_file, as_attachment=True)
        else:
            status_code = Response(status=404)
            return status_code
    except :
        status_code = Response(status=404)
        return status_code    


@app.route('/file_delete/<path:delete_file>', methods=['GET', 'POST'])
def file_delete(delete_file):
    try :

        if (os.path.exists(delete_file)) :
            os.remove(delete_file)

            status_code = Response(status=200)
            return status_code
        else:
            status_code = Response(status=404)
            return status_code
    except :
        status_code = Response(status=404)
        return status_code 

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(host=MY_IP_ADDRESS, port=50111)