import socket
import json
import threading
import multiprocessing
print("+: Network")

class Load:
    def __init__(self, ip):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = str(ip)
        self.port = 5555
        self.addr = (self.server, self.port)

        self.q_RECEIVE = multiprocessing.Queue()
        self.q_SEND = multiprocessing.Queue()
        self.q_STATUS = multiprocessing.Queue()

    def start(self):
        self.p1 = multiprocessing.Process(target=self.connect, args=(self.q_SEND, self.q_RECEIVE, self.q_STATUS))
        self.p1.daemon = True
        self.p1.start()

    def end(self):
        self.p1.terminate()

    def connect(self, q_send, q_receive, q_status):
        try:
            self.client.connect(self.addr)
            q_status.put({"-1000": "Online"})
            t1 = threading.Thread(target=self.send, args=(q_send,))
            t2 = threading.Thread(target=self.listen, args=(q_receive,))
            t2.start()
            t1.start()
        except Exception as e:
            q_status.put({"-1000": "Offline"})


    def listen(self, q_receive):
        rec = []
        try:
            while True:
                try:
                    rec.append(self.client.recv(1024))
                    data = json.loads(rec.pop().decode())
                    q_receive.put(data)
                except Exception as e:
                    pass

        except Exception as e:
            print(e)
            pass


    def send(self, q_send):
        try:
            while True:
                if not q_send.empty():
                    try:
                        msg = q_send.get()
                        self.client.send(json.dumps(msg).encode())
                    except Exception as e:
                        print(e)
                        break
        except Exception as e:
            print(e)

print("-: Network")