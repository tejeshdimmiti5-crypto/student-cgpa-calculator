import React,{useEffect,useRef,useState} from "react";
import {createRoot} from "react-dom/client";
import "./style.css";

function App(){
 const [messages,setMessages]=useState([]);
 const [input,setInput]=useState("");
 const [online,setOnline]=useState(false);
 const ws=useRef(null);
 useEffect(()=>{const url=(location.protocol==="https:"?"wss":"ws")+"://"+(location.hostname||"localhost")+":8000/v1/ws"; try{ws.current=new WebSocket(url);ws.current.onopen=()=>setOnline(true);ws.current.onclose=()=>setOnline(false);ws.current.onmessage=e=>{const d=JSON.parse(e.data);if(d.response)setMessages(m=>[...m,{role:"jarvis",text:d.response}]);}}catch{} return()=>ws.current?.close()},[]);
 const send=()=>{if(!input.trim())return;const text=input.trim();setMessages(m=>[...m,{role:"user",text}]);ws.current?.send(text);setInput("")};
 return <main><header><div><b>JARVIS</b><span> COGNITIVE CORE</span></div><i className={online?"on":""}>{online?"ONLINE":"OFFLINE"}</i></header><section className="orb"><div className="ring">J</div><p>JARVIS READY</p></section><section className="log">{messages.map((m,i)=><div key={i} className={m.role}>{m.text}</div>)}</section><footer><input value={input} onChange={e=>setInput(e.target.value)} onKeyDown={e=>e.key==="Enter"&&send()} placeholder="Command JARVIS..." /><button onClick={send}>SEND</button></footer></main>
}
createRoot(document.getElementById("root")).render(<App/>);