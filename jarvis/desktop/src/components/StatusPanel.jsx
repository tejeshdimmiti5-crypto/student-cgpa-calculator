import { Activity, BrainCircuit, ShieldCheck } from "lucide-react";

export default function StatusPanel({online,thinking=false}) {
  return (
    <aside className="component-panel">
      <strong><Activity size={13}/> SYSTEM</strong>
      <div>CORE: <b>{online ? "ACTIVE" : "OFFLINE"}</b></div>
      <div>COGNITION: <b>{thinking ? "PROCESSING" : "READY"}</b></div>
      <div>MEMORY: <b>READY</b></div>
      <div>AGENTS: <b>{thinking ? "BUSY" : "READY"}</b></div>
      <div>SECURITY: <b>ENFORCED</b></div>
      <div className="signal"><i/><i/><i/><i/><i/></div>
    </aside>
  );
}
