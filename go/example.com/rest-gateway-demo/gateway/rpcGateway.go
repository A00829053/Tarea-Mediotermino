package main

import (
	"context"
	"flag"
	"log"
	"net/http"

	"github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
	"google.golang.org/grpc"

	pb "example.com/rest-gateway-demo/protos"
)

var (
	grpcServerEndpoint = flag.String("grpc-server-endpoint","127.0.0.1:50051", "gRPC svr endpoint")
	port = "8080"
)

func run() error {
	//"""ctx := context.Background()
	//ctx, cancel := context.WithCancel()
	//defer cancel()"""
	gwmux := runtime.NewServeMux()
	opts := []grpc.DialOption{grpc.WithInsecure()}
	err := pb.RegisterRPCDemoHandlerFromEndpoint(context.Background(), gwmux, "127.0.0.1:50051", opts)
	if err != nil {
		return err
	}

	return http.ListenAndServe(":"+port, gwmux)
}

func main() {
	log.Println("Starting gateway at port: " + port)
	if err := run(); err!=nil {
		log.Fatalf("Failed to register gRPC-Gateway: %v", err)
	}
}
