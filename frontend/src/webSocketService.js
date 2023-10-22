import io from 'socket.io-client';

// Replace 'ws://your-backend-websocket-url' with the actual WebSocket URL of your Django backend.
// const socket = io('ws://127.0.0.1:8000/ws/test/', {
//   transports: ['websocket'],
// });

const socket = io('ws://127.0.0.1:8000/ws/test/', {
  transports: ['websocket'],
});

'ws://127.0.0.1:8000/socket.io/?EIO=4&transport=websocket'


const subscribeToUpdates = (channel, callback) => {
  socket.on(channel, callback);
};

const disconnect = () => {
  socket.disconnect();
};

export { subscribeToUpdates, disconnect };
