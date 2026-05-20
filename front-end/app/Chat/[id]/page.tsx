"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import { api } from "../../lib/api";  // one extra ../ since we're one level deeper now

export default function Chat() {
  const params = useParams();
  const resumeId = Number(params.id);  // grabs "23" from /Chat/23

  const [messages, setMessages] = useState<any[]>([]);
  const [question, setQuestion] = useState("");
  const [status, setStatus] = useState("");

  useEffect(() => {
    if (!resumeId) return;

    console.log("WS connecting:", resumeId);

    const ws = new WebSocket(`ws://localhost:8000/ws/${resumeId}`);

    ws.onopen = () => {
      console.log("WS connected");
    };

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);

      if (data.step) {
        setStatus(data.step);
      }

      if (data.answer) {
        setMessages((prev) => [...prev, { role: "assistant", text: data.answer }]);
      }
    };

    return () => {
      ws.close();
    };
  }, [resumeId]);

  const send = async () => {
    if (!question.trim() || !resumeId) return;

    setMessages((prev) => [...prev, { role: "user", text: question }]);

    const q = question;
    setQuestion("");

    await api.askQuestion(resumeId, q);
  };

  return (
    <div className="h-screen flex flex-col bg-black">
      <div className="flex-1 overflow-y-auto max-w-4xl mx-auto w-full p-6 space-y-6">
        {messages.map((m, i) => (
          <div key={i} className={m.role === "user" ? "flex justify-end" : "flex justify-start"}>
            <div
              className={`max-w-xl rounded-2xl px-5 py-4 ${
                m.role === "user" ? "bg-green-600 text-white" : "bg-zinc-800 text-white"
              }`}
            >
              {m.text}
            </div>
          </div>
        ))}

        {status && (
          <div className="text-center text-sm text-zinc-400 animate-pulse">
            {status === "retrieving_context" && "Searching resume…"}
            {status === "thinking" && "Thinking…"}
            {status === "completed" && "Done"}
          </div>
        )}
      </div>

      <div className="border-t border-zinc-800 p-5">
        <div className="max-w-4xl mx-auto flex gap-3">
          <input
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && send()}
            placeholder="Ask about resume..."
            className="flex-1 bg-zinc-900 text-white rounded-xl p-4 outline-none"
          />
          <button onClick={send} className="bg-white text-black px-6 rounded-xl">
            Send
          </button>
        </div>
      </div>
    </div>
  );
}