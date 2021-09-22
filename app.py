from flask import Flask, jsonify, request
import bot
import utilis
app=Flask(__name__)


@app.route("/chat",methods=["POST"])
def chat():
    request_data=request.get_json()
    message=request_data['message']
    data={}
    status, response=bot.chat(message)
    if status==0:
        data["reply"]=response
        data["status"]='success'
        return jsonify(data)
    else:
        data["reply"]=response
        data["status"]='failed'
        return jsonify(data)

    return response

@app.route("/test",methods=["POST"])
def test():
    request_data=request.get_json()
    message=request_data['message']
    print(message)
    return jsonify(utilis.save(message))


if __name__=="main":
    app.run()
