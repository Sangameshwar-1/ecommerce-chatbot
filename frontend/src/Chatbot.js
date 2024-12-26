import React, { useState } from 'react';

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleSend = async () => {
    const userMessage = { role: 'user', content: input };
    setMessages([...messages, userMessage]);

    const response = await fetch(`${process.env.REACT_APP_BACKEND_URL}/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: input }),
    });
    const botReply = await response.json();

    setMessages((prev) => [...prev, { role: 'bot', content: botReply.answer }]);
    setInput('');
  };

  return (
    <div>
      <h1>E-commerce Chatbot</h1>
      <div className="chat-box">
        {messages.map((msg, index) => (
          <p key={index} className={msg.role}>
            {msg.content}
          </p>
        ))}
      </div>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask me something..."
      />
      <button onClick={handleSend}>Send</button>
    </div>
  );
};

export default Chatbot;
