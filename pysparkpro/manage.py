# coding:utf-8
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit
from urllib.parse import unquote
from dsl.lexer import lexer
from dsl.parser import parser
from session.abstract_class import PysparkPro

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['JSON_AS_ASCII'] = False

socketio = SocketIO(app)
spark = PysparkPro().pysparkpro


@app.route('/')
def index():
    return render_template('socket.html')


@socketio.on('client_event', namespace='/test')
def client_msg(msg):
    cur = unquote(msg["data"])
    result = parser.parse(cur, lexer=lexer)
    from execute.main import execute_main
    # execute_main(result, lexer, spark)
    data = spark.read.csv(
        "file:///Users/leiqiankun/PycharmProjects/lqkcode/tianchi/pysparkpro/test/testflask/data/tianchi_fresh_comp_train_item.csv",
        header=True)
    data.createOrReplaceTempView("A")
    datatem = spark.sql(lexer.lexdata.replace(";", ""))
    datat_response = datatem.rdd.collect()
    emit('server_response', {'data': datat_response})


@socketio.on('connect_event')
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
