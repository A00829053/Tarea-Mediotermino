#!/usr/bin/env python
import rpc_pb2
import rpc_pb2_grpc
import grpc
from concurrent import futures
import logging
import rospy
from std_msgs.msg import Float64MultiArray

class RPCDemoImpl(rpc_pb2_grpc.RPCDemoServicer):
    data = []

    def __init__(self):
        self.data = [1,2,0]

    def update_data(self, msg):
        self.data[0] = msg.data[0]
        self.data[1] = msg.data[1]
    # Create a subscriber for the coordinates topic
    rospy.Subscriber('coords', Float64MultiArray, update_data)
    rospy.spin()
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
    # Initialize the ROS node
    rospy.init_node('grpc_server', anonymous=True)
    logging.basicConfig()
    main()