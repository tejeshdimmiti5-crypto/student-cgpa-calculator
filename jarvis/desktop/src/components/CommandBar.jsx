export default function CommandBar({value,onChange,onSend,disabled=false}) {
  return (
    <footer>
      <div className="input-wrap">
        <span>›</span>
        <input autoFocus value={value} onChange={e=>onChange(e.target.value)}
          onKeyDown={e=>e.key==="Enter"&&!disabled&&onSend()}
          placeholder={disabled ? "JARVIS IS THINKING..." : "Command JARVIS..."} />
        <kbd>ENTER</kbd>
      </div>
      <button disabled={disabled} onClick={onSend}><span>⌁</span> EXECUTE</button>
    </footer>
  );
}
