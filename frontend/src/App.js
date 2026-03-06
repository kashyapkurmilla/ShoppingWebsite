import { useState, useEffect } from "react";

function App() {

  const [text,setText] = useState("");
  const [messages,setMessages] = useState([]);

  const send = async () => {

    await fetch("http://localhost:8000/add",{
      method:"POST",
      headers:{
        "Content-Type":"application/json"
      },
      body: JSON.stringify({text})
    })

    loadMessages()
  }

  const loadMessages = async () => {

    const res = await fetch("http://localhost:8000/messages")
    const data = await res.json()

    setMessages(data)
  }

  useEffect(()=>{
    loadMessages()
  },[])

  return (
    <div>

      <h1>Furniture Project Test</h1>

      <input
        value={text}
        onChange={e=>setText(e.target.value)}
      />

      <button onClick={send}>
        Save
      </button>

      <h2>Messages</h2>

      <ul>
        {messages.map((m,i)=>(
          <li key={i}>{m[0]}</li>
        ))}
      </ul>

    </div>
  );
}

export default App;