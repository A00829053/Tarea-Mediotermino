using System;
using Grpc.Core;
using rpc2;
using Google.Protobuf.WellKnownTypes;

class Program
{
    static void Main(string[] args)
    {
        // Dirección y puerto del servicio RPC
        var serverAddress = "192.168.1.72:50051";

        // Crear el canal de comunicación con el servidor RPC
        var channel = new Channel(serverAddress, ChannelCredentials.Insecure);

        // Crear el cliente del servicio RPC
        var client = new rpc2.RPCDemo.RPCDemoClient(channel);

        // Llamar al método remoto para obtener las coordenadas del objeto
        var response = client.GetMultCoords(new Empty());

        // Mostrar las coordenadas en la terminal
        Console.WriteLine($"Coordenadas recibidas: x={response.Values[0]}, y={response.Values[1]}");

        // Cerrar el canal de comunicación
        channel.ShutdownAsync().Wait();
    }
}
