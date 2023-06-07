import rpc_pb2
import rpc_pb2_grpc
import grpc
from concurrent import futures
import logging
#import rospy

class RPCDemoImpl(rpc_pb2_grpc.RPCDemoServicer):
    data = []
    def __init__(self):
        self.data = [1,2,0]

    def update_data(self, data):
        self.data[0] = data.data[0]
        self.data[1] = data.data[1]
    
    def GetMultCoords(self, request, context):
        results = rpc_pb2.MultCoord()
        results.values.append(self.data[0])
        results.values.append(self.data[1])
        return results

def main():
    """server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    signal.signal(signal.sigint, terminate_server)
    rospy.init_node()
    server_addr = “[::]:7042
    """
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service = RPCDemoImpl()
    rpc_pb2_grpc.add_RPCDemoServicer_to_server(service, server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    main()