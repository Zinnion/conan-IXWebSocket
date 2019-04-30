#include <ixwebsocket/IXWebSocket.h>
#include <ixwebsocket/IXSocket.h>

int main(int argc, char ** argv) {

  ix::WebSocket webSocket;

  std::string url("ws://localhost:8080/");
  webSocket.setUrl(url);

  // Optional heart beat, sent every 45 seconds when there is not any traffic
  // to make sure that load balancers do not kill an idle connection.
  webSocket.setHeartBeatPeriod(45);

  // Setup a callback to be fired when a message or an event (open, close, error) is received
  webSocket.setOnMessageCallback(
    [](ix::WebSocketMessageType messageType,
      const std::string & str,
        size_t wireSize,
        const ix::WebSocketErrorInfo & error,
          const ix::WebSocketOpenInfo & openInfo,
            const ix::WebSocketCloseInfo & closeInfo) {
      if (messageType == ix::WebSocket_MessageType_Message) {
        std::cout << str << std::endl;
      }
    });

  // Now that our callback is setup, we can start our background thread and receive messages
  webSocket.start();

  // Send a message to the server (default to BINARY mode)
  webSocket.send("hello world");

  // Stop the connection
  webSocket.stop();

  return 0;
}
