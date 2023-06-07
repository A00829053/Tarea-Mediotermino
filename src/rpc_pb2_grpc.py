# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import rpc_pb2 as rpc_dot_rpc__pb2


class RPCDemoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMultCoords = channel.unary_unary(
                '/grpcWrapper.RPCDemo/GetMultCoords',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=rpc_dot_rpc__pb2.MultCoord.FromString,
                )


class RPCDemoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetMultCoords(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RPCDemoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMultCoords': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMultCoords,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=rpc_dot_rpc__pb2.MultCoord.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpcWrapper.RPCDemo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RPCDemo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetMultCoords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpcWrapper.RPCDemo/GetMultCoords',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            rpc_dot_rpc__pb2.MultCoord.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
