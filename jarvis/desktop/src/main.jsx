import React,{useEffect,useRef,useState} from "react";
import {createRoot} from "react-dom/client";
import "./style.css";
import { Activity, BrainCircuit, ShieldCheck, Mic, Volume2 } from "lucide-react";

function App(){
 const [messages,setMessages]=useState([]);
 const [input,setInput]=useState("");
 const [online,setOnline]=useState(false);
 const [thinking,setThinking]=useState(false);\n const [activity,setActivity]=useState("STANDBY");\n const [activeAgent,setActiveAgent]=useState("CORE");
 const [time,setTime]=useState(new Date());
 const ws=useRef(null);
 useEffect(()=>{
   const timer=setInterval(()=>setTime(new Date()),1000);
   const url=(location.protocol==="https:"?"wss":"ws")+"://"+(location.hostname||"localhost")+":8000/v1/ws";
   try{
     ws.current=new WebSocket(url);
     ws.current.onopen=()=>setOnline(true);
     ws.current.onclose=()=>{setOnline(false);setThinking(false)};
     ws.current.onmessage=e=>{
       const d=JSON.parse(e.data);
       if(d.response){setMessages(m=>[...m,{role:"jarvis",text:d.response}]);setThinking(false);setActivity("COMPLETE")}\n       if(d.event==="jarvis.action.started"){setThinking(true);setActivity("EXECUTING");setActiveAgent((d.target||"CORE").toUpperCase())}\n       if(d.event==="jarvis.action.completed"){setActivity("PROCESSING")}\n       if(d.event==="jarvis.plan.created"){setActivity("PLANNING")}\n       if(d.event==="jarvis.command.received"){setActivity("ANALYZING")}
     };
   }catch{}
   return()=>{clearInterval(timer);ws.current?.close()}
 },[]);
 const send=()=>{
   if(!input.trim())return;
   const text=input.trim();
   setMessages(m=>[...m,{role:"user",text}]);
   setThinking(true);
   if(ws.current?.readyState===WebSocket.OPEN) ws.current.send(text);
   else setMessages(m=>[...m,{role:"jarvis",text:"Gateway offline. Start the JARVIS Python gateway on port 8000."}]);
   setInput("");
 };
 return <main>
   <div className="scanline"/>
   <header>
    <div className="brand"><b>JARVIS</b><span>COGNITIVE COMMAND SYSTEM</span></div>
    <div className="header-right"><span>{time.toLocaleTimeString()}</span><i className={online?"on":""}><em/> {online?"ONLINE":"OFFLINE"}</i></div>
   </header>
   <div className="quick-actions"><button title="Voice mode"><Mic size={16}/></button><button title="Audio output"><Volume2 size={16}/></button><span><Activity size={13}/> LIVE COGNITIVE FEED</span></div>\n   <div className="dashboard">
    <aside className="side left">
      <div className="panel"><label><Activity size={12}/> SYSTEM CORE</label><strong>{online?"ACTIVE":"STANDBY"}</strong><div className="meter"><span/></div></div>
      <div className="panel"><label><BrainCircuit size={12}/> COGNITION</label><div>REASONING <b>READY</b></div><div>MEMORY <b>READY</b></div><div>AGENTS <b>ONLINE</b></div></div>
      <div className="panel"><label><ShieldCheck size={12}/> SECURITY</label><div className="secure">● ENFORCED</div></div>
    </aside>
    <section className="center">
      <div className={"reactor "+(thinking?"thinking":"")}>
        <div className="arc a1"/><div className="arc a2"/><div className="arc a3"/>
        <div className="core"><span>J</span></div>
        <div className="pulse"/>
      </div>
      <div className="core-title">JARVIS <span>◈</span> {thinking?activity:"READY"}</div><div className="active-agent">ACTIVE NODE // {activeAgent}</div>
      <div className="equalizer">{Array.from({length:18},(_,i)=><i key={i}/>)}</div>
    </section>
    <aside className="side right">
      <div className="panel"><label>AGENT MATRIX</label>{["PLANNER","RESEARCH","CODER","VISION","BROWSER","COMPUTER"].map((x,i)=><div className="agent" key={x}><span>{String(i+1).padStart(2,"0")}</span>{x}<b>●</b></div>)}</div>
      <div className="panel"><label>TASK ENGINE</label><div>QUEUE <b>READY</b></div><div>DAG <b>ACTIVE</b></div><div>WORKERS <b>4</b></div></div>
    </aside>
   </div>
   <section className="log">{messages.length===0?<div className="empty">AWAITING COMMAND<span>Say something to JARVIS</span></div>:messages.map((m,i)=><div key={i} className={"message "+m.role}><small>{m.role==="user"?"YOU":"JARVIS"}</small>{m.text}</div>)}</section>
   <footer><div className="input-wrap"><span>›</span><input value={input} onChange={e=>setInput(e.target.value)} onKeyDown={e=>e.key==="Enter"&&send()} placeholder="Command JARVIS..." /></div><button onClick={send}><span>⌁</span> EXECUTE</button></footer>
 </main>
}
createRoot(document.getElementById("root")).render(<App/>);